from bs4 import BeautifulSoup

# The perfect red circle checkmark SVG matching the original design
CHECK_SVG = '''<svg viewBox="0 0 24 24" width="20" height="20" xmlns="http://www.w3.org/2000/svg">
  <circle cx="12" cy="12" r="12" fill="#c0392b"/>
  <path d="M5.5 12.5l4 4 9-9" stroke="#fff" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
</svg>'''

with open('roovon_clone/newkit.creativemox.com/roovon/index.html','r',encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(),'lxml')

count = 0
for icon_span in soup.find_all('span', class_='elementor-icon-list-icon'):
    i_tag = icon_span.find('i', class_=lambda c: c and 'mdi' in c)
    if i_tag:
        i_tag.replace_with(BeautifulSoup(CHECK_SVG, 'lxml').find('svg'))
        count += 1

with open('roovon_clone/newkit.creativemox.com/roovon/index.html','w',encoding='utf-8') as f:
    f.write(str(soup))

print(f'Replaced {count} broken checkmark icons with red SVG checkmarks!')
