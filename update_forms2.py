import os, re
from glob import glob

WEB_APP_URL = "https://script.google.com/macros/s/AKfycbzHoD7XIEEaQQvsG2r66O2gMGOotON0zt8l_ZpuksC997OjfFDXxHrc-s8SAYGtqZ7U/exec"

IFRAME = f'''<script>var submitted=false;</script>
<iframe name="hidden_iframe" id="hidden_iframe" style="display:none;" onload="if(submitted) {{document.getElementById('response').innerHTML='<div style=\\'padding:15px; background-color:#d4edda; color:#155724; border-radius:5px; margin-top:15px;\\'>✅ Pedido de Orçamento processado com sucesso! Entraremos em contacto brevemente.</div>'; var cf = document.getElementById('contactForm'); if(cf) cf.reset();}}"></iframe>
'''

def fix_forms(directory):
    html_files = glob(os.path.join(directory, "**", "*.html"), recursive=True)
    count = 0
    for fpath in html_files:
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        c2 = content

        # Telha Verde style: hx-post="orcamento.php"
        if '"orcamento.php"' in c2 or '"hidden_iframe"' in c2:
            # Let's clean up previous broken modifications if any
            c2 = re.sub(r'action="[^"]*script\.google\.com[^"]*" target="hidden_iframe" method="POST" onsubmit="submitted=true;"', 'hx-post="orcamento.php"', c2)
            c2 = re.sub(r'action="[^"]*script\.google\.com[^"]*"', 'hx-post="orcamento.php"', c2)
            
            # Now properly inject iframe before the form
            if '<form ' in c2 and 'hidden_iframe' not in c2:
                # Find the form with hx-post
                match = re.search(r'<form[^>]*hx-post="orcamento\.php"[^>]*>', c2)
                if match:
                    original_form = match.group(0)
                    # Create new form tag
                    new_form = re.sub(r'hx-post="orcamento\.php"', f'action="{WEB_APP_URL}" target="hidden_iframe" method="POST" onsubmit="submitted=true;"', original_form)
                    # Clean hx-target and hx-on
                    new_form = re.sub(r'hx-target="[^"]*"', '', new_form)
                    new_form = re.sub(r'hx-on[^=]*="[^"]*"', '', new_form)
                    
                    c2 = c2.replace(original_form, IFRAME + new_form)

        # Roovon style: elementor-form
        if 'class="elementor-form"' in c2 and 'method="post"' in c2:
            if 'hidden_iframe' not in c2:
                match = re.search(r'<form[^>]*class="elementor-form"[^>]*>', c2)
                if match:
                    original_form = match.group(0)
                    new_form = original_form
                    # replace action if it exists, or add it
                    if 'action=' in new_form:
                        new_form = re.sub(r'action="[^"]*"', f'action="{WEB_APP_URL}"', new_form)
                    else:
                        new_form = new_form.replace('<form ', f'<form action="{WEB_APP_URL}" target="hidden_iframe" onsubmit="submitted=true;" ')
                    
                    c2 = c2.replace(original_form, IFRAME + new_form)
                    # also, we need to add id="response" near the bottom of the form to show the success message
                    if 'id="response"' not in c2:
                        c2 = c2.replace('</form>', '<div id="response"></div>\n</form>')
                        
                    # give the form an ID if it doesn't have one so reset() works
                    if 'id="contactForm"' not in new_form and 'id=' not in new_form:
                        c2 = c2.replace(new_form, new_form.replace('<form ', '<form id="contactForm" '))
                        
        if c2 != content:
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(c2)
            count += 1
            print(f"Fixed: {fpath}")

    print(f"{directory} - Updated: {count}")

fix_forms("C:\\Users\\Lenovo\\Downloads\\TELHADOS RENOVADOS\\telhaverde_clone")
fix_forms("C:\\Users\\Lenovo\\Downloads\\TELHADOS RENOVADOS\\roovon_clone")
