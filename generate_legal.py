import os, codecs, re

DEST_DIR = 'roovon_clone/newkit.creativemox.com/roovon'
INDEX_FILE = os.path.join(DEST_DIR, 'index.html')

with codecs.open(INDEX_FILE, 'r', 'utf-8') as f:
    html = f.read()

# 1. Update the footer links in the html so it serves as the base
html = html.replace('href="#">\n<span class="elementor-icon-list-text">Política de Privacidade</span>', 
                    'href="politica-de-privacidade.html">\n<span class="elementor-icon-list-text">Política de Privacidade</span>')
html = html.replace('href="#">\n<span class="elementor-icon-list-text">Termos e Condições</span>', 
                    'href="termos-e-condicoes.html">\n<span class="elementor-icon-list-text">Termos e Condições</span>')
html = html.replace('href="#">\n<span class="elementor-icon-list-text">Política de Cookies</span>', 
                    'href="politica-de-cookies.html">\n<span class="elementor-icon-list-text">Política de Cookies</span>')
html = html.replace('href="#">\n<span class="elementor-icon-list-text">Política de Garantia</span>', 
                    'href="politica-de-garantia.html">\n<span class="elementor-icon-list-text">Política de Garantia</span>')

# Update ALL html files with these new footer links
for fname in os.listdir(DEST_DIR):
    if fname.endswith('.html'):
        fpath = os.path.join(DEST_DIR, fname)
        with codecs.open(fpath, 'r', 'utf-8') as file:
            content = file.read()
        
        # Replace the placeholders
        c2 = content
        c2 = c2.replace('href="#">\n<span class="elementor-icon-list-text">Política de Privacidade', 'href="politica-de-privacidade.html">\n<span class="elementor-icon-list-text">Política de Privacidade')
        c2 = c2.replace('href="#">\n<span class="elementor-icon-list-text">Termos e Condições', 'href="termos-e-condicoes.html">\n<span class="elementor-icon-list-text">Termos e Condições')
        c2 = c2.replace('href="#">\n<span class="elementor-icon-list-text">Política de Cookies', 'href="politica-de-cookies.html">\n<span class="elementor-icon-list-text">Política de Cookies')
        c2 = c2.replace('href="#">\n<span class="elementor-icon-list-text">Política de Garantia', 'href="politica-de-garantia.html">\n<span class="elementor-icon-list-text">Política de Garantia')
        c2 = c2.replace('href="#" class="elementor-item">Política de Privacidade', 'href="politica-de-privacidade.html" class="elementor-item">Política de Privacidade')
        c2 = c2.replace('href="#" class="elementor-item">Termos e Condições', 'href="termos-e-condicoes.html" class="elementor-item">Termos e Condições')
        
        if c2 != content:
            with codecs.open(fpath, 'w', 'utf-8') as file:
                file.write(c2)
            print(f"Updated footer links in {fname}")

# 2. Extract Header and Footer wrapper from index.html
# Look for <footer class="elementor...
footer_start = html.find('<footer class="elementor elementor-61"')
if footer_start == -1:
    footer_start = html.rfind('<footer')

footer_html = html[footer_start:]

# Look for <div data-elementor-type="... or <div class="elementor elementor-837...
# Let's just find the last </style> tag before the body content
match = re.search(r'</style>\s*<div\s+data-elementor-type=', html)
if match:
    header_html = html[:match.start() + len('</style>\n')]
else:
    # fallback: use </header> and search forward 1000 chars for <div
    hdr_end = html.find('</header>')
    div_start = html.find('<div ', hdr_end)
    header_html = html[:div_start]

print("Extracted Header length:", len(header_html))
print("Extracted Footer length:", len(footer_html))

def build_page(title, content):
    body = f"""
    <div style="background-color: #f8fafc; padding: 120px 20px 80px; min-height: 70vh; font-family: 'Inter', sans-serif;">
        <div style="max-width: 900px; margin: 0 auto; background: white; padding: 50px; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.05);">
            <h1 style="color: #111d35; font-size: 2.2rem; font-weight: 800; margin-bottom: 30px; border-bottom: 2px solid #e2e8f0; padding-bottom: 20px;">{title}</h1>
            <div style="color: #4a5568; line-height: 1.8; font-size: 1.05rem;" class="legal-content">
                {content}
            </div>
        </div>
    </div>
    <style>
        .legal-content h2 {{ color: #111d35; font-size: 1.4rem; font-weight: 700; margin: 35px 0 15px; }}
        .legal-content h3 {{ color: #1e293b; font-size: 1.15rem; font-weight: 600; margin: 25px 0 10px; }}
        .legal-content p {{ margin-bottom: 16px; }}
        .legal-content ul {{ margin-bottom: 20px; padding-left: 20px; }}
        .legal-content li {{ margin-bottom: 8px; }}
        .legal-content a {{ color: #c0392b; text-decoration: none; font-weight: 600; }}
        .legal-content a:hover {{ text-decoration: underline; }}
    </style>
    """
    # Replace the <title> tag in header to reflect the new page
    page_header = re.sub(r'<title>.*?</title>', f'<title>{title} | Telhados Renovados</title>', header_html)
    return page_header + body + footer_html

