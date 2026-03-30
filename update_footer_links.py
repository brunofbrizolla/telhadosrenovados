import os, codecs, re

DEST_DIR = 'roovon_clone/newkit.creativemox.com/roovon'

for fname in os.listdir(DEST_DIR):
    if fname.endswith('.html'):
        fpath = os.path.join(DEST_DIR, fname)
        with codecs.open(fpath, 'r', 'utf-8') as file:
            content = file.read()
        
        c2 = content
        
        # Replace the hrefs specifically for the legal links
        c2 = re.sub(
            r'href="[^"]*"\s*(>[^<]*<span[^>]*>\s*Política de Privacidade\s*</span>)',
            r'href="politica-de-privacidade.html"\1',
            c2, flags=re.IGNORECASE
        )
        c2 = re.sub(
            r'href="[^"]*"\s*(>[^<]*<span[^>]*>\s*Termos e Condições\s*</span>)',
            r'href="termos-e-condicoes.html"\1',
            c2, flags=re.IGNORECASE
        )
        c2 = re.sub(
            r'href="[^"]*"\s*(>[^<]*<span[^>]*>\s*Política de Cookies\s*</span>)',
            r'href="politica-de-cookies.html"\1',
            c2, flags=re.IGNORECASE
        )
        c2 = re.sub(
            r'href="[^"]*"\s*(>[^<]*<span[^>]*>\s*Política de Garantia\s*</span>)',
            r'href="politica-de-garantia.html"\1',
            c2, flags=re.IGNORECASE
        )
        
        if c2 != content:
            with codecs.open(fpath, 'w', 'utf-8') as file:
                file.write(c2)
            print(f"Updated footer links in {fname}")
        else:
            # Check if it was already updated or not found
            if 'href="politica-de-privacidade.html"' in content:
                print(f"Already updated: {fname}")
            else:
                print(f"Links not found in: {fname}")
