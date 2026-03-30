import os

OUTPUT_DIR = 'roovon_clone/newkit.creativemox.com/roovon'

def get_header(active_page=''):
    return f'''<header id="custom-roovon-header">
    <div class="crh-container">
        <div class="crh-logo"><a href="index.html"><img src="logo_telhados_renovados.jpg" alt="Telhados Renovados Logo"></a></div>
        <nav class="crh-nav">
            <ul class="crh-menu">
                <li><a href="index.html">Home</a></li>
                <li class="crh-has-dropdown">
                    <a href="#">Serviços <svg viewBox="0 0 320 512" width="10" height="10" style="margin-left:3px"><path fill="currentColor" d="M143 352.3L7 216.3c-9.4-9.4-9.4-24.6 0-33.9l22.6-22.6c9.4-9.4 24.6-9.4 33.9 0l96.4 96.4 96.4-96.4c9.4-9.4 24.6-9.4 33.9 0l22.6 22.6c9.4 9.4 9.4 24.6 0 33.9l-136 136c-9.2 9.4-24.4 9.4-33.8 0z"/></svg></a>
                    <ul class="crh-dropdown">
                        <li{"  class='active-page'" if active_page=='instalacao' else ''}><a href="instalacao-telhados.html">Instalação de Telhados e Coberturas</a></li>
                        <li{"  class='active-page'" if active_page=='remodelacao' else ''}><a href="remodelacao-telhados.html">Remodelação de Telhados</a></li>
                        <li{"  class='active-page'" if active_page=='reparacao' else ''}><a href="reparacao-telhados.html">Reparação de Telhados</a></li>
                        <li{"  class='active-page'" if active_page=='impermeabilizacao' else ''}><a href="sistemas-impermeabilizacao.html">Sistemas de Impermeabilização</a></li>
                        <li{"  class='active-page'" if active_page=='limpeza' else ''}><a href="limpeza-telhados.html">Limpeza e Manutenção</a></li>
                        <li{"  class='active-page'" if active_page=='caleiras' else ''}><a href="caleiras-rufagem.html">Aplicação de Caleiras e Rufagem</a></li>
                    </ul>
                </li>
                <li><a href="contactos.html">Contactos</a></li>
            </ul>
        </nav>
        <div class="crh-actions">
            <a href="contactos.html" class="crh-btn crh-btn-navy">FAÇA SEU ORÇAMENTO</a>
            <a href="https://wa.me/351937065056" target="_blank" class="crh-btn crh-btn-whatsapp">
                <svg viewBox="0 0 448 512" width="14" height="14"><path fill="currentColor" d="M380.9 97.1C339 55.1 283.2 32 223.9 32c-122.4 0-222 99.6-222 222 0 39.1 10.2 77.3 29.6 111L0 480l117.7-30.9c32.4 17.7 68.9 27 106.1 27h.1c122.3 0 224.1-99.6 224.1-222 0-59.3-23.2-115-65.1-157z"/></svg>
                FALE NO WHATSAPP
            </a>
        </div>
        <button class="crh-hamburger" id="crh-hamburger" aria-label="Menu"><span></span><span></span><span></span></button>
    </div>
</header>'''

