from bs4 import BeautifulSoup

# Mapping: title keyword -> page file
SERVICE_MAP = {
    'Instalação de Telhados': 'instalacao-telhados.html',
    'Remodelação de Telhados': 'remodelacao-telhados.html',
    'Reparação de Telhados': 'reparacao-telhados.html',
    'Inspeção e Orçamentação': 'inspecao-orcamentacao.html',
    'Limpeza e Manutenção': 'limpeza-telhados.html',
    'Sistemas de Impermeabilização': 'sistemas-impermeabilizacao.html',
}

with open('roovon_clone/newkit.creativemox.com/roovon/index.html','r',encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(),'lxml')

# Strategy: find each elementor-widget-button containing "Saiba Mais".
# Then look BACKWARDS in the DOM for the nearest icon-box title to know which service it belongs to.
# We'll do this by finding the parent container (e-con or elementor-column) and searching within it.

fixed = 0

# Find all containers that seem to be service cards (have both an icon-box-title AND a button)
# They share the same parent e-con / column
all_buttons = soup.find_all('span', class_='elementor-button-text')

for span in all_buttons:
    if 'Saiba Mais' not in span.get_text():
        continue
    
    # Walk up to find a container that also has an icon-box-title
    parent = span.parent
    for _ in range(12):  # walk up max 12 levels
        if parent is None:
            break
        title_el = parent.find(class_='elementor-icon-box-title')
        if title_el:
            title_text = title_el.get_text(strip=True)
            # Match to service page
            for keyword, page in SERVICE_MAP.items():
                if keyword.lower() in title_text.lower():
                    # Update the href of the parent <a>
                    a_tag = span.find_parent('a')
                    if a_tag:
                        old = a_tag.get('href','#')
                        a_tag['href'] = page
                        print(f'FIXED: "{title_text[:40]}" -> {page}  (was: {old})')
                        fixed += 1
                    break
            break
        parent = parent.parent

with open('roovon_clone/newkit.creativemox.com/roovon/index.html','w',encoding='utf-8') as f:
    f.write(str(soup))

print(f'\nTotal fixed: {fixed} buttons')
