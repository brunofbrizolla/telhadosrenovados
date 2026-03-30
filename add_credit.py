import os, re

DEST = 'roovon_clone/newkit.creativemox.com/roovon'
credit = ' &nbsp;|&nbsp; Desenvolvido por <a href="https://foturemkt.com/" target="_blank" rel="noopener" style="color:rgba(255,255,255,0.5);text-decoration:none;font-weight:600;">Foture MKt</a>'

pages = [f for f in os.listdir(DEST) if f.endswith('.html')]
count = 0
for page in pages:
    fpath = os.path.join(DEST, page)
    with open(fpath, 'r', encoding='utf-8') as f:
        html = f.read()
    if 'Foture' in html:
        print(f'Already has credit: {page}')
        continue
    # Match the copyright line and append credit before </p>
    updated = re.sub(
        r'(Copyright (?:&copy;|©) 2026 Telhados Renovados[^<]*)(</p>)',
        r'\1' + credit + r'\2',
        html
    )
    if updated != html:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(updated)
        count += 1
        print(f'Updated: {page}')
    else:
        print(f'Pattern not found: {page}')

print(f'\nDone! {count} pages updated.')
