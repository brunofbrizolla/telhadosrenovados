from bs4 import BeautifulSoup

service_pages = [
    'instalacao-telhados.html',
    'remodelacao-telhados.html', 
    'reparacao-telhados.html',
    'sistemas-impermeabilizacao.html',
    'limpeza-telhados.html',
    'inspecao-gratuita.html',
]

with open('roovon_clone/newkit.creativemox.com/roovon/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'lxml')

# Find all spans with class "elementor-button-text" containing "Ligar Agora"
btn_spans = soup.find_all('span', class_='elementor-button-text')

service_idx = 0
changed = 0
for span in btn_spans:
    if span.string and 'Ligar Agora' in span.string:
        span.string = 'Saiba Mais'
        # Also update the parent <a> href to the corresponding service page
        parent_a = span.find_parent('a')
        if parent_a and service_idx < len(service_pages):
            parent_a['href'] = service_pages[service_idx]
            service_idx += 1
        changed += 1

with open('roovon_clone/newkit.creativemox.com/roovon/index.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print(f'Changed {changed} buttons to "Saiba Mais" with correct service links!')
