import os

file_path = r"C:\Users\Lenovo\Downloads\TELHADOS RENOVADOS\roovon_clone\newkit.creativemox.com\roovon\index.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

new_html = """
<!-- SEO CONTENT SECTIONS -->
<style>
.seo-two-col { display: grid; grid-template-columns: 1fr 1fr; gap: 60px; align-items: center; }
@media(max-width: 900px) { .seo-two-col { grid-template-columns: 1fr; gap: 40px; } }
.process-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 30px; margin-top:40px; }
.seo-card { background: #f8fafc; padding: 30px; border-radius: 12px; border-left: 4px solid var(--red); box-shadow: 0 4px 15px rgba(0,0,0,0.03); }
</style>

<!-- 1. Sobre Nós -->
<section class="section" style="background:var(--light-gray);">
    <div class="container">
        <div class="seo-two-col">
            <div>
                <span class="section-tag">A Empresa</span>
                <h2 class="section-title">Telhados Renovados: A sua Empresa de Confian&ccedil;a no Porto</h2>
                <h3 style="color:var(--red); font-size:1.3rem; margin-bottom:15px; font-weight:800;">Profissionalismo, Compet&ecirc;ncia e Pre&ccedil;o Imbat&iacute;vel.</h3>
                <p style="margin-bottom:15px; color:var(--gray); line-height:1.7; font-size:1.05rem;">Na Telhados Renovados, somos especialistas na instala&ccedil;&atilde;o e repara&ccedil;&atilde;o de coberturas. Com uma vasta experi&ecirc;ncia acumulada, oferecemos os pre&ccedil;os mais competitivos de todo o Norte de Portugal. Focamo-nos em tr&ecirc;s pilares fundamentais:</p>
                <ul style="list-style:none; margin-bottom:25px; color:var(--navy); font-weight:700; line-height:1.8; font-size:1.05rem;">
                    <li><svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="var(--red)" stroke-width="3" style="vertical-align:middle;margin-right:10px;"><polyline points="20 6 9 17 4 12"></polyline></svg> Instala&ccedil;&atilde;o de novos telhados;</li>
                    <li><svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="var(--red)" stroke-width="3" style="vertical-align:middle;margin-right:10px;"><polyline points="20 6 9 17 4 12"></polyline></svg> Repara&ccedil;&atilde;o urgente e estrutural;</li>
                    <li><svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="var(--red)" stroke-width="3" style="vertical-align:middle;margin-right:10px;"><polyline points="20 6 9 17 4 12"></polyline></svg> Manuten&ccedil;&atilde;o preventiva.</li>
                </ul>
                <div style="background:#fff; border-left:4px solid var(--red); padding:20px 25px; border-radius:12px; box-shadow:0 4px 20px rgba(0,0,0,0.05);">
                    <p style="color:var(--navy); font-weight:800; line-height:1.6; margin-bottom:0;">&#9888; Aten&ccedil;&atilde;o aos sinais! Humidade nas paredes, cantos do teto manchados ou pingos de &aacute;gua s&atilde;o avisos cr&iacute;ticos. Assim que detetar uma infiltra&ccedil;&atilde;o, contacte-nos de imediato.</p>
                </div>
                <p style="margin-top:25px; color:var(--gray); line-height:1.7; font-size:1.05rem;">A Telhados Renovados disp&otilde;e de equipas multidisciplinares prontas a atuar em todo o distrito do Porto (Porto, Gaia, Maia, Matosinhos, Gondomar, Valongo, Trofa, Vila do Conde, Paredes, entre outros).</p>
            </div>
            <img src="img-instalacao.webp" alt="Equipa Telhados Renovados a trabalhar no telhado" style="border-radius:16px; box-shadow:0 20px 40px rgba(0,0,0,0.15); width:100%; object-fit:cover; height:580px;">
        </div>
    </div>
</section>

<!-- 2. Método de Trabalho -->
<section class="section" style="background:#fff;">
    <div class="container">
        <div class="section-header">
            <span class="section-tag">Efici&ecirc;ncia Passo a Passo</span>
            <h2 class="section-title">O Nosso M&eacute;todo de Trabalho</h2>
            <p>O seu telhado est&aacute; danificado pelas agress&otilde;es clim&aacute;ticas? Na Telhados Renovados, o nosso processo &eacute; rigoroso:</p>
        </div>
        <div class="process-grid">
            <div class="seo-card">
                <h3 style="color:var(--navy); margin-bottom:12px; font-size:1.25rem; font-weight:800;">1. Limpeza e Diagn&oacute;stico</h3>
                <p style="color:var(--gray); font-size:1rem; line-height:1.6; margin:0;">Limpamos o local e as caleiras para identificar a origem exata da infiltra&ccedil;&atilde;o.</p>
            </div>
            <div class="seo-card">
                <h3 style="color:var(--navy); margin-bottom:12px; font-size:1.25rem; font-weight:800;">2. Substitui&ccedil;&atilde;o</h3>
                <p style="color:var(--gray); font-size:1rem; line-height:1.6; margin:0;">Trocamos telhas danificadas (cer&acirc;mica, lusa, marselha, sandwich, portuguesa, fibrocimento, etc.).</p>
            </div>
            <div class="seo-card">
                <h3 style="color:var(--navy); margin-bottom:12px; font-size:1.25rem; font-weight:800;">3. Refor&ccedil;o Estrutural</h3>
                <p style="color:var(--gray); font-size:1rem; line-height:1.6; margin:0;">Consolidamos as zonas fragilizadas garantindo a seguran&ccedil;a do im&oacute;vel.</p>
            </div>
            <div class="seo-card">
                <h3 style="color:var(--navy); margin-bottom:12px; font-size:1.25rem; font-weight:800;">4. Isolamento</h3>
                <p style="color:var(--gray); font-size:1rem; line-height:1.6; margin:0;">Aplicamos materiais isolantes t&eacute;rmicos e ac&uacute;sticos de &uacute;ltima gera&ccedil;&atilde;o.</p>
            </div>
        </div>
        <div style="margin-top:50px; text-align:center; padding:24px; background:rgba(192,57,43,0.06); border-radius:12px; border:1px dashed rgba(192,57,43,0.3);">
            <p style="color:var(--red); font-weight:800; font-size:1.1rem; margin-bottom:0;">&#128161; Dica dos Especialistas: Realize inspe&ccedil;&otilde;es e limpezas anuais para evitar custos elevados no futuro.</p>
        </div>
    </div>
</section>

<!-- 3 e 4. Sandwich vs Cerâmica + Segurança -->
<section class="section" style="background:var(--light-gray);">
    <div class="container">
        <div class="seo-two-col" style="align-items:start;">
            <div>
                <span class="section-tag">O que escolher?</span>
                <h2 class="section-title" style="font-size:2.2rem; margin-bottom:15px;">Telhado Sandwich ou Telha Cer&acirc;mica?</h2>
                <p style="margin-bottom:25px; color:var(--gray); font-size:1.05rem; line-height:1.7;">Na Telhados Renovados, ajudamo-lo a escolher a melhor op&ccedil;&atilde;o para o seu or&ccedil;amento e tipo de im&oacute;vel (moradia, pr&eacute;dio ou pavilh&atilde;o industrial).</p>
                <div style="background:#fff; padding:25px 30px; border-radius:12px; margin-bottom:20px; box-shadow:0 4px 20px rgba(0,0,0,0.04); border-left:5px solid var(--navy);">
                    <strong style="color:var(--navy); font-size:1.15rem; display:block; margin-bottom:8px;">&#127968; Telha Cer&acirc;mica (Tradicional)</strong> 
                    <p style="color:var(--gray); font-size:1rem; line-height:1.6; margin:0;">Excelente durabilidade, est&eacute;tica cl&aacute;ssica portuguesa e &oacute;timo comportamento t&eacute;rmico. &Eacute; a solu&ccedil;&atilde;o "ecol&oacute;gica" feita de argila.</p>
                </div>
                <div style="background:#fff; padding:25px 30px; border-radius:12px; box-shadow:0 4px 20px rgba(0,0,0,0.04); border-left:5px solid var(--navy);">
                    <strong style="color:var(--navy); font-size:1.15rem; display:block; margin-bottom:8px;">&#127981; Painel Sandwich (Moderno)</strong> 
                    <p style="color:var(--gray); font-size:1rem; line-height:1.6; margin:0;">Alta capacidade de isolamento (at&eacute; 90% t&eacute;rmico), instala&ccedil;&atilde;o r&aacute;pida, vers&aacute;til e ideal para evitar condensa&ccedil;&otilde;es. Muito resistente e personaliz&aacute;vel.</p>
                </div>
            </div>
            
            <div style="background:#fff; border-radius:16px; box-shadow:0 20px 50px rgba(0,0,0,0.1); padding:50px 40px; text-align:center; display:flex; flex-direction:column; justify-content:center; height:100%;">
                <div style="width:80px; height:80px; background:rgba(192,57,43,0.1); border-radius:50%; display:flex; align-items:center; justify-content:center; margin:0 auto 24px; color:var(--red);">
                    <svg viewBox="0 0 24 24" width="40" height="40" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
                </div>
                <h2 class="section-title" style="font-size:2rem; color:var(--red); margin-bottom:15px;">Seguran&ccedil;a em Primeiro Lugar!</h2>
                <h3 style="font-size:1.25rem; color:var(--navy); margin-bottom:20px; font-weight:800;">N&atilde;o se Arrisque. As quedas podem ser fatais.</h3>
                <p style="color:var(--gray); line-height:1.7; font-size:1.05rem; margin-bottom:20px;">A repara&ccedil;&atilde;o de telhados &eacute; uma atividade de alto risco. N&atilde;o tente subir ao telhado sozinho.</p>
                <p style="color:var(--gray); line-height:1.7; font-size:1.05rem;">As equipas da Telhados Renovados s&atilde;o certificadas, utilizam equipamento de prote&ccedil;&atilde;o individual (arn&ecirc;s e linhas de vida) e t&ecirc;m treino espec&iacute;fico para trabalhar sob as condi&ccedil;&otilde;es clim&aacute;ticas exigentes do Norte de Portugal.</p>
            </div>
        </div>
    </div>
</section>

<!-- 5, 6 e 7. Preços, Prevenção e Tipos -->
<section class="section" style="background:#fff;">
    <div class="container">
        
        <div class="seo-two-col" style="align-items:start; margin-bottom:80px;">
            <!-- Preços -->
            <div>
                <span class="section-tag">Or&ccedil;amentos</span>
                <h2 class="section-title" style="font-size:2.2rem; margin-bottom:15px;">Quanto custa o seu novo telhado?</h2>
                <p style="color:var(--gray); margin-bottom:30px; line-height:1.7; font-size:1.05rem;">Oferecemos o melhor pre&ccedil;o de repara&ccedil;&atilde;o de telhados no Porto.</p>
                
                <div style="background:var(--light-gray); padding:30px; border-radius:12px; margin-bottom:20px; border-left:4px solid var(--navy);">
                    <strong style="color:var(--navy); font-size:1.2rem; display:block; margin-bottom:8px;">Pequenas Repara&ccedil;&otilde;es</strong>
                    <span style="color:var(--gray); font-size:1.05rem; line-height:1.6; display:block;">Troca de telhas ou repara&ccedil;&atilde;o de caleiras a pre&ccedil;os incrivelmente econ&oacute;micos.</span>
                </div>
                
                <div style="background:var(--light-gray); padding:30px; border-radius:12px; border-left:4px solid var(--navy);">
                    <strong style="color:var(--navy); font-size:1.2rem; display:block; margin-bottom:8px;">Substitui&ccedil;&atilde;o Completa</strong>
                    <span style="color:var(--gray); font-size:1.05rem; line-height:1.6; display:block;">O custo m&eacute;dio de um servi&ccedil;o completo (substitui&ccedil;&atilde;o + isolamento) ronda os 100&euro;/m&sup2;, variando entre os 60&euro;/m&sup2; e os 150&euro;/m&sup2; consoante os materiais escolhidos.</span>
                </div>
            </div>

            <!-- Prevenção -->
            <div style="background:linear-gradient(135deg, #0d2a45, #111d35); color:#fff; padding:50px 40px; border-radius:16px; box-shadow:0 20px 40px rgba(17,29,53,0.2);">
                <h2 class="section-title" style="font-size:2rem; color:#fff; border-bottom:1px solid rgba(255,255,255,0.1); padding-bottom:20px; margin-bottom:25px;">Preven&ccedil;&atilde;o: O "Dentista" do seu Telhado</h2>
                <p style="color:rgba(255,255,255,0.8); margin-bottom:25px; line-height:1.7; font-size:1.05rem;">Tal como a higiene oral evita dores de dentes, a manuten&ccedil;&atilde;o preventiva evita desastres financeiros. A Telhados Renovados recomenda:</p>
                <ul style="list-style:none; padding:0; margin:0; color:rgba(255,255,255,0.95); line-height:1.7; font-size:1.05rem;">
                    <li style="margin-bottom:15px;"><svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="var(--red)" stroke-width="3" style="vertical-align:middle;margin-right:10px;"><polyline points="20 6 9 17 4 12"></polyline></svg> Vistorias antes do inverno.</li>
                    <li style="margin-bottom:15px;"><svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="var(--red)" stroke-width="3" style="vertical-align:middle;margin-right:10px;"><polyline points="20 6 9 17 4 12"></polyline></svg> Verifica&ccedil;&atilde;o de estruturas de madeira.</li>
                    <li style="margin-bottom:15px;"><svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="var(--red)" stroke-width="3" style="vertical-align:middle;margin-right:10px;"><polyline points="20 6 9 17 4 12"></polyline></svg> Limpeza de caleiras e algerozes (folhas, musgos e ninhos).</li>
                    <li style="margin-top:25px; padding-top:25px; border-top:1px solid rgba(255,255,255,0.1);"><strong style="color:var(--red);">Remo&ccedil;&atilde;o de Amianto:</strong> Substitu&iacute;mos o antigo fibrocimento por solu&ccedil;&otilde;es modernas e seguras para a sa&uacute;de.</li>
                </ul>
            </div>
        </div>

        <div style="text-align:center; max-width:900px; margin:0 auto; background:var(--light-gray); padding:50px; border-radius:16px; border:1px solid var(--border);">
            <h2 class="section-title">Especialistas em Todo o Tipo de Coberturas</h2>
            <div style="display:flex; flex-wrap:wrap; justify-content:center; gap:12px; margin-top:30px; margin-bottom:40px;">
                <span style="background:#fff; color:var(--navy); padding:12px 24px; border-radius:100px; font-weight:700; font-size:1rem; box-shadow:0 4px 15px rgba(0,0,0,0.05); border:1px solid var(--border);">Telha Cer&acirc;mica: Modelos Lusa, Marselha, Canudo, etc.</span>
                <span style="background:#fff; color:var(--navy); padding:12px 24px; border-radius:100px; font-weight:700; font-size:1rem; box-shadow:0 4px 15px rgba(0,0,0,0.05); border:1px solid var(--border);">Painel Sandwich: O rei do isolamento industrial e residencial.</span>
                <span style="background:#fff; color:var(--navy); padding:12px 24px; border-radius:100px; font-weight:700; font-size:1rem; box-shadow:0 4px 15px rgba(0,0,0,0.05); border:1px solid var(--border);">Telhas Met&aacute;licas: Leveza e resist&ecirc;ncia.</span>
                <span style="background:#fff; color:var(--navy); padding:12px 24px; border-radius:100px; font-weight:700; font-size:1rem; box-shadow:0 4px 15px rgba(0,0,0,0.05); border:1px solid var(--border);">Telhas de Vidro e Policarbonato: Para maximizar a luz natural.</span>
                <span style="background:#fff; color:var(--navy); padding:12px 24px; border-radius:100px; font-weight:700; font-size:1rem; box-shadow:0 4px 15px rgba(0,0,0,0.05); border:1px solid var(--border);">Estruturas de A&ccedil;o Leve (LSF): Modernidade e rapidez.</span>
            </div>
            <h3 style="color:var(--red); font-size:1.5rem; font-weight:800; margin:0;">Telhados Renovados: Mantemos o seu telhado bonito, funcional e seguro.</h3>
        </div>

    </div>
</section>

<!-- FIM SEO CONTENT SECTIONS -->

<!-- WHY US -->
"""

if "<!-- WHY US -->" in content:
    content = content.replace("<!-- WHY US -->", new_html)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Injected SEO Content Sections Successfully.")
else:
    print("Could not find <!-- WHY US --> in index.html")
