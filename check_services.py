from bs4 import BeautifulSoup

with open('roovon_clone/newkit.creativemox.com/roovon/index.html','r',encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(),'lxml')

# Find service card titles
print("=== elementor-icon-box-title ===")
titles = soup.find_all(class_='elementor-icon-box-title')
for t in titles:
    print(' -', t.get_text(strip=True))

# Also find h3s inside icon box wrappers
print("\n=== elementor-icon-box wrappers h3/h4 ===")
boxes = soup.find_all(class_='elementor-icon-box-wrapper')
for b in boxes:
    heading = b.find(['h2','h3','h4','h5'])
    link = b.find('a', class_='elementor-button')
    if heading:
        print(f"  Title: {heading.get_text(strip=True)}")
    if link:
        print(f"  Link href: {link.get('href','#')}")
