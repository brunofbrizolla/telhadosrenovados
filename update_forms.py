import os
from glob import glob

WEB_APP_URL = "https://script.google.com/macros/s/AKfycbwh-oIofPUVh99nRIF7tBSchelbkounkRtY3x4AXnLmLYjKwDKmn--_DsaXJyKyFm9o/exec"

def update_forms_in_dir(directory):
    html_files = glob(os.path.join(directory, "**", "*.html"), recursive=True)
    count = 0
    for fpath in html_files:
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        c2 = content

        # Replace standard action
        if 'action="orcamento.php"' in c2:
            c2 = c2.replace('action="orcamento.php"', f'action="{WEB_APP_URL}"')
        
        # Replace HTMX form to use iframe approach
        if 'hx-post="orcamento.php"' in c2:
            # First, check if hidden_iframe is already injected
            if 'hidden_iframe' not in c2:
                # Add iframe right before form
                iframe_html = '''<script>var submitted=false;</script>
<iframe name="hidden_iframe" id="hidden_iframe" style="display:none;" onload="if(submitted) {document.getElementById('response').innerHTML='<div style=\\\'padding:15px; background-color:#d4edda; color:#155724; border-radius:5px; margin-top:15px;\\\'>✅ Pedido enviado com sucesso! Entraremos em contacto brevemente.</div>'; document.getElementById('contactForm').reset();}"></iframe>
<form action="URL" method="POST" target="hidden_iframe"'''
                
                # We need to replace <form ... hx-post="orcamento.php" ...> with the new iframe form approach
                # But notice the form opening bracket <form might be far. Let's just do a simple replace:
                c2 = c2.replace('<form hx-post="orcamento.php" hx-target="#response" hx-on::after-request="this.reset()" id="contactForm">',
                                iframe_html.replace('URL', WEB_APP_URL) + ' id="contactForm" onsubmit="submitted=true;">')
                
                # Alternative if it's slightly different:
                c2 = c2.replace('hx-post="orcamento.php"', f'action="{WEB_APP_URL}" target="hidden_iframe" method="POST" onsubmit="submitted=true;"')
                # clean up hx attributes just to be safe:
                c2 = c2.replace('hx-target="#response"', '')
                c2 = c2.replace('hx-on::after-request="this.reset()"', '')

        if c2 != content:
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(c2)
            count += 1
            print(f"Updated forms in {fpath}")

    print(f"Directory {directory}: Updated {count} files.")

update_forms_in_dir("C:\\Users\\Lenovo\\Downloads\\TELHADOS RENOVADOS\\telhaverde_clone")
update_forms_in_dir("C:\\Users\\Lenovo\\Downloads\\TELHADOS RENOVADOS\\roovon_clone")