SHARED_CSS = '''<style>
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
:root{--navy:#111d35;--red:#c0392b;--green:#25D366;--gray:#64748b;--light:#f8fafc;--border:#e2e8f0;--text:#1e293b}
html{overflow-x:hidden;scroll-behavior:smooth}
body{font-family:'Inter',sans-serif;color:var(--text);overflow-x:hidden}
img{max-width:100%;height:auto}
#custom-roovon-header{background:#fff;position:fixed;top:0;left:0;right:0;z-index:99999;box-shadow:0 2px 10px rgba(0,0,0,0.05);overflow:visible;transition:box-shadow 0.3s}
#custom-roovon-header.scrolled{box-shadow:0 2px 20px rgba(0,0,0,0.12);backdrop-filter:blur(8px)}
.crh-container{max-width:1250px;margin:0 auto;display:flex;align-items:center;justify-content:space-between;padding:4px 20px;overflow:visible;transition:padding 0.3s}
#custom-roovon-header.scrolled .crh-container{padding:0 20px}
.crh-logo{overflow:visible;display:flex;align-items:center}
.crh-logo img{height:90px;width:auto;margin-top:20px;filter:drop-shadow(0 4px 6px rgba(0,0,0,0.18));transition:height 0.35s,margin-top 0.35s}
#custom-roovon-header.scrolled .crh-logo img{height:40px;margin-top:0;filter:none}
.crh-menu{list-style:none;display:flex;gap:32px;align-items:center}
.crh-menu a{text-decoration:none;color:#666;font-weight:700;font-size:14.5px;display:flex;align-items:center;padding:15px 0;transition:color 0.2s}
.crh-menu>li>a:hover{color:#1a202c}
.crh-has-dropdown{position:relative}
.crh-dropdown{position:absolute;top:100%;left:0;background:#fff;min-width:280px;list-style:none;padding:0;box-shadow:0 4px 15px rgba(0,0,0,0.08);opacity:0;visibility:hidden;transform:translateY(10px);transition:all 0.2s;border-top:3px solid #0d2a45}
.crh-has-dropdown:hover .crh-dropdown{opacity:1;visibility:visible;transform:translateY(0)}
.crh-dropdown a{color:#4a5568!important;font-weight:500!important;padding:15px 20px;display:block;font-size:14px;border-bottom:1px solid #f1f5f9}
.crh-dropdown a:hover{color:#fff!important;background:#0d2a45!important}
.crh-dropdown .active-page a{color:#fff!important;background:#c0392b!important}
.crh-actions{display:flex;align-items:center;gap:12px}
.crh-btn{display:flex;align-items:center;gap:8px;padding:8px 18px;font-weight:700;font-size:12px;border-radius:4px;text-decoration:none;transition:all 0.2s;text-transform:uppercase}
.crh-btn-navy{background:#111d35!important;color:#fff!important}
.crh-btn-whatsapp{background:#25D366!important;color:#fff!important}
.crh-hamburger{display:none;flex-direction:column;gap:5px;background:none;border:none;cursor:pointer;padding:6px}
.crh-hamburger span{display:block;width:24px;height:2px;background:#1a202c;border-radius:2px;transition:transform 0.3s,opacity 0.3s}
.crh-hamburger.open span:nth-child(1){transform:translateY(7px) rotate(45deg)}
.crh-hamburger.open span:nth-child(2){opacity:0}
.crh-hamburger.open span:nth-child(3){transform:translateY(-7px) rotate(-45deg)}
.page-hero{padding-top:160px;background:linear-gradient(135deg,#0d2a45,#111d35 60%,#1a0a0a);padding-bottom:80px;position:relative;overflow:hidden}
.page-hero .container{max-width:1200px;margin:0 auto;padding:0 24px;position:relative;z-index:1}
.breadcrumb{display:flex;gap:8px;align-items:center;margin-bottom:20px}
.breadcrumb a{color:rgba(255,255,255,0.6);font-size:13px;text-decoration:none}
.breadcrumb span{color:rgba(255,255,255,0.4);font-size:13px}
.page-hero h1{color:#fff;font-size:clamp(2rem,5vw,3.2rem);font-weight:800;line-height:1.2;margin-bottom:20px}
.page-hero h1 em{color:#c0392b;font-style:normal}
.page-hero p{color:rgba(255,255,255,0.75);font-size:1.1rem;max-width:600px;line-height:1.7;margin-bottom:36px}
.hero-ctas{display:flex;gap:16px;flex-wrap:wrap}
.btn-primary{background:#c0392b;color:#fff;padding:16px 32px;border-radius:4px;font-weight:700;font-size:14px;text-decoration:none;text-transform:uppercase;transition:background 0.2s;display:inline-flex;align-items:center;gap:10px}
.btn-primary:hover{background:#a93226}
.btn-outline{border:2px solid rgba(255,255,255,0.4);color:#fff;padding:16px 32px;border-radius:4px;font-weight:700;font-size:14px;text-decoration:none;text-transform:uppercase;transition:all 0.2s;display:inline-flex;align-items:center;gap:10px}
.btn-outline:hover{background:rgba(255,255,255,0.1);border-color:#fff}
.section{padding:80px 0}
.section.gray{background:var(--light)}
.container{max-width:1200px;margin:0 auto;padding:0 24px}
.section-tag{display:inline-block;background:rgba(192,57,43,0.1);color:var(--red);font-size:12px;font-weight:700;text-transform:uppercase;letter-spacing:2px;padding:6px 14px;border-radius:100px;margin-bottom:14px}
.section-title{font-size:clamp(1.6rem,4vw,2.4rem);font-weight:800;color:var(--navy);line-height:1.25;margin-bottom:16px}
.section-sub{color:var(--gray);font-size:1.05rem;line-height:1.75;max-width:680px}
.two-col{display:grid;grid-template-columns:1fr 1fr;gap:60px;align-items:center}
.two-col img{border-radius:12px;box-shadow:0 8px 32px rgba(0,0,0,0.12);width:100%;height:380px;object-fit:cover}
.features-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:24px;margin-top:48px}
.feature-card{background:#fff;border:1px solid var(--border);border-radius:12px;padding:28px;transition:box-shadow 0.2s,transform 0.2s}
.feature-card:hover{box-shadow:0 8px 32px rgba(0,0,0,0.1);transform:translateY(-4px)}
.feature-icon{width:52px;height:52px;background:rgba(192,57,43,0.1);border-radius:10px;display:flex;align-items:center;justify-content:center;color:var(--red);margin-bottom:16px}
.feature-card h3{font-size:1rem;font-weight:700;color:var(--navy);margin-bottom:8px}
.feature-card p{font-size:0.9rem;color:var(--gray);line-height:1.65}
.process-steps{display:grid;grid-template-columns:repeat(4,1fr);gap:24px;margin-top:48px}
.process-step{text-align:center}
.step-num{width:56px;height:56px;background:var(--navy);color:#fff;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:1.4rem;font-weight:800;margin:0 auto 16px}
.process-step h3{font-size:1rem;font-weight:700;color:var(--navy);margin-bottom:8px}
.process-step p{font-size:0.88rem;color:var(--gray);line-height:1.6}
.cta-band{background:linear-gradient(135deg,var(--navy),#1e335e);padding:64px 0;text-align:center}
.cta-band h2{color:#fff;font-size:clamp(1.5rem,4vw,2.2rem);font-weight:800;margin-bottom:12px}
.cta-band p{color:rgba(255,255,255,0.7);font-size:1rem;margin-bottom:32px}
.cta-buttons{display:flex;gap:16px;justify-content:center;flex-wrap:wrap}
.btn-wa{background:#25D366;color:#fff;padding:16px 32px;border-radius:4px;font-weight:700;font-size:14px;text-decoration:none;text-transform:uppercase;display:inline-flex;align-items:center;gap:10px;transition:background 0.2s}
.btn-wa:hover{background:#20b858}
.btn-call{background:rgba(255,255,255,0.1);border:2px solid rgba(255,255,255,0.3);color:#fff;padding:16px 32px;border-radius:4px;font-weight:700;font-size:14px;text-decoration:none;text-transform:uppercase;display:inline-flex;align-items:center;gap:10px;transition:all 0.2s}
.btn-call:hover{background:rgba(255,255,255,0.2)}
footer{background:#05111f;color:rgba(255,255,255,0.6);padding:48px 0 24px}
.footer-inner{display:grid;grid-template-columns:2fr 1fr 1fr;gap:40px;margin-bottom:36px}
.footer-logo img{height:60px;margin-bottom:16px}
.footer-desc{font-size:0.9rem;line-height:1.7;max-width:300px}
footer h4{color:#fff;font-size:0.95rem;font-weight:700;margin-bottom:16px}
footer ul{list-style:none}
footer ul li{margin-bottom:8px}
footer ul li a{color:rgba(255,255,255,0.55);text-decoration:none;font-size:0.88rem;transition:color 0.2s}
footer ul li a:hover{color:#fff}
.footer-bottom{border-top:1px solid rgba(255,255,255,0.1);padding-top:24px;text-align:center;font-size:0.82rem}
#mobile-wa-fab{position:fixed;bottom:22px;right:22px;width:56px;height:56px;background:#25D366;color:#fff;border-radius:50%;display:flex;align-items:center;justify-content:center;box-shadow:0 4px 16px rgba(37,211,102,0.45);z-index:999998;text-decoration:none;transition:transform 0.2s}
#mobile-wa-fab:hover{transform:scale(1.1)}
@media(max-width:900px){
    .crh-hamburger{display:flex!important}
    .crh-nav{display:none;width:100%;order:3;background:#fff;border-top:1px solid #f0f0f0;padding:8px 0}
    .crh-nav.open{display:block}
    .crh-menu{flex-direction:column;gap:0;width:100%}
    .crh-menu>li>a{padding:12px 20px;border-bottom:1px solid #f5f5f5}
    .crh-dropdown{position:static;box-shadow:none;opacity:1;visibility:visible;transform:none;display:none;border-left:3px solid #0d2a45;margin-left:20px;min-width:auto}
    .crh-has-dropdown.open-mobile .crh-dropdown{display:block}
    .crh-actions{display:none!important}
    .crh-actions.open{display:flex!important;flex-direction:column;width:100%;padding:12px 16px;background:#fff}
    .crh-logo img{height:55px;margin-top:8px}
    .crh-container{flex-wrap:wrap}
    .two-col{grid-template-columns:1fr}
    .features-grid{grid-template-columns:1fr}
    .process-steps{grid-template-columns:1fr 1fr}
    .footer-inner{grid-template-columns:1fr}
}
@media(min-width:901px){#mobile-wa-fab{display:none!important}}
@media(max-width:480px){.process-steps{grid-template-columns:1fr}.page-hero{padding-top:130px}}
</style>'''

