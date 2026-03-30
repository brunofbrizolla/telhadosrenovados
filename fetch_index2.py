import urllib.request
import os
import re

url = "https://newkit.creativemox.com/roovon/"
dest = "roovon_clone/newkit.creativemox.com/roovon/index.html"

print(f"Fetching {url}... to get CSS back!")
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as response:
    html = response.read().decode('utf-8', errors='ignore')

print("Applying safe CORS fixes (preserving CSS <link>s)...")

# 1. We ONLY want to remove JS tags, preconnects, prefetch etc.
# <link rel="stylesheet"> stays!
# Remove <link rel="https://api.w.org/"> and <link rel="alternate"> and <link rel="EditURI">
html = re.sub(
    r'<link\b[^>]*rel="(?:https://api\.w\.org/|alternate|EditURI|wlwmanifest|shortlink|preconnect)"[^>]*/?>',
    '',
    html, flags=re.IGNORECASE
)

# 2. Remove external <script src="...newkit..."> blocks to stop active CORS requests
html = re.sub(
    r'<script\b[^>]+src="https?://newkit\.creativemox\.com[^"]*"[^>]*>\s*</script>',
    '',
    html, flags=re.IGNORECASE
)

# 3. Fix Elementor/WordPress inline JS safely without destroying JSON structure.
# This prevents heartbeat and AJAX errors.
html = re.sub(
    r'"ajaxurl":"https?:\\/\\/newkit\.creativemox\.com[^"]*"',
    '"ajaxurl":""',
    html, flags=re.IGNORECASE
)
html = re.sub(
    r'"nonce":"[a-zA-Z0-9]+"([^}]*)"ajaxurl"',
    r'"nonce":""\1"ajaxurl"',
    html, flags=re.IGNORECASE
)

# 4. Remove speculationrules scripts
html = re.sub(
    r'<script type="speculationrules">.*?</script>',
    '',
    html, flags=re.DOTALL | re.IGNORECASE
)

# 5. Fix broken phone regex pattern (HTML form validation)
html = html.replace('pattern="[0-9()#&amp;+*-=.]+"', 'pattern="[0-9()#&amp;+*=.-]+"')

# 6. We MUST reapply the custom header, footer, forms, and translations because this is a clean fetch!
with open("roovon_clone/newkit.creativemox.com/roovon/instalacao-telhados.html", "r", encoding="utf-8") as f:
    ref_html = f.read()

# Extract custom header/footer
header_css_match = re.search(r'/\* ===== HEADER ===== \*/.*?/\* ===== HERO ===== \*/', ref_html, re.DOTALL)
hamburger_css_match = re.search(r'/\* ===== MOBILE HAMBURGER ===== \*/.*?/\* ===== RESPONSIVE ===== \*/', ref_html, re.DOTALL)
responsive_css_match = re.search(r'@media \(max-width: 900px\).*?@media \(min-width: 901px\) \{ #mobile-wa-fab \{ display: none; \} \}', ref_html, re.DOTALL)
wa_fab_css_match = re.search(r'/\* Floating WA button on mobile \*/.*?</style>', ref_html, re.DOTALL)
footer_css_match = re.search(r'/\* ===== FOOTER ===== \*/.*?/\* ===== MOBILE HAMBURGER ===== \*/', ref_html, re.DOTALL)

header_css = header_css_match.group(0) if header_css_match else ""
hamburger_css = hamburger_css_match.group(0) if hamburger_css_match else ""
responsive_css = responsive_css_match.group(0) if responsive_css_match else ""
wa_fab_css = wa_fab_css_match.group(0).replace('</style>', '') if wa_fab_css_match else ""
footer_css = footer_css_match.group(0) if footer_css_match else ""

header_html_match = re.search(r'<!-- HEADER -->.*?<!-- HERO -->', ref_html, re.DOTALL)
footer_html_match = re.search(r'<!-- FOOTER -->.*?<!-- Floating WA -->', ref_html, re.DOTALL)
fab_html_match = re.search(r'<!-- Floating WA -->.*?<script>', ref_html, re.DOTALL)
script_match = re.search(r'<script>\n\(function\(\) \{\n    var header = document\.getElementById.*?\n</script>', ref_html, re.DOTALL)

header_html = header_html_match.group(0).replace('<!-- HERO -->', '') if header_html_match else ""
footer_html = footer_html_match.group(0).replace('<!-- Floating WA -->', '') if footer_html_match else ""
fab_html = fab_html_match.group(0).replace('<script>', '') if fab_html_match else ""
js_script = script_match.group(0) if script_match else ""

# Apply custom header/footer to freshly fetched HTML
html = re.sub(r'<div data-elementor-type="header"[^>]*>.*?(?=<div data-elementor-type="wp-page")', '', html, flags=re.DOTALL)
if '<body' in html:
    body_end = html.find('>', html.find('<body')) + 1
    html = html[:body_end] + "\n" + header_html + "\n<main>\n" + html[body_end:]

html = re.sub(r'<div data-elementor-type="footer"[^>]*>.*', '', html, flags=re.DOTALL)
if '</body>' in html:
    html = html.replace('</body>', f"</main>\n{footer_html}\n{fab_html}\n{js_script}\n</body>")
else:
    html += f"</main>\n{footer_html}\n{fab_html}\n{js_script}\n</body></html>"

all_css = f"\n<style>\n{header_css}\n{footer_css}\n{hamburger_css}\n{responsive_css}\n{wa_fab_css}\n</style>\n</head>"
html = html.replace('</head>', all_css)

new_form_tag = '''
<script>var submitted_orcamento=false;</script>
<iframe name="hidden_iframe_orc" id="hidden_iframe_orc" style="display:none;" onload="if(submitted_orcamento){document.getElementById('form_response_orc').innerHTML='<div style=&quot;padding:15px;background:#d4edda;color:#155724;border-radius:6px;margin-top:12px;font-weight:bold;&quot;>&#10003; Pedido enviado com sucesso! Entraremos em contacto muito em breve.</div>';}"></iframe>
<form class="elementor-form" action="https://script.google.com/macros/s/AKfycbxwzOED42-82fwCVNUV6XSiHVHDCNJcr-7xWCpWzqjImqZKCUkapHEghToBEEV6pkmT/exec" target="hidden_iframe_orc" method="POST" onsubmit="submitted_orcamento=true;">
'''
html = re.sub(r'<form class="elementor-form" method="post" [^>]*>', new_form_tag, html)
html = html.replace('</form>', '<div id="form_response_orc"></div></form>')

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

with open(dest, "w", encoding="utf-8") as f:
    f.write(html)

print("Done downloading and fixing index.html completely!")
