# digitalmate.io — where everything lives

Everything is in `d:\Downloads\digitalmate-site\`, split into two kinds of thing: the website itself,
and notes about it.

```
digitalmate-site\
├─ website\                      ← THE WEBSITE. Only these files get published
│  ├─ index.html                 home: hero, services, pricing, how it works,
│  │                             company details, CTA with photo, contact
│  ├─ imprint.html               legal information
│  ├─ privacy.html               privacy policy
│  ├─ terms.html                 terms of service
│  ├─ styles.css                 all styling for every page
│  ├─ robots.txt                 PREVIEW ONLY — blocks search engines, delete before go-live
│  └─ images\
│     └─ valerian-gegidze.jpg    photo in the CTA band
│
├─ digitalmate-site-upload.zip   ← what you drag into Cloudflare Pages
├─ build_zip.py                  rebuilds that zip from website\
├─ README.md                     this file
├─ GO_LIVE_RUNBOOK.md            step by step: Cloudflare → domain → bank
└─ DEPLOY_AND_NOTES.md           why it is built this way + what still needs real content
```

To preview the site, open `website\index.html` in a browser. It works straight from disk.

## The upload zip
`digitalmate-site-upload.zip` contains **only** what is inside `website\`, with `index.html` at the
top level — the shape Cloudflare Pages expects. The notes never go up.

It is rebuilt after every change, so it always matches. To check, compare its timestamp with the
newest file in `website\`.

## Current contact details on the site
- `Hi@digitalmate.io` — company address, every page
- `v.gegidze@gmail.com` — CTA band and beside the company address
- `+995 599 525 282` — phone, every page

## Backup
Private GitHub repo: **github.com/KateTchWork/digitalmate-site** (account KateTchWork).
Every change is committed, so any earlier version can be restored.

## To request a change
Tell me what should change. I edit the files in `website\`, rebuild the zip, and push to GitHub.
You then re-upload the zip: Cloudflare Pages → your project → Create deployment.

## Before going live — do not forget
1. Remove the `noindex` line from all four HTML pages and delete `robots.txt`, or Google will never
   list the site.
2. Confirm `Hi@digitalmate.io` actually receives mail.
3. Review the content I wrote myself — the "How it works" steps, the office hours, and the whole of
   the privacy and terms pages. The full list is in `DEPLOY_AND_NOTES.md`.