# Page: Política de Privacidade
privacy_content = """
<p>Atualizado em Março de 2026</p>
<p>A Telhados Renovados ("nós", "nosso", ou "nossa") reconhece a importância de proteger a sua privacidade e os seus dados pessoais. Esta Política de Privacidade explica como recolhemos, utilizamos, partilhamos e protegemos as suas informações quando visita o nosso website ou utiliza os nossos serviços.</p>

<h2>1. Informação que Recolhemos</h2>
<p>Podemos recolher os seguintes tipos de informações:</p>
<ul>
    <li><strong>Dados fornecidos diretamente por si:</strong> Nome, contacto telefónico, endereço de e-mail e morada, fornecidos ao preencher formulários de orçamento ou contacto.</li>
    <li><strong>Informação sobre o projeto:</strong> Detalhes sobre a sua habitação e as suas necessidades de reparação ou remodelação do telhado.</li>
    <li><strong>Informação de navegação:</strong> Dados técnicos recolhidos automaticamente através de cookies (ver secção de Política de Cookies).</li>
</ul>

<h2>2. Utilização da Informação</h2>
<p>Os dados recolhidos são utilizados exclusivamente para:</p>
<ul>
    <li>Responder a pedidos de orçamento e fornecer as estimativas adequadas.</li>
    <li>Agendar visitas técnicas e inspeções ao local.</li>
    <li>Comunicação sobre o projeto através de email, chamada telefónica ou WhatsApp.</li>
    <li>Processamento administrativo e emissão de garantias aos clientes.</li>
</ul>

<h2>3. Partilha de Dados Pessoais</h2>
<p>Não vendemos nem comercializamos os seus dados pessoais. Podemos partilhar as suas informações apenas com:</p>
<ul>
    <li>Funcionários e técnicos da nossa equipa que necessitam da morada para execução do trabalho.</li>
    <li>Autoridades fiscais e legais, quando estritamente exigido por lei.</li>
</ul>

<h2>4. Segurança dos seus Dados</h2>
<p>Implementamos rigorosas medidas de proteção física e digital para prevenir a perda, alteração ou acesso não autorizado à sua informação. Limitamos o acesso a quem realmente precisa das informações operacionais.</p>

<h2>5. Os seus Direitos</h2>
<p>Ao abrigo do RGPD (Regulamento Geral sobre a Proteção de Dados), tem o direito de aceder, retificar, limitar ou apagar os seus dados pessoais guardados na nossa base de dados. Pode exercer este direito contactando-nos através de <a>contacto@telhadosrenovados.pt</a>.</p>
"""

# Page: Termos e Condições
terms_content = """
<p>Atualizado em Março de 2026</p>
<p>Leia atentamente estes Termos e Condições antes de contratar os serviços da Telhados Renovados. Ao avançar com a contratação das nossas equipas de reparação, remodelação ou instalação, concorda com as disposições abaixo indicadas.</p>

<h2>1. Orçamentos e Avaliações</h2>
<p>As nossas inspeções e emissão de orçamentos são gratuitos e sem compromisso para localidades num raio designado no Grande Porto. Um orçamento entregue tem a validade legal descrita no próprio documento (habitualmente 30 dias). Após esse período, reserva-se o direito de revisão de custos de materiais e mão-de-obra.</p>

<h2>2. Execução dos Trabalhos</h2>
<p>Os trabalhos serão executados segundo as boas práticas de construção, nos prazos acordados com o cliente, salvo motivos de força maior: intempéries (chuva constante ou ventos fortes impróprios para trabalhos em altura), indisponibilidade extrema do material no mercado, ou descoberta de problemas estruturais paralelos que afetem a obra.</p>

<h2>3. Condições de Pagamento</h2>
<p>Salvo indicação em contrário formalizada no momento de adjudicação, os nossos serviços exigem um sinal correspondente a % de adjudicação antes do arranque dos trabalhos para aquisição de materiais e agendamento da equipa, e o restante será faturado após conclusão final do trabalho.</p>

<h2>4. Responsabilidades Adicionais</h2>
<p>A preparação do espaço imediato e o acesso seguro ao telhado por onde serão transportados os materiais deve estar livre de limitações extraordinárias que impeçam o início dos trabalhos. Se forem necessários acessos através da propriedade de terceiros, o cliente é responsável por validar essas permissões antecipadamente.</p>
"""