SCRIPT = '''<script>
(function(){
var h=document.getElementById('custom-roovon-header');
var hb=document.getElementById('crh-hamburger');
var nav=document.querySelector('.crh-nav');
var act=document.querySelector('.crh-actions');
var srv=document.querySelector('.crh-has-dropdown');
window.addEventListener('scroll',function(){h.classList.toggle('scrolled',window.scrollY>60);},{passive:true});
if(hb){hb.addEventListener('click',function(){var o=nav.classList.contains('open');hb.classList.toggle('open',!o);nav.classList.toggle('open',!o);if(act)act.classList.toggle('open',!o);});}
if(srv){srv.querySelector('a').addEventListener('click',function(e){if(window.innerWidth<=900){e.preventDefault();srv.classList.toggle('open-mobile');}});}
})();
</script>'''

WA_SVG = '<svg viewBox="0 0 448 512" width="16" height="16"><path fill="currentColor" d="M380.9 97.1C339 55.1 283.2 32 223.9 32c-122.4 0-222 99.6-222 222 0 39.1 10.2 77.3 29.6 111L0 480l117.7-30.9c32.4 17.7 68.9 27 106.1 27h.1c122.3 0 224.1-99.6 224.1-222 0-59.3-23.2-115-65.1-157z"/></svg>'
PHONE_SVG = '<svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 01-2.18 2 19.79 19.79 0 01-8.63-3.07A19.5 19.5 0 013.07 10.8a19.79 19.79 0 01-3.07-8.68A2 2 0 012 0h3a2 2 0 012 1.72c.127.96.361 1.903.7 2.81a2 2 0 01-.45 2.11L6.09 7.91a16 16 0 006 6l1.27-1.27a2 2 0 012.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0122 14.92z"/></svg>'
EMAIL_SVG = '<svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>'

