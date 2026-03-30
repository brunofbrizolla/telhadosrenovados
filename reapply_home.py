import re

with open("roovon_clone/newkit.creativemox.com/roovon/index.html", "r", encoding="utf-8") as f:
    html = f.read()

with open("roovon_clone/newkit.creativemox.com/roovon/instalacao-telhados.html", "r", encoding="utf-8") as f:
    ref_html = f.read()

print("Extracting components from instalacao-telhados...")
# Extract custom header CSS
header_css_match = re.search(r'/\* ===== HEADER ===== \*/.*?/\* ===== HERO ===== \*/', ref_html, re.DOTALL)
hamburger_css_match = re.search(r'/\* ===== MOBILE HAMBURGER ===== \*/.*?/\* ===== RESPONSIVE ===== \*/', ref_html, re.DOTALL)
responsive_css_match = re.search(r'@media \(max-width: 900px\).*?@media \(min-width: 901px\) \{ #mobile-wa-fab \{ display: none; \} \}', ref_html, re.DOTALL)
wa_fab_css_match = re.search(r'/\* Floating WA button on mobile \*/.*?</style>', ref_html, re.DOTALL)
footer_css_match = re.search(r'/\* ===== FOOTER ===== \*/.*?/\* ===== MOBILE HAMBURGER ===== \*/', ref_html, re.DOTALL)

# Default to empty if not found perfectly, though we know it's there
header_css = header_css_match.group(0) if header_css_match else ""
hamburger_css = hamburger_css_match.group(0) if hamburger_css_match else ""
responsive_css = responsive_css_match.group(0) if responsive_css_match else ""
wa_fab_css = wa_fab_css_match.group(0).replace('</style>', '') if wa_fab_css_match else ""
footer_css = footer_css_match.group(0) if footer_css_match else ""

# Extract HTML blocks
header_html_match = re.search(r'<!-- HEADER -->.*?<!-- HERO -->', ref_html, re.DOTALL)
footer_html_match = re.search(r'<!-- FOOTER -->.*?<!-- Floating WA -->', ref_html, re.DOTALL)
fab_html_match = re.search(r'<!-- Floating WA -->.*?<script>', ref_html, re.DOTALL)
script_match = re.search(r'<script>\n\(function\(\) \{\n    var header = document\.getElementById.*?\n</script>', ref_html, re.DOTALL)

header_html = header_html_match.group(0).replace('<!-- HERO -->', '') if header_html_match else ""
footer_html = footer_html_match.group(0).replace('<!-- Floating WA -->', '') if footer_html_match else ""
fab_html = fab_html_match.group(0).replace('<script>', '') if fab_html_match else ""
js_script = script_match.group(0) if script_match else ""

print("Applying to original index.html...")

# 1. Remove Elementor original header area
# Usually it's in <div data-elementor-type="header" ...> or similar
html = re.sub(r'<div data-elementor-type="header"[^>]*>.*?(?=<div data-elementor-type="wp-page")', '', html, flags=re.DOTALL)
# And the typical <main> spacing
html = html.replace('<body class="', '<body class="')

# 2. Insert the custom header at the start of body
if '<body' in html:
    body_end = html.find('>', html.find('<body')) + 1
    html = html[:body_end] + "\n" + header_html + "\n<main>\n" + html[body_end:]

# 3. Remove Elementor footer area and inject custom footer
html = re.sub(r'<div data-elementor-type="footer"[^>]*>.*', '', html, flags=re.DOTALL)

if '</body>' in html:
    html = html.replace('</body>', f"</main>\n{footer_html}\n{fab_html}\n{js_script}\n</body>")
else:
    html += f"</main>\n{footer_html}\n{fab_html}\n{js_script}\n</body></html>"

# 4. Inject all the CSS blocks
all_css = f"\n<style>\n{header_css}\n{footer_css}\n{hamburger_css}\n{responsive_css}\n{wa_fab_css}\n</style>\n</head>"
html = html.replace('</head>', all_css)

# 5. Fix form: the original form is <form class="elementor-form" method="post" name="New Form">
# We change it to point to Google App Script.
new_form_tag = '''
<script>var submitted_orcamento=false;</script>
<iframe name="hidden_iframe_orc" id="hidden_iframe_orc" style="display:none;" onload="if(submitted_orcamento){document.getElementById('form_response_orc').innerHTML='<div style=&quot;padding:15px;background:#d4edda;color:#155724;border-radius:6px;margin-top:12px;font-weight:bold;&quot;>&#10003; Pedido enviado com sucesso! Entraremos em contacto muito em breve.</div>';}"></iframe>
<form class="elementor-form" action="https://script.google.com/macros/s/AKfycbxwzOED42-82fwCVNUV6XSiHVHDCNJcr-7xWCpWzqjImqZKCUkapHEghToBEEV6pkmT/exec" target="hidden_iframe_orc" method="POST" onsubmit="submitted_orcamento=true;">
'''
html = re.sub(r'<form class="elementor-form" method="post" [^>]*>', new_form_tag, html)
html = html.replace('</form>', '<div id="form_response_orc"></div></form>')

# 6. Apply simple translations (regex-based roughly from translate2.mjs)
t = {
    'Discover more': 'Saiba Mais',
    'Read More': 'Ler Mais',
    'Explore Our Services': 'Explore os Nossos Serviços',
    'Why Choose Us': 'Por Que Nos Escolher',
    'Working Process': 'O Nosso Processo',
    'Residential Roofing': 'Telhados Residenciais no Porto',
    'Commercial Roofing': 'Coberturas Comerciais',
    'View Details': 'Ver Detalhes',
    'Get A Quote': 'Pedir Orçamento',
    'Our Services': 'Nossos Serviços',
    'Learn More': 'Saber Mais',
    'Testimonials': 'Testemunhos',
    'What They Say': 'O Que Dizem os Nossos Clientes',
    'Pricing Plan': 'Preços',
    'Send Message': 'Enviar Mensagem',
    'Latest News': 'Últimas Novidades',
    'Follow Us': 'Siga-nos',
    'Quick Links': 'Links Rápidos',
    'Contact Info': 'Informações de Contacto',
    'Location': 'Localização',
    'Find Us Here': 'Encontre-nos no Porto',
    'Best Roofing': 'Os Melhores Telhados',
    'Services Provider': 'No Grande Porto',
    'Quality Roofing': 'Telhados de Qualidade',
    'Since 2008': 'Desde 2008'
}
for en, pt in t.items():
    regex = rf'>\s*{en}\s*<'
    html = re.sub(regex, f">{pt}<", html, flags=re.IGNORECASE)

html = html.replace('lang="en-US"', 'lang="pt-PT"')
html = html.replace('<title>Roovon - Roofing Services Elementor Template Kit</title>', '<title>Telhados Renovados - Especialistas em Telhados no Porto</title>')

with open("roovon_clone/newkit.creativemox.com/roovon/index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Done reapplying home modifications!")
