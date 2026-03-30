from bs4 import BeautifulSoup

with open('roovon_clone/newkit.creativemox.com/roovon/index.html','r',encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(),'lxml')

# Find each icon-box widget, get its title and its Saiba Mais link href
widgets = soup.find_all(class_='elementor-widget-icon-box')
print(f'Found {len(widgets)} icon-box widgets\n')
for w in widgets:
    title_el = w.find(class_='elementor-icon-box-title')
    btn = w.find('a')  # first link in the widget
    saiba_mais_links = [a for a in w.find_all('a') if 'Saiba' in a.get_text() or 'Ligar' in a.get_text() or 'Mais' in a.get_text()]
    title = title_el.get_text(strip=True) if title_el else 'NO TITLE'
    for sl in saiba_mais_links:
        print(f'  Title: {title}')
        print(f'  Link text: {sl.get_text(strip=True)}')
        print(f'  href: {sl.get("href","#")}')
        print()