def icon(d, size=26):
    return f'<svg viewBox="0 0 24 24" width="{size}" height="{size}" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">{d}</svg>'

def fc(icon_svg, title, text):
    return f'<div class="feature-card"><div class="feature-icon">{icon_svg}</div><h3>{title}</h3><p>{text}</p></div>'

def step(n, t, p):
    return f'<div class="process-step"><div class="step-num">{n}</div><h3>{t}</h3><p>{p}</p></div>'

FOOTER = f'''<footer>
<div class="container">
<div class="footer-inner">
<div><div class="footer-logo"><img src="logo_telhados_renovados.jpg" alt="Telhados Renovados"></div>
<p class="footer-desc">Especialistas em telhados no Porto e Grande Porto há mais de 15 anos.</p></div>
<div><h4>Serviços</h4><ul>
<li><a href="instalacao-telhados.html">Instalação de Telhados</a></li>
<li><a href="remodelacao-telhados.html">Remodelação de Telhados</a></li>
<li><a href="reparacao-telhados.html">Reparação de Telhados</a></li>
<li><a href="sistemas-impermeabilizacao.html">Impermeabilização</a></li>
<li><a href="limpeza-telhados.html">Limpeza e Manutenção</a></li>
<li><a href="caleiras-rufagem.html">Caleiras e Rufagem</a></li>
</ul></div>
<div><h4>Contactos</h4><ul>
<li><a href="tel:+351937065056">+351 937 065 056</a></li>
<li><a href="mailto:contacto@telhadosrenovados.pt">contacto@telhadosrenovados.pt</a></li>
<li><a href="https://wa.me/351937065056" target="_blank">WhatsApp</a></li>
<li><span style="color:rgba(255,255,255,0.4)">Porto, Portugal</span></li>
</ul></div>
</div>
<div class="footer-bottom"><p>Copyright © 2026 Telhados Renovados – Todos os direitos reservados. Porto, Portugal.</p></div>
</div>
</footer>
<a id="mobile-wa-fab" href="https://wa.me/351937065056" target="_blank" aria-label="WhatsApp">
{WA_SVG}</a>'''

