import os, shutil, re

SRC = 'telhaverde_clone/telhaverde.pt/img'
DEST = 'roovon_clone/newkit.creativemox.com/roovon'

# Copy all relevant roofing images to the roovon folder
copies = {
    'colocarTelhas.webp':         'img-instalacao.webp',
    'telhado-novo.jpeg':           'img-remodelacao.jpeg',
    'telhado-em-repa.jpeg':        'img-reparacao.jpeg',    # wait check name
    'manutencao-telhados-2.jpeg': 'img-impermeabilizacao.jpeg',
    'limpeza-de-telhados.jpeg':   'img-limpeza.jpeg',
    'roof-vertical.webp':         'img-impermeabilizacao2.webp',
    'rop3-2.webp':                'img-impermeabilizacao3.webp',
    'telhados-reparar.webp':      'img-reparacao.webp',
    'telhado-sandwich.jpeg':      'img-sandwich.jpeg',
}

copied = []
for src_name, dest_name in copies.items():
    src_path = os.path.join(SRC, src_name)
    if os.path.exists(src_path):
        shutil.copy2(src_path, os.path.join(DEST, dest_name))
        copied.append((src_name, dest_name))
        print(f'OK: {src_name} -> {dest_name}')
    else:
        print(f'NOT FOUND: {src_name}')

# Also list what's actually in the img folder to pick the right ones
print('\nAll available images:')
for f in sorted(os.listdir(SRC)):
    if f.lower().endswith(('.jpg','.jpeg','.png','.webp')):
        print(' ', f)
