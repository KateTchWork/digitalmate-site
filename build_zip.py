"""Rebuild the Cloudflare upload zip from d:\\Downloads\\digitalmate-site\\website.

The zip's root is the CONTENTS of website/, so index.html sits at the top level —
which is what Cloudflare Pages expects.
"""
import zipfile, os

SITE = r"D:\Downloads\digitalmate-site\website"
OUT  = r"D:\Downloads\digitalmate-site\digitalmate-site-upload.zip"

added = []
with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as z:
    for folder, dirs, files in os.walk(SITE):
        dirs[:] = [d for d in dirs if d not in (".git", "__pycache__")]
        for f in files:
            full = os.path.join(folder, f)
            rel = os.path.relpath(full, SITE).replace("\\", "/")
            z.write(full, rel)
            added.append(rel)

print("built:", OUT, round(os.path.getsize(OUT) / 1024, 1), "KB")
for a in sorted(added):
    print("  ", a)