content = f'''<!DOCTYPE html>
<html lang="pt-PT">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Aplicação de Caleiras e Rufagem no Porto | Telhados Renovados</title>
<meta name="description" content="Instalação e substituição de caleiras, algerozes e rufagem no Porto. Sistemas em PVC, zinco e inox. Elimine infiltrações nas juntas do telhado. Orçamento gratuito. Tel: +351 937 065 056.">
<meta name="keywords" content="caleiras Porto, rufagem telhados Porto, algerozes Porto, substituição caleiras, impermeabilização juntas telhado">
<meta name="robots" content="index, follow">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
{SHARED_CSS}
</head>
<body>
{get_header('caleiras')}

<section class="page-hero">
<div style="position:absolute;inset:0;background-image:url('https://images.unsplash.com/photo-1600585154526-990dced4db0d?w=1600&q=80');background-size:cover;background-position:center;opacity:0.15;"></div>
<div class="container">
<nav class="breadcrumb">
<a href="index.html">Home</a><span>/</span><a href="#">Serviços</a><span>/</span>
<span style="color:rgba(255,255,255,0.9)">Caleiras e Rufagem</span>
</nav>
<h1>Aplicação de Caleiras e Rufagem<br><em>Proteção Duradoura para o seu Telhado</em></h1>
<p>Caleiras entupidas ou rufos mal aplicados causam infiltrações sérias nas paredes e fundações. Instalamos e substituímos sistemas de drenagem e rufagem com materiais de primeira qualidade no Porto e Grande Porto.</p>
<div class="hero-ctas">
<a href="tel:+351937065056" class="btn-primary">{PHONE_SVG} Ligar Agora</a>
<a href="https://wa.me/351937065056" target="_blank" class="btn-outline">{WA_SVG} WhatsApp</a>
</div>
</div>
</section>

<section class="section">
<div class="container">
<div class="two-col">
<div>
<span class="section-tag">Instalação Especializada</span>
<h2 class="section-title">Caleiras e Rufagem Bem Feitas Evitam Obras Caras</h2>
<p class="section-sub" style="margin-bottom:20px">As caleiras e o sistema de rufagem são os "guardiões silenciosos" do seu telhado. Quando falham, a água infiltra-se pelas paredes, corrói estruturas metálicas e provoca humidades que se alastram a toda a casa. No Porto, com a pluviosidade elevada, um sistema de drenagem eficiente é absolutamente essencial.</p>
<p class="section-sub">A Telhados Renovados instala sistemas de caleiras em PVC de alta resistência, zinco galvanizado e inox, com caimento calculado ao milímetro para garantir escoamento total sem estagnação. Todos os rufos são cortados e fixados com precisão para eliminar qualquer ponto de entrada de água.</p>
<div style="margin-top:28px"><a href="tel:+351937065056" class="btn-primary">Pedir Orçamento Gratuito</a></div>
</div>
<img src="https://images.unsplash.com/photo-1600585154526-990dced4db0d?w=800&q=80" alt="Instalação de caleiras no Porto" loading="lazy">
</div>
</div>
</section>

<section class="section gray">
<div class="container">
<div style="text-align:center;margin-bottom:8px"><span class="section-tag">O Que Fazemos</span></div>
<h2 class="section-title" style="text-align:center">Serviços Completos de Caleiras e Rufagem</h2>
<div class="features-grid">
{fc(icon('<rect x="3" y="3" width="18" height="18" rx="2"/><path d="M3 9h18"/>'), "Caleiras em PVC", "Instalação de caleiras em PVC de alta resistência UV, leveza e durabilidade comprovada. Disponível em várias cores.")}
{fc(icon('<path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/>'), "Caleiras em Zinco ou Inox", "Sistemas em zinco galvanizado ou inox para habitações de prestígio. Alta durabilidade e resistência ao clima do Porto.")}
{fc(icon('<path d="M3 9l9-7 9 7v11a2 2 0 01-2 2H5a2 2 0 01-2-2z"/>'), "Rufos e Frechais", "Corte e montagem precisa de rufos em chapa galvanizada ou alumínio nas encostas, paredes e mansardas.")}
{fc(icon('<path d="M20 14.66V20a2 2 0 01-2 2H4a2 2 0 01-2-2V6a2 2 0 012-2h5.34"/>'), "Desentupimento de Caleiras", "Limpeza e desentupimento completo de algerozes, ralos e tubos de queda bloqueados por folhas e sedimentos.")}
{fc(icon('<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>'), "Selagem de Juntas", "Aplicação de selantes de alta durabilidade em todas as juntas e conexões para estanquidade perfeita.")}
{fc(icon('<path d="M14 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V8z"/>'), "Garantia por Escrito", "Todos os trabalhos de instalação de caleiras e rufagem têm garantia de 5 anos documentada.")}
</div>
</div>
</section>

<section class="section">
<div class="container">
<div style="text-align:center;margin-bottom:8px"><span class="section-tag">Materiais Disponíveis</span></div>
<h2 class="section-title" style="text-align:center">Qual o Melhor Material para o seu Telhado?</h2>
<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:32px;margin-top:48px">
<div style="background:#fff;border-radius:16px;padding:32px;border:1px solid #e2e8f0;text-align:center">
<div style="font-size:2.5rem;margin-bottom:16px">🟦</div>
<h3 style="font-size:1.1rem;font-weight:800;color:#111d35;margin-bottom:10px">PVC</h3>
<p style="font-size:0.9rem;color:#64748b;line-height:1.6">Económico, leve e resistente à corrosão. Ideal para moradias e habitações. Várias cores disponíveis. Fácil manutenção.</p>
</div>
<div style="background:#fff;border-radius:16px;padding:32px;border:2px solid #c0392b;text-align:center;position:relative">
<div style="position:absolute;top:-12px;left:50%;transform:translateX(-50%);background:#c0392b;color:#fff;font-size:11px;font-weight:700;padding:4px 12px;border-radius:100px">MAIS POPULAR</div>
<div style="font-size:2.5rem;margin-bottom:16px">🔩</div>
<h3 style="font-size:1.1rem;font-weight:800;color:#111d35;margin-bottom:10px">Zinco Galvanizado</h3>
<p style="font-size:0.9rem;color:#64748b;line-height:1.6">Clássico e durável. Resistente ao clima húmido do Porto. Excelente relação qualidade/preço e grande durabilidade.</p>
</div>
<div style="background:#fff;border-radius:16px;padding:32px;border:1px solid #e2e8f0;text-align:center">
<div style="font-size:2.5rem;margin-bottom:16px">✨</div>
<h3 style="font-size:1.1rem;font-weight:800;color:#111d35;margin-bottom:10px">Inox</h3>
<p style="font-size:0.9rem;color:#64748b;line-height:1.6">Premium e eterno. A escolha para propriedades de luxo. Resistência absoluta à corrosão. Garantia de vida útil superior a 30 anos.</p>
</div>
</div>
</div>
</section>

<section class="section gray">
<div class="container">
<div style="text-align:center;margin-bottom:8px"><span class="section-tag">Como Trabalhamos</span></div>
<h2 class="section-title" style="text-align:center">Instalação de Caleiras em 4 Passos</h2>
<div class="process-steps">
{step(1, "Contacto e Visita", "Ligue ou envie mensagem pelo WhatsApp. Deslocamo-nos ao local para avaliar o sistema existente.")}
{step(2, "Escolha do Material", "Apresentamos as opções de material e preço, adaptadas ao seu telhado e ao seu orçamento.")}
{step(3, "Instalação Cuidada", "Remoção das antigas caleiras, cálculo do caimento ideal e montagem do novo sistema com precisão.")}
{step(4, "Teste e Garantia", "Testamos o sistema com água e entregamos garantia escrita de 5 anos sobre a instalação.")}
</div>
</div>
</section>

<section class="cta-band">
<div class="container">
<h2>Caleiras a precisar de substituição?</h2>
<p>Não espere pela próxima chuva forte. Contacte-nos para orçamento gratuito no Grande Porto.</p>
<div class="cta-buttons">
<a href="https://wa.me/351937065056" target="_blank" class="btn-wa">{WA_SVG} WhatsApp Agora</a>
<a href="tel:+351937065056" class="btn-call">{PHONE_SVG} +351 937 065 056</a>
<a href="mailto:contacto@telhadosrenovados.pt" class="btn-call">{EMAIL_SVG} contacto@telhadosrenovados.pt</a>
</div>
</div>
</section>

{FOOTER}
{SCRIPT}
</body>
</html>'''

filepath = os.path.join(OUTPUT_DIR, 'caleiras-rufagem.html')
with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print('Created: caleiras-rufagem.html')

# Also update inspecao-gratuita.html to redirect to caleiras-rufagem.html
redirect = '''<!DOCTYPE html>
<html lang="pt-PT">
<head>
<meta charset="UTF-8">
<meta http-equiv="refresh" content="0; url=caleiras-rufagem.html">
<title>Redirecionando...</title>
</head>
<body><a href="caleiras-rufagem.html">Clique aqui se não for redirecionado.</a></body>
</html>'''
with open(os.path.join(OUTPUT_DIR, 'inspecao-gratuita.html'), 'w', encoding='utf-8') as f:
    f.write(redirect)
print('Updated: inspecao-gratuita.html -> redirect to caleiras-rufagem.html')
