# digitalmate.io — go-live runbook

Written 2026-09-22. Follow top to bottom. Each step says exactly what to click and what to check
before moving on.

---

## ⚠️ Read this first: the domain already has live email

I looked up the domain's current DNS. These records exist **and must survive the move**:

| Type | Name | Value | What it does |
|---|---|---|---|
| MX | `digitalmate.io` | `smtp.google.com` (priority 1) | **Google Workspace email** — mail to @digitalmate.io |
| TXT | `digitalmate.io` | `v=spf1 include:_spf.google.com ~all` | lets Google send mail as your domain |
| TXT | `digitalmate.io` | `google-site-verification=5wsbUpxBdTHvdBGgiQL9s6MVMPxAT8URQkmYJ0xTRWU` | proves domain ownership to Google |
| TXT | `_dmarc.digitalmate.io` | `v=DMARC1; p=quarantine; rua=mailto:dmarc@digitalmate.io` | anti-spoofing policy |
| A | `digitalmate.io` | `76.223.105.230`, `13.248.243.5` | the GoDaddy builder site — these get replaced |
| CNAME | `www` | `digitalmate.io` | gets replaced |

**Good news:** `@digitalmate.io` mailboxes already work through Google Workspace. So you may not need
to create a new mailbox at all — check which addresses exist and use a real one on the site.

**The rule for the whole move:** the A and CNAME records change; **everything mail-related stays
exactly as it is.** Lose the MX record and mail stops the same day.

---

## Step 0 — ✅ DONE: contacts are in the files

- Company address published on every page: **Hi@digitalmate.io**
- Phone published on every page: **+995 599 525 282**
- CTA band (the block with Valerian's photo) uses his own **v.gegidze@gmail.com**

⚠️ **Confirm Hi@digitalmate.io actually receives mail** before the bank sees it. Send a test message
to it from an outside address. A published address that bounces is worse than no address at all.

---

## Step 1 — Create the Cloudflare account (5 minutes)

1. Go to **https://dash.cloudflare.com/sign-up**.
2. Sign up with a **company mailbox you control long-term** — not a personal Gmail. If Workspace is
   on the domain, `info@digitalmate.io` is ideal.
3. Confirm the verification email.
4. Turn on two-factor authentication: **My Profile → Authentication → Two-Factor**. This account will
   control the domain's DNS, so protect it properly.

---

## Step 2 — Upload the site (5 minutes)

1. In the dashboard sidebar: **Compute (Workers & Pages)** → **Create** → **Pages** tab →
   **Upload assets**.
2. Project name: `digitalmate` → **Create project**.
3. Drag the **contents** of `d:\Downloads\digitalmate-site\` into the upload area — the files
   themselves, not the folder around them. It must include `index.html` at the top level plus the
   `images` folder.
4. **Deploy site**.
5. You get `https://digitalmate.pages.dev`. Open it and check:
   - the homepage loads with the photo in the CTA band
   - Imprint, Privacy and Terms open from the footer
   - it looks right on a phone

**Share this link with whoever needs to review.** The old site stays live and untouched at
digitalmate.io throughout.

---

## Step 3 — Make your corrections (however long it takes)

Send me the changes; I'll edit the files and you re-upload:
**Pages project → Create deployment → Upload assets → drag the folder → Deploy.**

Each deployment gets its own URL and you can roll back to any earlier one from the deployment list.
Free plan allows 500 deployments a month, so change it as often as you like.

Do not go past this step until the phone number and the real email address are in place.

---

## Step 4 — Add the domain to Cloudflare (10 minutes + waiting)

Cloudflare needs to run the DNS for `digitalmate.io`, because a root domain can't be pointed at
Pages with a plain CNAME at GoDaddy.

1. Dashboard → **Add a domain** → type `digitalmate.io` → choose the **Free** plan.
2. Cloudflare scans your existing DNS and lists what it found. **This is the critical screen.**
   Check that all of these are present, and add any that are missing:

   | Type | Name | Value | Priority |
   |---|---|---|---|
   | MX | `digitalmate.io` | `smtp.google.com` | 1 |
   | TXT | `digitalmate.io` | `v=spf1 include:_spf.google.com ~all` | — |
   | TXT | `digitalmate.io` | `google-site-verification=5wsbUpxBdTHvdBGgiQL9s6MVMPxAT8URQkmYJ0xTRWU` | — |
   | TXT | `_dmarc` | `v=DMARC1; p=quarantine; rua=mailto:dmarc@digitalmate.io` | — |

   ⚠️ Also open GoDaddy's DNS page side by side and compare the full list. Anything you don't
   recognise, copy it across anyway — deleting a record you don't understand is how email and
   third-party verifications break. **Screenshot the GoDaddy DNS page before you change anything.**
3. Cloudflare gives you **two nameservers**, e.g. `xxx.ns.cloudflare.com`. Copy both.

---

## Step 5 — Point the nameservers at GoDaddy (5 minutes + up to 24h)

1. Sign in at GoDaddy → **My Products** → digitalmate.io → **DNS** → **Nameservers** → **Change**.
2. Choose **I'll use my own nameservers**.
3. Replace `ns19.domaincontrol.com` and `ns20.domaincontrol.com` with the two Cloudflare ones.
4. Save. GoDaddy will warn you that this moves DNS control — that's expected.
5. Cloudflare emails you when the domain is active. Usually under an hour, sometimes up to 24.

**While waiting, check email still works:** send a message to and from an @digitalmate.io address.
If mail breaks, the MX record didn't come across — fix it in Cloudflare's DNS tab immediately.

---

## Step 6 — Attach the domain to the site (5 minutes)

1. **Compute (Workers & Pages)** → `digitalmate` project → **Custom domains** → **Set up a custom
   domain**.
2. Enter `digitalmate.io` → Cloudflare adds the record itself → **Activate domain**.
3. Repeat for `www.digitalmate.io`.
4. Wait for the certificate — a few minutes, occasionally longer.
5. Open **https://digitalmate.io** in a private window. You should see the new site with a padlock.

---

## Step 7 — Final checks before telling the bank

- [ ] `https://digitalmate.io` shows the new site
- [ ] `https://www.digitalmate.io` works too
- [ ] The padlock is there and there is no certificate warning
- [ ] Phone and email on the page are **real**, and the email receives a test message
- [ ] Imprint, Privacy and Terms all open
- [ ] It reads well on a phone
- [ ] Ask me to **remove the `noindex` tags and robots.txt** — they're preview-only and would keep
      Google out permanently
- [ ] Send a mail from an @digitalmate.io address and confirm it arrives

Only then resubmit the URL in the bank's verification centre.

---

## Step 8 — Tidy up afterwards

- Cancel the **GoDaddy website builder** subscription — but keep the **domain** registration.
  Do this only after digitalmate.io has been serving the new site for a few days.
- Keep the GitHub repo as your backup copy of the files.
- Optional: redirect `digitalmate.pages.dev` to the real domain so only one address is public.

---

## If something goes wrong

**The site doesn't appear after the nameserver change** — DNS may still be propagating. Check
https://dnschecker.org for `digitalmate.io`.

**Email stops** — go to Cloudflare → DNS and confirm the MX record `smtp.google.com` priority 1 is
there. Add it if it's missing. Mail resumes within minutes.

**You want to undo everything** — set the GoDaddy nameservers back to `ns19.domaincontrol.com` and
`ns20.domaincontrol.com`. The old builder site returns. Nothing is destroyed at any point in this
runbook.
