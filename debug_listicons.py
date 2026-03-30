from bs4 import BeautifulSoup

with open('roovon_clone/newkit.creativemox.com/roovon/index.html','r',encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(),'lxml')

icons = soup.find_all('span', class_='elementor-icon-list-icon')
print(f'Found {len(icons)} list icons')
if icons:
    print('Sample:', str(icons[0])[:300])
