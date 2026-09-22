# digitalmate.io — new site, deploy notes (2026-09-22)

Files in this folder are the complete website. No build step, no dependencies.

```
index.html      home: services, pricing, how it works, company details, contact
imprint.html    legal information (replaces the current /imprint)
privacy.html    privacy policy
terms.html      terms of service
styles.css      all styling
```

Open `index.html` in a browser to preview it locally — it works straight from disk.

---

## ⚠️ Fill these in before publishing

Two placeholders appear in every file. Search and replace both:

| Placeholder | Replace with |
|---|---|
| `+374 00 000000` (and `+37400000000` in the `tel:` links) | the real company phone number |
| `hello@digitalmate.io` | the real mailbox on the domain, once it exists |

**The phone number matters most.** The bank asked for a page showing at least two of: name, company
name, phone, email, address, photo. With a phone number and a domain email in place, the home page
shows **six of the six** — company name, director's full name, address, phone, email and the
registration IDs.

Until the domain mailbox exists you can leave the Gmail address in, but expect it to weaken the
review: a company site with a personal Gmail is exactly what reviewers flag.

---

## Why the old site was failing

The live site shows the company name and `v.gegidze@gmail.com`, nothing else. The full details sit
on `/imprint`, which a reviewer may never open. The new home page carries everything in one view,
in a "Company details" block, and repeats it in the footer of every page.

Also added, because bank and payment reviewers look for them: published pricing, a clear description
of the services, an imprint, a privacy policy and terms of service.

---

## Publishing on Cloudflare Pages (free)

1. Sign in at **dash.cloudflare.com** → **Workers & Pages** → **Create** → **Pages** →
   **Upload assets**.
2. Name the project `digitalmate`.
3. Drag the whole folder in, or zip its contents and upload the zip. Deploy.
4. You get a URL like `digitalmate.pages.dev`. Check it works.

### Pointing digitalmate.io at it
In the Pages project → **Custom domains** → **Set up a custom domain** → enter `digitalmate.io`.
Cloudflare then tells you one of two things:

- **Move the nameservers** (Cloudflare's preference). You'd add the domain to Cloudflare, copy the
  two nameservers it gives you, and set them in GoDaddy under the domain's DNS settings. ⚠️ Before
  doing this, copy every existing DNS record — especially **MX records for email** — and recreate
  them in Cloudflare, or email on the domain stops.
- **Or add a CNAME** at GoDaddy pointing `www` to `digitalmate.pages.dev`, plus the records
  Cloudflare shows for the root domain. Slower to propagate but leaves your DNS where it is.

Either way HTTPS is issued automatically and free. Both are reversible.

### Updating later
Re-upload the folder in the Pages dashboard, or connect it to a GitHub repo and it redeploys on
every commit. Either way it costs nothing.

---

## What to do about the GoDaddy builder site

Leave it live until the new one is on the domain, then switch the DNS. Don't cancel the domain
itself — only the website builder product, and only after the new site answers on digitalmate.io.

---

## Content still worth adding (in review order of usefulness)

1. **A photo** — the office, or the director. The bank's list includes "your picture", and a real
   photograph makes a site look operated rather than generated.
2. **Two or three client references**, even by first name and country.
3. **A team page** with two or three real people.
4. **A logo** — text is fine for now, but a mark helps.

Send me any of these and I'll add them.
