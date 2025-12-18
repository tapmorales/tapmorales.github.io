#!/usr/bin/env python3
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SNIPPET = (
"<!-- Google tag (gtag.js) -->\n"
"<script async src=\"https://www.googletagmanager.com/gtag/js?id=G-LDDZBCF196\"></script>\n"
"<script>\n"
"  window.dataLayer = window.dataLayer || [];\n"
"  function gtag(){dataLayer.push(arguments);}\n"
"  gtag('js', new Date());\n\n"
"  gtag('config', 'G-LDDZBCF196');\n"
"</script>\n"
)

HEAD_RE = re.compile(r"(<head\b[^>]*>)", re.IGNORECASE)

updated = []
skipped = []
nohead = []

for dirpath, dirnames, filenames in os.walk(ROOT):
    for fname in filenames:
        if not fname.lower().endswith('.html'):
            continue
        path = os.path.join(dirpath, fname)
        try:
            with open(path, 'r', encoding='utf-8') as f:
                text = f.read()
        except Exception:
            try:
                with open(path, 'r', encoding='latin-1') as f:
                    text = f.read()
            except Exception:
                skipped.append(path)
                continue

        if 'G-LDDZBCF196' in text:
            skipped.append(path)
            continue

        m = HEAD_RE.search(text)
        if not m:
            nohead.append(path)
            continue

        insert_pos = m.end()
        new_text = text[:insert_pos] + "\n" + SNIPPET + text[insert_pos:]

        try:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(new_text)
            updated.append(path)
        except Exception:
            skipped.append(path)

print('Updated files:', len(updated))
for p in updated:
    print('  ', p)

print('\nSkipped (already had snippet):', len(skipped))
print('\nFiles without <head> found:', len(nohead))
for p in nohead[:20]:
    print('  ', p)

if nohead:
    print('\nNote: some files did not contain a <head> tag; they were left unchanged.')

# Exit code 0
