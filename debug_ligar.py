import re, sys

with open('roovon_clone/newkit.creativemox.com/roovon/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

positions = [m.start() for m in re.finditer('Ligar Agora', html)]
print(f'Found {len(positions)} occurrences')
for p in positions[:3]:
    print('---')
    print(repr(html[max(0,p-100):p+150]))
