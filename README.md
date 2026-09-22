# digitalmate.io — where everything lives

Everything for the website is in this one folder: `d:\Downloads\digitalmate-site\`

## The website itself — edit these
| File | What it is |
|---|---|
| `index.html` | home: hero, services, pricing, how it works, company details, CTA with photo, contact |
| `imprint.html` | legal information |
| `privacy.html` | privacy policy |
| `terms.html` | terms of service |
| `styles.css` | all styling for every page |
| `images/valerian-gegidze.jpg` | photo used in the CTA band |
| `robots.txt` | **preview only** — blocks search engines. Delete before going live |

Open `index.html` in a browser to see the site; it works straight from disk, no server needed.

## The upload file
`digitalmate-site-upload.zip` — this is what you drag into Cloudflare Pages. It holds only the seven
files above, nothing else.

**It is rebuilt every time a change is made**, so it always matches the loose files next to it.
If in doubt, check the timestamps: the zip should be as new as the newest `.html`.

## Notes and instructions — not part of the website
| File | What it is |
|---|---|
| `README.md` | this file |
| `GO_LIVE_RUNBOOK.md` | step by step: Cloudflare account → upload → domain → bank |
| `DEPLOY_AND_NOTES.md` | why the site is built this way, what still needs real content |

These stay out of the zip, so they are never published.

## Current contact details on the site
- `Hi@digitalmate.io` — company address, on every page
- `v.gegidze@gmail.com` — in the CTA band and next to the company address
- `+995 599 525 282` — phone, on every page

## Backup
Everything is also in a private GitHub repo: **github.com/KateTchWork/digitalmate-site**
(account KateTchWork). Every change is committed there, so you can go back to any earlier version.

## To request a change
Say what should change and I will edit the files here, rebuild the zip and push to GitHub. You then
re-upload the zip in Cloudflare Pages → Create deployment.

## Before going live — do not forget
1. Remove the `noindex` line from all four HTML pages and delete `robots.txt`,
   otherwise Google will never list the site.
2. Confirm `Hi@digitalmate.io` actually receives mail.
3. Review the content I wrote myself — the "How it works" steps, office hours, and the whole of the
   privacy and terms pages. The list is in `DEPLOY_AND_NOTES.md`.
