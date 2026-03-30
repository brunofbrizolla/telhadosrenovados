import shutil, os, re
from bs4 import BeautifulSoup

SRC_IMG = 'telhaverde_clone/telhaverde.pt/img'
DEST = 'roovon_clone/newkit.creativemox.com/roovon'

# ---- 1. Copy images ----
img_map = {
    'colocarTelhas.webp':          'img-instalacao.webp',
    'telhado-novo.jpeg':           'img-remodelacao.jpeg',
    'telhado-em-repa.jpeg':        'img-reparacao.jpeg',
    'manutencao-telhados-2.jpeg':  'img-manutencao.jpeg',
    'limpeza-de-telhados.jpeg':    'img-limpeza.jpeg',
    'telhados-reparar.webp':       'img-inspecao.webp',
    'pexels-photo-5273346-1920w.webp': 'img-impermeabilizacao.webp',
    'roof-vertical.webp':          'img-hero-services.webp',
}
for src, dst in img_map.items():
    sp = os.path.join(SRC_IMG, src)
    if os.path.exists(sp):
        shutil.copy2(sp, os.path.join(DEST, dst))
        print(f'Copied: {src} -> {dst}')

# ---- 2. The 6 real services (from the homepage section) ----
SERVICES = [
    {
        'name': 'Instalação de Telhados e Coberturas',
        'page': 'instalacao-telhados.html',
        'img':  'img-instalacao.webp',
    },
    {
        'name': 'Remodelação de Telhados',
        'page': 'remodelacao-telhados.html',
        'img':  'img-remodelacao.jpeg',
    },
    {
        'name': 'Reparação de Telhados',
        'page': 'reparacao-telhados.html',
        'img':  'img-reparacao.jpeg',
    },
    {
        'name': 'Inspeção e Orçamentação',
        'page': 'inspecao-orcamentacao.html',
        'img':  'img-inspecao.webp',
    },
    {
        'name': 'Limpeza e Manutenção',
        'page': 'limpeza-telhados.html',
        'img':  'img-limpeza.jpeg',
    },
    {
        'name': 'Sistemas de Impermeabilização',
        'page': 'sistemas-impermeabilizacao.html',
        'img':  'img-impermeabilizacao.webp',
    },
]

# ---- 3. Build the new dropdown HTML ----
dropdown_items = ''
for s in SERVICES:
    dropdown_items += f'<li><a href="{s["page"]}">{s["name"]}</a></li>\n'

# ---- 4. Update index.html: nav dropdown + service card Saiba Mais links ----
with open(os.path.join(DEST,'index.html'), 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'lxml')

# Update the nav dropdown
dropdown = soup.select_one('.crh-dropdown')
if dropdown:
    dropdown.clear()
    for s in SERVICES:
        li = soup.new_tag('li')
        a = soup.new_tag('a', href=s['page'])
        a.string = s['name']
        li.append(a)
        dropdown.append(li)
    print('Nav dropdown updated in index.html')

# Update Saiba Mais button hrefs by order
btn_spans = soup.find_all('span', class_='elementor-button-text')
service_idx = 0
for span in btn_spans:
    txt = span.get_text(strip=True)
    if 'Saiba Mais' in txt and service_idx < len(SERVICES):
        a = span.find_parent('a')
        if a:
            a['href'] = SERVICES[service_idx]['page']
            service_idx += 1

with open(os.path.join(DEST,'index.html'), 'w', encoding='utf-8') as f:
    f.write(str(soup))
print(f'Updated {service_idx} Saiba Mais links in index.html')

# ---- 5. Update images in all service pages ----
page_img = {
    'instalacao-telhados.html':         'img-instalacao.webp',
    'remodelacao-telhados.html':        'img-remodelacao.jpeg',
    'reparacao-telhados.html':          'img-reparacao.jpeg',
    'inspecao-orcamentacao.html':       'img-inspecao.webp',
    'limpeza-telhados.html':            'img-limpeza.jpeg',
    'sistemas-impermeabilizacao.html':  'img-impermeabilizacao.webp',
}

for page, img in page_img.items():
    fpath = os.path.join(DEST, page)
    if not os.path.exists(fpath):
        print(f'SKIP (no file): {page}')
        continue
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    # Replace any unsplash URLs
    updated = re.sub(r'https://images\.unsplash\.com/[^"\'>\s]+', img, content)
    # Also replace old placeholder local images
    updated = re.sub(r'img-caleiras\.\w+', img, updated)
    updated = re.sub(r'img-impermeabilizacao\d*\.\w+', img, updated)
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(updated)
    print(f'Images updated: {page} -> {img}')

# ---- 6. Update nav dropdown in ALL service pages ----
new_nav_ul = f'''<ul class="crh-dropdown">
{dropdown_items}</ul>'''

service_files = [
    'instalacao-telhados.html','remodelacao-telhados.html','reparacao-telhados.html',
    'inspecao-orcamentacao.html','limpeza-telhados.html','sistemas-impermeabilizacao.html',
    'caleiras-rufagem.html',
]
for page in service_files:
    fpath = os.path.join(DEST, page)
    if not os.path.exists(fpath):
        continue
    with open(fpath,'r',encoding='utf-8') as f:
        c = f.read()
    # Replace the crh-dropdown ul
    c = re.sub(r'<ul class="crh-dropdown">.*?</ul>', new_nav_ul, c, flags=re.DOTALL)
    with open(fpath,'w',encoding='utf-8') as f:
        f.write(c)
    print(f'Nav updated: {page}')

print('\nAll done!')
