import json
from bs4 import BeautifulSoup

def extract_texts():
    with open('roovon_clone/newkit.creativemox.com/roovon/index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    soup = BeautifulSoup(html, 'lxml')
    
    # Elements to avoid extracting from (like the custom header we did)
    # We'll just target typical Elementor textual elements
    texts = set()
    
    # Exclude our custom header
    header = soup.find(id='custom-roovon-header')
    if header:
        header.decompose()
        
    for tag in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'span', 'a', 'div', 'button']):
        # If it has direct text 
        if tag.string:
            clean_text = tag.string.strip()
            if len(clean_text) > 3 and clean_text.replace('\n','').strip():
                # Avoid single numbers or short random words unless they look like actual phrases
                if not clean_text.isdigit():
                    texts.add(clean_text)
        else:
            # Maybe it has strings inside
            for text in tag.strings:
                clean_text = text.strip()
                if len(clean_text) > 3 and not clean_text.isdigit():
                    texts.add(clean_text)

    # Filter out empty or pure whitespace
    valid_texts = [t for t in texts if t and len(t) > 3]
    
    # Sort by length descending, so longest phrases replace first when we do the inject phase
    valid_texts.sort(key=len, reverse=True)

    with open('en_texts.json', 'w', encoding='utf-8') as f:
        json.dump(valid_texts, f, indent=4, ensure_ascii=False)

if __name__ == '__main__':
    extract_texts()
    print("Extraction complete. Generated en_texts.json")