# Page: Política de Cookies
cookies_content = """
<p>Atualizado em Março de 2026</p>
<p>Como muitos websites, a Telhados Renovados utiliza cookies para melhorar a sua experiência digital. Esta política explica de forma clara, simples e transparente a nossa utilização de cookies.</p>

<h2>O que são cookies?</h2>
<p>Cookies são minúsculos ficheiros de texto guardados no seu computador ou dispositivo móvel quando acede e interage connosco através do navegador. Estes indicadores temporários permitem-nos compreender que tipo de serviços prefere, reter o seu histórico temporário e garantir um funcionamento rápido do site.</p>

<h2>Como utilizamos os cookies?</h2>
<ul>
    <li><strong>Cookies Estritamente Necessários:</strong> Fundamentais para a segurança do nosso site e navegação fluida; sem estes a página web pode não funcionar como previsto.</li>
    <li><strong>Cookies de Desempenho e de Análise:</strong> Utilizados para obter ferramentas de contagem de visitas, por quais páginas o cliente entrou, e os serviços em que teve mais interesse, gerados pelo Google Analytics, de forma totalmente anónima.</li>
    <li><strong>Cookies Funcionais:</strong> Armazenam escolhas do cliente como temas, e não recolhem informações de identificação.</li>
</ul>

<h2>Como gerir os cookies?</h2>
<p>A qualquer momento, o utilizador pode predefinir no seu explorador web (browser) como bloquear, recusar novas ou apagar todas as cookies anteriormente guardadas. Importa salientar que ao bloqueares cookies da Telhados Renovados, determinadas secções poderão não preencher instantaneamente a máxima experiência prevista.</p>
"""

# Page: Política de Garantia
warranty_content = """
<p>Atualizado em Março de 2026</p>

<p>Na Telhados Renovados levamos a durabilidade e a confiança dos nossos trabalhos muito a sério. Assumimos um compromisso claro e duradouro porque sabemos dos materiais que utilizamos e confiamos nos nossos profissionais.</p>

<h2>1. Garantias por Categoria de Serviço</h2>
<ul>
    <li><strong>Instalação de Novos Telhados e Remodelação Total:</strong> Estão automaticamente abrangidos pela Garantia Construção de longa escala dos trabalhos por <strong>5 a 10 Anos</strong> consoante o projeto.</li>
    <li><strong>Sistemas De Impermeabilização:</strong> As membranas, poliuretano e todos os produtos de selagem beneficiam numa exclusão de humidades e infiltrações entre <strong>5 a 10 anos</strong>, registados ao abrigo no fim dos trabalhos de intervenção.</li>
    <li><strong>Trabalhos de Reparação e Remendos Menores:</strong> Todas as reparações têm um período de Garantia Técnica do re-serviço (mão-de-obra) sobre os items substituídos.</li>
    <li><strong>Materiais de Construção Utilizados:</strong> Os painéis telha e membranas gozam inteiramente sob protecção vital das fábricas de origem (podendo estas ir de 10 a 30 anos pelos fabricantes).</li>
</ul>

<h2>2. Condições para Validade da Garantia</h2>
<p>A proteção da Garantia é mantida plenamente sob os seguintes trâmites:</p>
<ul>
    <li>A fatura ou contrato do serviço foi formalizado e não tem montantes em dívida em final de processo de construção/remodelação.</li>
    <li>Queixume de intervenções alheias, se danos foram causados por terceiras empresas/profissionais para arranjo de varandas/instalação de parabólicas depois do nosso selo.</li>
    <li>Fatores e Desastres Naturais Extremos tais como furações (ventos extremos ou quebra maciça de granizos anormais com alerta vermelho local).</li>
</ul>

<h2>3. Procedimento de Ativação de Anomalias Reais</h2>
<p>Dentro deste período, caso detete alguma inconformidade ou repare em nova infiltração exatamente e derivado dos nossos trabalhos efetuados, deve providenciar aviso rápido num período útil de 15 dias aos nossos contactos por telemóvel (+351 937 065 056) ou enviando email (contacto@telhadosrenovados.pt) identificando a data da obra para vistoriarmos presencialmente e acionar o protocolo em total respeito e eficácia.</p>
"""

# Save Pages
pages = [
    ('politica-de-privacidade.html', 'Política de Privacidade', privacy_content),
    ('termos-e-condicoes.html', 'Termos e Condições', terms_content),
    ('politica-de-cookies.html', 'Política de Cookies', cookies_content),
    ('politica-de-garantia.html', 'Política de Garantia', warranty_content)
]

for filename, title, content in pages:
    page_html = build_page(title, content)
    filepath = os.path.join(DEST_DIR, filename)
    with codecs.open(filepath, 'w', 'utf-8') as f:
        f.write(page_html)
    print("Created:", filename)
