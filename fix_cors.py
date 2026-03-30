import os, re, codecs
from glob import glob

DEST_DIR = 'roovon_clone/newkit.creativemox.com/roovon'

def clean_file(fpath):
    with codecs.open(fpath, 'r', 'utf-8') as f:
        content = f.read()

    c2 = content

    # 1. Remove external <link rel="stylesheet"> from newkit.creativemox.com / skyboot / elementskit
    c2 = re.sub(
        r'<link[^>]+href="https?://(newkit\.creativemox\.com|fonts\.gstatic\.com)[^"]*"[^>]*/?>',
        '',
        c2, flags=re.IGNORECASE
    )

    # 2. Remove external <script src="...newkit...">...</script>
    c2 = re.sub(
        r'<script[^>]+src="https?://newkit\.creativemox\.com[^"]*"[^>]*>\s*</script>',
        '',
        c2, flags=re.IGNORECASE
    )

    # 3. Remove speculationrules <script> that points to /roovon/* paths (internal WP speculation)
    c2 = re.sub(
        r'<script type="speculationrules">.*?</script>',
        '',
        c2, flags=re.DOTALL | re.IGNORECASE
    )

    # 4. Remove WordPress admin-ajax XHR calls embedded in inline scripts
    c2 = re.sub(
        r'ajaxurl\s*[=:]\s*["\']https?://[^"\']+admin-ajax\.php["\']',
        "ajaxurl: ''",
        c2, flags=re.IGNORECASE
    )
    c2 = re.sub(
        r'["\'](https?://newkit\.creativemox\.com[^"\']*)["\']',
        "''",
        c2, flags=re.IGNORECASE
    )

    # 5. Fix broken phone pattern attribute that causes SyntaxError
    # pattern="[0-9()#&+*-=.]+" has an invalid - between * and =
    c2 = c2.replace(
        'pattern="[0-9()#&amp;+*-=.]+"',
        'pattern="[0-9()#&amp;+*=.-]+"'
    )
    c2 = c2.replace(
        "pattern=\"[0-9()#&+*-=.]+\"",
        "pattern=\"[0-9()#&+*=.-]+\""
    )

    # 6. Remove canonical and other WP link tags pointing to newkit
    c2 = re.sub(
        r'<link[^>]+(?:href|content)="https?://newkit\.creativemox\.com[^"]*"[^>]*/?>',
        '',
        c2, flags=re.IGNORECASE
    )

    if c2 != content:
        with codecs.open(fpath, 'w', 'utf-8') as f:
            f.write(c2)
        return True
    return False

html_files = glob(os.path.join(DEST_DIR, '*.html'))
updated = 0
for fpath in html_files:
    if clean_file(fpath):
        print(f"Cleaned: {os.path.basename(fpath)}")
        updated += 1
    else:
        print(f"No changes: {os.path.basename(fpath)}")

print(f"\nDone! {updated}/{len(html_files)} files cleaned.")
