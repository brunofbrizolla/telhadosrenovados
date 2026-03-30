import json, re
from bs4 import BeautifulSoup

with open('roovon_clone/newkit.creativemox.com/roovon/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'lxml')

# Find ALL elements with icon in class
icon_elements = []
for el in soup.find_all(True):
    classes = ' '.join(el.get('class', []))
    tag = el.name
    if 'icon' in classes.lower():
        icon_elements.append(f"{tag}: {classes[:100]}")

# Deduplicate
unique = list(set(icon_elements))
for line in sorted(unique)[:40]:
    print(line)
