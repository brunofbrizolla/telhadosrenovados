import os, re, codecs
from glob import glob

DEST_DIR = 'roovon_clone/newkit.creativemox.com/roovon'

def clean_file(fpath):
    with codecs.open(fpath, 'r', 'utf-8') as f:
        content = f.read()

    c2 = content

    # 1. Remove <link> tags pointing to newkit.creativemox.com (css, rss, json, canonical, etc.)
    c2 = re.sub(
        r'<link\b[^>]*href="https?://newkit\.creativemox\.com[^"]*"[^>]*/?>',
        '',
        c2, flags=re.IGNORECASE
    )

    # 2. Remove external <script src="...newkit..."> blocks
    c2 = re.sub(
        r'<script\b[^>]+src="https?://newkit\.creativemox\.com[^"]*"[^>]*>\s*</script>',
        '',
        c2, flags=re.IGNORECASE
    )

    # 3. Remove the large elementorFrontendConfig inline script (references ajax.php)
    c2 = re.sub(
        r'var elementorFrontendConfig\s*=\s*\{.*?\};',
        'var elementorFrontendConfig = {};',
        c2, flags=re.DOTALL
    )

    # 4. Remove ElementorProFrontendConfig inline script
    c2 = re.sub(
        r'var ElementorProFrontendConfig\s*=\s*\{.*?\};',
        'var ElementorProFrontendConfig = {};',
        c2, flags=re.DOTALL
    )

    # 5. Remove speculationrules scripts
    c2 = re.sub(
        r'<script type="speculationrules">.*?</script>',
        '',
        c2, flags=re.DOTALL | re.IGNORECASE
    )

    # 6. Remove wp-emoji-loader inline scripts (the ones with sourceURL to newkit)
    c2 = re.sub(
        r'<script[^>]*>[\s\S]*?//# sourceURL=https://newkit\.creativemox\.com[^<]*</script>',
        '',
        c2, flags=re.IGNORECASE
    )

    # 7. Remove all remaining inline references to admin-ajax.php from newkit in JS strings
    c2 = re.sub(
        r'"ajaxurl"\s*:\s*"https?:\\\/\\\/newkit\.creativemox[^"]*"',
        '"ajaxurl": ""',
        c2, flags=re.IGNORECASE
    )

    # 8. Fix broken phone regex pattern: [0-9()#&+*-=.]+ -> [0-9()#&+*=.-]+
    c2 = c2.replace('pattern="[0-9()#&amp;+*-=.]+"', 'pattern="[0-9()#&amp;+*=.-]+"')
    c2 = c2.replace("pattern=\"[0-9()#&+*-=.]+\"", "pattern=\"[0-9()#&+*=.-]+\"")

    # 9. Remove ekit inline script block (elementskit scripts that reference newkit)
    c2 = re.sub(
        r'<script[^>]*id="ekit[^"]*"[^>]*>.*?</script>',
        '',
        c2, flags=re.DOTALL | re.IGNORECASE
    )

    if c2 != content:
        with codecs.open(fpath, 'w', 'utf-8') as f:
            f.write(c2)
        return True
    return False

html_files = glob(os.path.join(DEST_DIR, '*.html'))
updated = 0
for fpath in sorted(html_files):
    if clean_file(fpath):
        print(f"OK Cleaned: {os.path.basename(fpath)}")
        updated += 1
    else:
        print(f"  No changes: {os.path.basename(fpath)}")

print(f"\nDone! {updated}/{len(html_files)} files updated.")
