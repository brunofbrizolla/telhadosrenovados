import os, re

# The local server serves telhaverde_clone at port 3000 and roovon at port 3001
# Since the roovon pages need the images, we copy them to the roovon folder
# and use relative paths

import shutil

SRC_DIR = 'telhaverde_clone/telhaverde.pt'
DEST_DIR = 'roovon_clone/newkit.creativemox.com/roovon'

# Mapping: image file in telhaverde -> copy name used in roovon service pages
image_map = {
    # (source file, destination copy name)
    'colocarTelhas.webp': 'img-instalacao.webp',
    'substituicao_telhas.jpeg': 'img-remodelacao.jpeg',
    'telhado-em-repa.jpeg': 'img-reparacao.jpeg',
    'pexels-photo-5273346-1920w.webp': 'img-impermeabilizacao.webp',
    'limpeza-de-telhados.jpeg': 'img-limpeza.jpeg',
    'telhas-zinco.webp': 'img-caleiras.webp',
}

# Also find the actual filename (it might be truncated in the list)
all_files = os.listdir(SRC_DIR)
print("Copying images...")
for src_name, dest_name in image_map.items():
    # Try exact match first
    if src_name in all_files:
        src_path = os.path.join(SRC_DIR, src_name)
    else:
        # Try partial match
        matches = [f for f in all_files if f.startswith(src_name[:15])]
        if matches:
            src_path = os.path.join(SRC_DIR, matches[0])
            src_name = matches[0]
        else:
            print(f"  NOT FOUND: {src_name}")
            continue
    
    dest_path = os.path.join(DEST_DIR, dest_name)
    shutil.copy2(src_path, dest_path)
    print(f"  Copied: {src_name} -> {dest_name}")

# Now update the service pages to use the local images
page_image_map = {
    'instalacao-telhados.html': 'img-instalacao.webp',
    'remodelacao-telhados.html': 'img-remodelacao.jpeg',
    'reparacao-telhados.html': 'img-reparacao.jpeg',
    'sistemas-impermeabilizacao.html': 'img-impermeabilizacao.webp',
    'limpeza-telhados.html': 'img-limpeza.jpeg',
    'caleiras-rufagem.html': 'img-caleiras.webp',
}

print("\nUpdating HTML files...")
for page, img in page_image_map.items():
    filepath = os.path.join(DEST_DIR, page)
    if not os.path.exists(filepath):
        print(f"  SKIP (not found): {page}")
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Replace all unsplash.com URLs with the local image
    updated = re.sub(r'https://images\.unsplash\.com/[^"\']+', img, html)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(updated)
    print(f"  Updated: {page} -> {img}")

print("\nDone! All service pages now use local images from telhaverde.")
