import os

OUTPUT_DIR = 'roovon_clone/newkit.creativemox.com/roovon'

def get_header(active_page=''):
    return f'''<!-- HEADER -->
<header id="custom-roovon-header">
    <div class="crh-container">
        <div class="crh-logo">
            <a href="index.html"><img src="logo_telhados_renovados.jpg" alt="Telhados Renovados Logo"></a>
        </div>
        <nav class="crh-nav">
            <ul class="crh-menu">
                <li><a href="index.html">Home</a></li>
                <li class="crh-has-dropdown">
                    <a href="#">Serviços <svg viewBox="0 0 320 512" width="10" height="10" style="margin-left:3px"><path fill="currentColor" d="M143 352.3L7 216.3c-9.4-9.4-9.4-24.6 0-33.9l22.6-22.6c9.4-9.4 24.6-9.4 33.9 0l96.4 96.4 96.4-96.4c9.4-9.4 24.6-9.4 33.9 0l22.6 22.6c9.4 9.4 9.4 24.6 0 33.9l-136 136c-9.2 9.4-24.4 9.4-33.8 0z"/></svg></a>
                    <ul class="crh-dropdown">
                        <li{"  class='active-page'" if active_page=="instalacao" else ""}><a href="instalacao-telhados.html">Instalação de Telhados e Coberturas</a></li>
                        <li{"  class='active-page'" if active_page=="remodelacao" else ""}><a href="remodelacao-telhados.html">Remodelação de Telhados</a></li>
                        <li{"  class='active-page'" if active_page=="reparacao" else ""}><a href="reparacao-telhados.html">Reparação de Telhados</a></li>
                        <li{"  class='active-page'" if active_page=="impermeabilizacao" else ""}><a href="sistemas-impermeabilizacao.html">Sistemas de Impermeabilização</a></li>
                        <li{"  class='active-page'" if active_page=="limpeza" else ""}><a href="limpeza-telhados.html">Limpeza e Manutenção</a></li>
                        <li{"  class='active-page'" if active_page=="inspecao" else ""}><a href="inspecao-gratuita.html">Inspeção Gratuita do Telhado</a></li>
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
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
:root { --navy: #111d35; --red: #c0392b; --green: #25D366; --gray: #64748b; --light: #f8fafc; --border: #e2e8f0; --text: #1e293b; }
html { overflow-x: hidden; scroll-behavior: smooth; }
body { font-family: 'Inter', sans-serif; color: var(--text); overflow-x: hidden; }
img { max-width: 100%; height: auto; }
#custom-roovon-header { background:#fff; position:fixed; top:0; left:0; right:0; z-index:99999; box-shadow:0 2px 10px rgba(0,0,0,0.05); overflow:visible; transition:box-shadow 0.3s; }
#custom-roovon-header.scrolled { box-shadow:0 2px 20px rgba(0,0,0,0.12); backdrop-filter:blur(8px); }
.crh-container { max-width:1250px; margin:0 auto; display:flex; align-items:center; justify-content:space-between; padding:4px 20px; overflow:visible; transition:padding 0.3s; }
#custom-roovon-header.scrolled .crh-container { padding:0 20px; }
.crh-logo { overflow:visible; display:flex; align-items:center; }
.crh-logo img { height:90px; width:auto; margin-top:20px; filter:drop-shadow(0 4px 6px rgba(0,0,0,0.18)); transition:height 0.35s,margin-top 0.35s; }
#custom-roovon-header.scrolled .crh-logo img { height:40px; margin-top:0; filter:none; }
.crh-menu { list-style:none; display:flex; gap:32px; align-items:center; }
.crh-menu a { text-decoration:none; color:#666; font-weight:700; font-size:14.5px; display:flex; align-items:center; padding:15px 0; transition:color 0.2s; }
.crh-menu > li > a:hover { color:#1a202c; }
.crh-has-dropdown { position:relative; }
.crh-dropdown { position:absolute; top:100%; left:0; background:#fff; min-width:280px; list-style:none; padding:0; box-shadow:0 4px 15px rgba(0,0,0,0.08); opacity:0; visibility:hidden; transform:translateY(10px); transition:all 0.2s; border-top:3px solid #0d2a45; }
.crh-has-dropdown:hover .crh-dropdown { opacity:1; visibility:visible; transform:translateY(0); }
.crh-dropdown a { color:#4a5568!important; font-weight:500!important; padding:15px 20px; display:block; font-size:14px; border-bottom:1px solid #f1f5f9; }
.crh-dropdown a:hover { color:#fff!important; background:#0d2a45!important; }
.crh-dropdown .active-page a { color:#fff!important; background:#c0392b!important; }
.crh-actions { display:flex; align-items:center; gap:12px; }
.crh-btn { display:flex; align-items:center; gap:8px; padding:8px 18px; font-weight:700; font-size:12px; border-radius:4px; text-decoration:none; transition:all 0.2s; text-transform:uppercase; }
.crh-btn-navy { background:#111d35!important; color:#fff!important; }
.crh-btn-whatsapp { background:#25D366!important; color:#fff!important; }
.crh-hamburger { display:none; flex-direction:column; gap:5px; background:none; border:none; cursor:pointer; padding:6px; }
.crh-hamburger span { display:block; width:24px; height:2px; background:#1a202c; border-radius:2px; transition:transform 0.3s,opacity 0.3s; }
.crh-hamburger.open span:nth-child(1) { transform:translateY(7px) rotate(45deg); }
.crh-hamburger.open span:nth-child(2) { opacity:0; }
.crh-hamburger.open span:nth-child(3) { transform:translateY(-7px) rotate(-45deg); }
.page-hero { padding-top:160px; background:linear-gradient(135deg,#0d2a45,#111d35 60%,#1a0a0a); padding-bottom:80px; position:relative; overflow:hidden; }
.page-hero::before { content:''; position:absolute; inset:0; opacity:0.15; background-size:cover; background-position:center; }
.page-hero .container { max-width:1200px; margin:0 auto; padding:0 24px; position:relative; z-index:1; }
.breadcrumb { display:flex; gap:8px; align-items:center; margin-bottom:20px; }
.breadcrumb a { color:rgba(255,255,255,0.6); font-size:13px; text-decoration:none; }
.breadcrumb span { color:rgba(255,255,255,0.4); font-size:13px; }
.page-hero h1 { color:#fff; font-size:clamp(2rem,5vw,3.2rem); font-weight:800; line-height:1.2; margin-bottom:20px; }
.page-hero h1 em { color:#c0392b; font-style:normal; }
.page-hero p { color:rgba(255,255,255,0.75); font-size:1.1rem; max-width:600px; line-height:1.7; margin-bottom:36px; }
.hero-ctas { display:flex; gap:16px; flex-wrap:wrap; }
.btn-primary { background:#c0392b; color:#fff; padding:16px 32px; border-radius:4px; font-weight:700; font-size:14px; text-decoration:none; text-transform:uppercase; transition:background 0.2s; display:inline-flex; align-items:center; gap:10px; }
.btn-primary:hover { background:#a93226; }
.btn-outline { border:2px solid rgba(255,255,255,0.4); color:#fff; padding:16px 32px; border-radius:4px; font-weight:700; font-size:14px; text-decoration:none; text-transform:uppercase; transition:all 0.2s; display:inline-flex; align-items:center; gap:10px; }
.btn-outline:hover { background:rgba(255,255,255,0.1); border-color:#fff; }
.section { padding:80px 0; }
.section.gray { background:var(--light); }
.container { max-width:1200px; margin:0 auto; padding:0 24px; }
.section-tag { display:inline-block; background:rgba(192,57,43,0.1); color:var(--red); font-size:12px; font-weight:700; text-transform:uppercase; letter-spacing:2px; padding:6px 14px; border-radius:100px; margin-bottom:14px; }
.section-title { font-size:clamp(1.6rem,4vw,2.4rem); font-weight:800; color:var(--navy); line-height:1.25; margin-bottom:16px; }
.section-sub { color:var(--gray); font-size:1.05rem; line-height:1.75; max-width:680px; }
.two-col { display:grid; grid-template-columns:1fr 1fr; gap:60px; align-items:center; }
.two-col img { border-radius:12px; box-shadow:0 8px 32px rgba(0,0,0,0.12); width:100%; height:380px; object-fit:cover; }
.features-grid { display:grid; grid-template-columns:repeat(3,1fr); gap:24px; margin-top:48px; }
.feature-card { background:#fff; border:1px solid var(--border); border-radius:12px; padding:28px; transition:box-shadow 0.2s,transform 0.2s; }
.feature-card:hover { box-shadow:0 8px 32px rgba(0,0,0,0.1); transform:translateY(-4px); }
.feature-icon { width:52px; height:52px; background:rgba(192,57,43,0.1); border-radius:10px; display:flex; align-items:center; justify-content:center; color:var(--red); margin-bottom:16px; }
.feature-card h3 { font-size:1rem; font-weight:700; color:var(--navy); margin-bottom:8px; }
.feature-card p { font-size:0.9rem; color:var(--gray); line-height:1.65; }
.process-steps { display:grid; grid-template-columns:repeat(4,1fr); gap:24px; margin-top:48px; }
.process-step { text-align:center; }
.step-num { width:56px; height:56px; background:var(--navy); color:#fff; border-radius:50%; display:flex; align-items:center; justify-content:center; font-size:1.4rem; font-weight:800; margin:0 auto 16px; }
.process-step h3 { font-size:1rem; font-weight:700; color:var(--navy); margin-bottom:8px; }
.process-step p { font-size:0.88rem; color:var(--gray); line-height:1.6; }
.cta-band { background:linear-gradient(135deg,var(--navy),#1e335e); padding:64px 0; text-align:center; }
.cta-band h2 { color:#fff; font-size:clamp(1.5rem,4vw,2.2rem); font-weight:800; margin-bottom:12px; }
.cta-band p { color:rgba(255,255,255,0.7); font-size:1rem; margin-bottom:32px; }
.cta-buttons { display:flex; gap:16px; justify-content:center; flex-wrap:wrap; }
.btn-wa { background:#25D366; color:#fff; padding:16px 32px; border-radius:4px; font-weight:700; font-size:14px; text-decoration:none; text-transform:uppercase; display:inline-flex; align-items:center; gap:10px; transition:background 0.2s; }
.btn-wa:hover { background:#20b858; }
.btn-call { background:rgba(255,255,255,0.1); border:2px solid rgba(255,255,255,0.3); color:#fff; padding:16px 32px; border-radius:4px; font-weight:700; font-size:14px; text-decoration:none; text-transform:uppercase; display:inline-flex; align-items:center; gap:10px; transition:all 0.2s; }
.btn-call:hover { background:rgba(255,255,255,0.2); }
footer { background:#05111f; color:rgba(255,255,255,0.6); padding:48px 0 24px; }
.footer-inner { display:grid; grid-template-columns:2fr 1fr 1fr; gap:40px; margin-bottom:36px; }
.footer-logo img { height:60px; margin-bottom:16px; }
.footer-desc { font-size:0.9rem; line-height:1.7; max-width:300px; }
footer h4 { color:#fff; font-size:0.95rem; font-weight:700; margin-bottom:16px; }
footer ul { list-style:none; }
footer ul li { margin-bottom:8px; }
footer ul li a { color:rgba(255,255,255,0.55); text-decoration:none; font-size:0.88rem; transition:color 0.2s; }
footer ul li a:hover { color:#fff; }
.footer-bottom { border-top:1px solid rgba(255,255,255,0.1); padding-top:24px; text-align:center; font-size:0.82rem; }
#mobile-wa-fab { position:fixed; bottom:22px; right:22px; width:56px; height:56px; background:#25D366; color:#fff; border-radius:50%; display:flex; align-items:center; justify-content:center; box-shadow:0 4px 16px rgba(37,211,102,0.45); z-index:999998; text-decoration:none; transition:transform 0.2s,box-shadow 0.2s; }
#mobile-wa-fab:hover { transform:scale(1.1); }
@media(max-width:900px) {
    .crh-hamburger{display:flex!important;}
    .crh-nav{display:none;width:100%;order:3;background:#fff;border-top:1px solid #f0f0f0;padding:8px 0;}
    .crh-nav.open{display:block;}
    .crh-menu{flex-direction:column;gap:0;width:100%;}
    .crh-menu>li>a{padding:12px 20px;border-bottom:1px solid #f5f5f5;}
    .crh-dropdown{position:static;box-shadow:none;opacity:1;visibility:visible;transform:none;display:none;border-left:3px solid #0d2a45;margin-left:20px;min-width:auto;}
    .crh-has-dropdown.open-mobile .crh-dropdown{display:block;}
    .crh-actions{display:none!important;}
    .crh-actions.open{display:flex!important;flex-direction:column;width:100%;padding:12px 16px;background:#fff;}
    .crh-logo img{height:55px;margin-top:8px;}
    .crh-container{flex-wrap:wrap;}
    .two-col{grid-template-columns:1fr;}
    .features-grid{grid-template-columns:1fr;}
    .process-steps{grid-template-columns:1fr 1fr;}
    .footer-inner{grid-template-columns:1fr;}
    #mobile-wa-fab{display:flex!important;}
}
@media(min-width:901px){#mobile-wa-fab{display:none!important;}}
@media(max-width:480px){.process-steps{grid-template-columns:1fr;}.page-hero{padding-top:130px;}}
</style>'''

SHARED_SCRIPT = '''<script>
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

FOOTER_HTML = '''<footer>
<div class="container">
<div class="footer-inner">
<div>
<div class="footer-logo"><img src="logo_telhados_renovados.jpg" alt="Telhados Renovados"></div>
<p class="footer-desc">Especialistas em instalação, reparação e manutenção de telhados no Porto e Grande Porto há mais de 15 anos.</p>
</div>
<div>
<h4>Serviços</h4>
<ul>
<li><a href="instalacao-telhados.html">Instalação de Telhados</a></li>
<li><a href="remodelacao-telhados.html">Remodelação de Telhados</a></li>
<li><a href="reparacao-telhados.html">Reparação de Telhados</a></li>
<li><a href="sistemas-impermeabilizacao.html">Impermeabilização</a></li>
<li><a href="limpeza-telhados.html">Limpeza e Manutenção</a></li>
<li><a href="inspecao-gratuita.html">Inspeção Gratuita</a></li>
</ul>
</div>
<div>
<h4>Contactos</h4>
<ul>
<li><a href="tel:+351937065056">+351 937 065 056</a></li>
<li><a href="mailto:contacto@telhadosrenovados.pt">contacto@telhadosrenovados.pt</a></li>
<li><a href="https://wa.me/351937065056" target="_blank">WhatsApp</a></li>
<li><span style="color:rgba(255,255,255,0.4)">Porto, Portugal</span></li>
</ul>
</div>
</div>
<div class="footer-bottom"><p>Copyright © 2026 Telhados Renovados – Todos os direitos reservados. Porto, Portugal.</p></div>
</div>
</footer>
<a id="mobile-wa-fab" href="https://wa.me/351937065056" target="_blank" aria-label="WhatsApp">
<svg viewBox="0 0 448 512" width="26" height="26"><path fill="currentColor" d="M380.9 97.1C339 55.1 283.2 32 223.9 32c-122.4 0-222 99.6-222 222 0 39.1 10.2 77.3 29.6 111L0 480l117.7-30.9c32.4 17.7 68.9 27 106.1 27h.1c122.3 0 224.1-99.6 224.1-222 0-59.3-23.2-115-65.1-157z"/></svg>
</a>'''

def icon(svg_path, size=26):
    return f'<svg viewBox="0 0 24 24" width="{size}" height="{size}" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">{svg_path}</svg>'

PHONE_ICON = icon('<path d="M22 16.92v3a2 2 0 01-2.18 2 19.79 19.79 0 01-8.63-3.07A19.5 19.5 0 013.07 10.8a19.79 19.79 0 01-3.07-8.68A2 2 0 012 0h3a2 2 0 012 1.72c.127.96.361 1.903.7 2.81a2 2 0 01-.45 2.11L6.09 7.91a16 16 0 006 6l1.27-1.27a2 2 0 012.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0122 14.92z"/>', 18)
WA_ICON = '<svg viewBox="0 0 448 512" width="16" height="16"><path fill="currentColor" d="M380.9 97.1C339 55.1 283.2 32 223.9 32c-122.4 0-222 99.6-222 222 0 39.1 10.2 77.3 29.6 111L0 480l117.7-30.9c32.4 17.7 68.9 27 106.1 27h.1c122.3 0 224.1-99.6 224.1-222 0-59.3-23.2-115-65.1-157z"/></svg>'
EMAIL_ICON = icon('<path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/>', 18)

def make_feature(icon_svg, title, text):
    return f'''<div class="feature-card">
<div class="feature-icon">{icon_svg}</div>
<h3>{title}</h3>
<p>{text}</p>
</div>'''

def make_step(num, title, text):
    return f'''<div class="process-step">
<div class="step-num">{num}</div>
<h3>{title}</h3>
<p>{text}</p>
</div>'''

def cta_section(title, desc):
    return f'''<section class="cta-band">
<div class="container">
<h2>{title}</h2>
<p>{desc}</p>
<div class="cta-buttons">
<a href="https://wa.me/351937065056" target="_blank" class="btn-wa">{WA_ICON} WhatsApp Agora</a>
<a href="tel:+351937065056" class="btn-call">{PHONE_ICON} +351 937 065 056</a>
<a href="mailto:contacto@telhadosrenovados.pt" class="btn-call">{EMAIL_ICON} contacto@telhadosrenovados.pt</a>
</div>
</div>
</section>'''

def page(title_tag, meta_desc, page_key, breadcrumb, h1, h1_em, hero_p, img_url,
         intro_tag, intro_h2, intro_p1, intro_p2,
         feat_tag, feat_h2, features,
         proc_tag, proc_h2, steps,
         cta_title, cta_desc):

    hero_bg = f'background-image:url("{img_url}");'

    return f'''<!DOCTYPE html>
<html lang="pt-PT">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title_tag} | Telhados Renovados</title>
<meta name="description" content="{meta_desc}">
<meta name="robots" content="index, follow">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
{SHARED_CSS}
</head>
<body>
{get_header(page_key)}
<section class="page-hero">
<div style="position:absolute;inset:0;{hero_bg}background-size:cover;background-position:center;opacity:0.15;"></div>
<div class="container">
<nav class="breadcrumb">
<a href="index.html">Home</a><span>/</span><a href="#">Serviços</a><span>/</span>
<span style="color:rgba(255,255,255,0.9)">{breadcrumb}</span>
</nav>
<h1>{h1}<br><em>{h1_em}</em></h1>
<p>{hero_p}</p>
<div class="hero-ctas">
<a href="tel:+351937065056" class="btn-primary">{PHONE_ICON} Ligar Agora</a>
<a href="https://wa.me/351937065056" target="_blank" class="btn-outline">{WA_ICON} WhatsApp</a>
</div>
</div>
</section>
<section class="section">
<div class="container">
<div class="two-col">
<div>
<span class="section-tag">{intro_tag}</span>
<h2 class="section-title">{intro_h2}</h2>
<p class="section-sub" style="margin-bottom:20px">{intro_p1}</p>
<p class="section-sub">{intro_p2}</p>
<div style="margin-top:28px"><a href="tel:+351937065056" class="btn-primary">Pedir Orçamento Gratuito</a></div>
</div>
<img src="{img_url}" alt="{breadcrumb} Porto" loading="lazy">
</div>
</div>
</section>
<section class="section gray">
<div class="container">
<div style="text-align:center;margin-bottom:8px"><span class="section-tag">{feat_tag}</span></div>
<h2 class="section-title" style="text-align:center">{feat_h2}</h2>
<div class="features-grid">{"".join(features)}</div>
</div>
</section>
<section class="section">
<div class="container">
<div style="text-align:center;margin-bottom:8px"><span class="section-tag">{proc_tag}</span></div>
<h2 class="section-title" style="text-align:center">{proc_h2}</h2>
<div class="process-steps">{"".join(steps)}</div>
</div>
</section>
{cta_section(cta_title, cta_desc)}
{FOOTER_HTML}
{SHARED_SCRIPT}
</body>
</html>'''

# =====================================================================
# PAGE 1: Remodelação de Telhados
# =====================================================================
p1 = page(
    title_tag="Remodelação de Telhados no Porto",
    meta_desc="Remodelação completa de telhados no Porto. Substituição de estrutura, novas telhas e isolamento. Orçamento gratuito. Tel: +351 937 065 056.",
    page_key="remodelacao",
    breadcrumb="Remodelação de Telhados",
    h1="Remodelação de Telhados",
    h1_em="com Qualidade e Garantia no Porto",
    hero_p="Dê uma nova vida ao seu telhado. Substituímos estruturas degradadas, renovamos a cobertura e melhoramos o isolamento térmico para mais conforto e poupança energética no Porto.",
    img_url="https://images.unsplash.com/photo-1581094794329-c8112a89af12?w=800&q=80",
    intro_tag="Renovação Total",
    intro_h2="Telhados Renovados de Raiz no Grande Porto",
    intro_p1="A remodelação do seu telhado é o investimento mais inteligente que pode fazer na conservação do seu imóvel. Um telhado degradado provoca humidades, perdas de calor e deterioração da estrutura — tudo isso tem solução com a Telhados Renovados.",
    intro_p2="Realizamos substituição completa da estrutura de madeira ou metálica, colocação de novas telhas e aplicação de isolamentos certificados. Trabalhamos em moradias, condomínios e espaços comerciais em todo o Porto e arredores.",
    feat_tag="O Que Fazemos",
    feat_h2="Serviços Completos de Remodelação",
    features=[
        make_feature(icon('<path d="M3 9l9-7 9 7v11a2 2 0 01-2 2H5a2 2 0 01-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/>'), "Substituição Total de Telhas", "Remoção das telhas antigas e colocação de telhas cerâmicas, betão ou painel, conforme a escolha."),
        make_feature(icon('<polygon points="12 2 2 7 12 12 22 7 12 2"/><polyline points="2 17 12 22 22 17"/><polyline points="2 12 12 17 22 12"/>'), "Renovação da Estrutura", "Diagnóstico e substituição de varas, caibros e madres em estado avançado de degradação."),
        make_feature(icon('<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>'), "Isolamento Térmico Melhorado", "Aplicação de isolamentos de alta eficiência para reduzir a fatura energética e melhorar o conforto interior."),
        make_feature(icon('<path d="M20.84 4.61a5.5 5.5 0 00-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 00-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 000-7.78z"/>'), "Impermeabilização Completa", "Instalação de tela impermeabilizante sob as telhas para eliminar definitivamente as infiltrações."),
        make_feature(icon('<rect x="3" y="3" width="18" height="18" rx="2"/><path d="M3 9h18M9 21V9"/>'), "Caleiras e Algerozes Novos", "Substituição ou instalação de sistemas de drenagem de água em PVC ou zinco com caimento correto."),
        make_feature(icon('<path d="M14 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V8z"/><polyline points="14 2 14 8 20 8"/>'), "Garantia Escrita 5 Anos", "Documentamos toda a obra com garantia formal de 5 anos sobre materiais e mão de obra."),
    ],
    proc_tag="Processo de Trabalho",
    proc_h2="Como Realizamos a sua Remodelação",
    steps=[
        make_step(1, "Contacto Inicial", "Ligue ou escreva pelo WhatsApp. Respondemos em menos de 2 horas nos dias úteis."),
        make_step(2, "Inspeção Gratuita", "Deslocamo-nos ao local para avaliar o estado do telhado e identificar todas as necessidades."),
        make_step(3, "Proposta Detalhada", "Recebe um orçamento discriminado por itens, sem custos ocultos ou surpresas."),
        make_step(4, "Obra e Entrega", "Executamos no prazo acordado, com equipa segurada e vistoria final conjunta."),
    ],
    cta_title="Pronto para remodelar o seu telhado?",
    cta_desc="Contacte-nos agora. Visita e orçamento gratuito em qualquer ponto do Grande Porto."
)

# =====================================================================
# PAGE 2: Reparação de Telhados
# =====================================================================
p2 = page(
    title_tag="Reparação de Telhados no Porto",
    meta_desc="Reparação urgente de telhados no Porto. Telhas partidas, infiltrações e humidades. Resposta rápida. Orçamento gratuito. Tel: +351 937 065 056.",
    page_key="reparacao",
    breadcrumb="Reparação de Telhados",
    h1="Reparação Urgente de Telhados",
    h1_em="Resposta Rápida no Porto",
    hero_p="Telha partida, infiltração ou dano causado por tempestade? A nossa equipa responde em urgência no Porto e Grande Porto para resolver o problema antes que cause mais estragos.",
    img_url="https://images.unsplash.com/photo-1590086782957-93c06ef21604?w=800&q=80",
    intro_tag="Reparação Profissional",
    intro_h2="Resolvemos Qualquer Problema de Telhado no Porto",
    intro_p1="Uma pequena infiltração pode tornar-se um problema grave em questão de horas. A Telhados Renovados oferece serviço de reparação rápida para minimizar os danos e devolver a proteção ao seu imóvel com qualidade certificada.",
    intro_p2="Reparamos telhas cerâmicas, de betão e painéis sanduíche. Colmatamos fissuras, corrigimos cumeeiras e criptas, substituímos rufos e selamos todas as juntas vulneráveis. Tudo com garantia por escrito.",
    feat_tag="Tipos de Reparação",
    feat_h2="Problemas que Resolvemos de Imediato",
    features=[
        make_feature(icon('<path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/>'), "Telhas Partidas ou Deslocadas", "Substituímos telhas danificadas por granizo, vento ou desgaste, repondo o alinhamento correto."),
        make_feature(icon('<path d="M20 14.66V20a2 2 0 01-2 2H4a2 2 0 01-2-2V6a2 2 0 012-2h5.34"/><polygon points="18 2 22 6 12 16 8 16 8 12 18 2"/>'), "Infiltrações e Humidades", "Localizamos e selamos a origem exata de cada infiltração, eliminando humidades no interior."),
        make_feature(icon('<path d="M3 9l9-7 9 7v11a2 2 0 01-2 2H5a2 2 0 01-2-2z"/>'), "Cumeeiras e Criptas", "Recimentação ou substituição de cumeeiras e criptas, pontos críticos de entrada de água."),
        make_feature(icon('<rect x="3" y="3" width="18" height="18" rx="2"/><path d="M3 9h18"/>'), "Rufos e Caleiras", "Reparação ou substituição de rufos, algerozes e tubos de queda danificados."),
        make_feature(icon('<circle cx="12" cy="12" r="10"/><line x1="4.93" y1="4.93" x2="19.07" y2="19.07"/>'), "Danos por Tempestade", "Atendimento urgente após intempéries. Colocação de proteções provisórias quando necessário."),
        make_feature(icon('<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>'), "Impermeabilização Pontual", "Aplicação de membranas e vedantes de alta durabilidade nas zonas mais vulneráveis."),
    ],
    proc_tag="Como Actuamos",
    proc_h2="Reparação Rápida em 4 Passos",
    steps=[
        make_step(1, "Contacto de Urgência", "Ligue agora ou envie foto pelo WhatsApp. Avaliamos a gravidade e damos resposta imediata."),
        make_step(2, "Deslocação ao Local", "A nossa equipa chega rapidamente ao local e faz um diagnóstico completo."),
        make_step(3, "Orçamento no Local", "Apresentamos o orçamento no próprio local, sem esperas ou burocracia."),
        make_step(4, "Reparação Garantida", "Executamos a reparação com qualidade e entregamos garantia escrita do trabalho."),
    ],
    cta_title="Telhado com problemas? Ligue agora!",
    cta_desc="Atendemos urgências em todo o Grande Porto. Orçamento gratuito e resposta rápida."
)

# =====================================================================
# PAGE 3: Sistemas de Impermeabilização
# =====================================================================
p3 = page(
    title_tag="Sistemas de Impermeabilização no Porto",
    meta_desc="Impermeabilização de telhados, terraços e paredes no Porto. Eliminação definitiva de infiltrações e humidades. Orçamento gratuito. Tel: +351 937 065 056.",
    page_key="impermeabilizacao",
    breadcrumb="Impermeabilização",
    h1="Sistemas de Impermeabilização",
    h1_em="Proteção Total contra Humidades no Porto",
    hero_p="Eliminamos definitivamente infiltrações em telhados, terraços, caves e paredes no Porto. Utilizamos sistemas de impermeabilização certificados com garantia até 10 anos de vida útil.",
    img_url="https://images.unsplash.com/photo-1504307651254-35680f356dfd?w=800&q=80",
    intro_tag="Impermeabilização Profissional",
    intro_h2="Diga Adeus às Humidades e Infiltrações",
    intro_p1="As humidades são um dos maiores inimigos do seu imóvel. Estragam paredes, tectos, estruturas metálicas e promovem o crescimento de fungos prejudiciais à saúde. A Telhados Renovados aplica sistemas de impermeabilização de alta performance que eliminam o problema na origem.",
    intro_p2="Trabalhamos com membranas asfálticas, telas EPDM, elastómeros líquidos e resinas de poliuretano — cada sistema escolhido ao milímetro conforme a superfície e a exposição. Garantia de 5 a 10 anos por escrito.",
    feat_tag="Sistemas Disponíveis",
    feat_h2="Impermeabilização para Cada Situação",
    features=[
        make_feature(icon('<path d="M20.84 4.61a5.5 5.5 0 00-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 00-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 000-7.78z"/>'), "Tela Asfáltica Termofusível", "Sistema clássico de alta durabilidade aplicado por chama, ideal para coberturas planas e terraços."),
        make_feature(icon('<circle cx="12" cy="12" r="10"/>'), "Elastómero Líquido (Membrana)", "Aplicação em frio por pintura, adapta-se a qualquer geometria. Excelente para terraços com sifões."),
        make_feature(icon('<polygon points="12 2 2 7 12 12 22 7 12 2"/>'), "Geotêxtil + PEAD", "Sistema multicamadas para terraços pisáveis e jardinados, com drenagem integrada."),
        make_feature(icon('<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>'), "Injeção em Paredes e Caves", "Tratamento de paredes enterradas e caves com injeção de resinas hidrofóbicas sob pressão."),
        make_feature(icon('<path d="M3 9l9-7 9 7v11a2 2 0 01-2 2H5a2 2 0 01-2-2z"/>'), "Coberturas Inclinadas", "Aplicação de subtelha impermeabilizante e rufagem em todas as juntas críticas do telhado."),
        make_feature(icon('<rect x="3" y="3" width="18" height="18" rx="2"/><path d="M3 9h18M9 21V9"/>'), "Garantia 5-10 Anos", "Certificamos o sistema aplicado com garantia de impermeabilidade por escrito."),
    ],
    proc_tag="O Nosso Processo",
    proc_h2="Impermeabilização em 4 Etapas",
    steps=[
        make_step(1, "Diagnóstico Gratuito", "Inspecionamos todas as superfícies e identificamos a origem e extensão das infiltrações."),
        make_step(2, "Escolha do Sistema", "Recomendamos o sistema mais eficiente e económico para a sua situação específica."),
        make_step(3, "Preparação da Superfície", "Limpeza, reparação de fissuras e aplicação do primário de penetração antes da impermeabilização."),
        make_step(4, "Aplicação e Garantia", "Impermeabilização executada por técnicos certificados, com teste de estanquidade e garantia."),
    ],
    cta_title="Problemas com humidades? Temos a solução!",
    cta_desc="Contacte-nos para uma inspeção gratuita. Atuamos em todo o Grande Porto com rapidez."
)

# =====================================================================
# PAGE 4: Limpeza e Manutenção
# =====================================================================
p4 = page(
    title_tag="Limpeza e Manutenção de Telhados no Porto",
    meta_desc="Limpeza profissional de telhados no Porto. Remoção de musgo, líquenes e sujidade. Tratamento antimosgo. Orçamento gratuito. Tel: +351 937 065 056.",
    page_key="limpeza",
    breadcrumb="Limpeza e Manutenção",
    h1="Limpeza e Manutenção",
    h1_em="de Telhados no Porto",
    hero_p="O musgo e os líquenes nas telhas retêm humidade e causam danos sérios à cobertura. A nossa limpeza profissional com tratamento antimosgo prolonga a vida útil do seu telhado por muitos anos.",
    img_url="https://images.unsplash.com/photo-1581578731548-c64695cc6952?w=800&q=80",
    intro_tag="Limpeza Especializada",
    intro_h2="Telhados Limpos duram muito mais tempo",
    intro_p1="O clima húmido do Porto favorece o crescimento de musgo, líquenes e outras colonizações biológicas sobre as telhas. Estes organismos retêm humidade, aceleram a deterioração da telha e provocam infiltrações. Uma limpeza anual ou bianual é o melhor investimento que pode fazer.",
    intro_p2="Utilizamos equipamentos profissionais de pressão regulada e produtos biocidas certificados e ecológicos. Após a limpeza, aplicamos tratamento preventivo antimosgo com duração de 2 a 5 anos, dependendo da exposição.",
    feat_tag="O Que Incluímos",
    feat_h2="Serviço Completo de Limpeza e Conservação",
    features=[
        make_feature(icon('<path d="M3 9l9-7 9 7v11a2 2 0 01-2 2H5a2 2 0 01-2-2z"/>'), "Remoção de Musgo e Líquenes", "Limpeza mecânica com alta pressão regulada para remover toda a cobertura biológica sem danificar as telhas."),
        make_feature(icon('<path d="M12 2.69l5.66 5.66a8 8 0 11-11.31 0z"/>'), "Tratamento Antimosgo", "Aplicação de produto biocida de longa duração que previne o reaparecimento do musgo por 2-5 anos."),
        make_feature(icon('<rect x="3" y="3" width="18" height="18" rx="2"/><path d="M3 9h18"/>'), "Limpeza de Caleiras", "Desentupimento e limpeza completa de algerozes, tubos de queda e ralos para escoamento correto."),
        make_feature(icon('<path d="M20 14.66V20a2 2 0 01-2 2H4a2 2 0 01-2-2V6a2 2 0 012-2h5.34"/>'), "Inspeção Preventiva", "Após a limpeza, fazemos vistoria ao estado geral do telhado e identificamos potenciais problemas futuros."),
        make_feature(icon('<circle cx="12" cy="12" r="10"/>'), "Tratamento de Cumeeiras", "Verificação e retoque de cumeeiras, criptas e rufos após a limpeza."),
        make_feature(icon('<path d="M14 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V8z"/>'), "Relatório de Estado", "Entregamos relatório com fotos antes/depois e recomendações de manutenção futura."),
    ],
    proc_tag="Como Limpamos",
    proc_h2="Limpeza Profissional em 4 Passos",
    steps=[
        make_step(1, "Contacto e Agendamento", "Marque a sua limpeza pelo telefone ou WhatsApp. Temos disponibilidade rápida."),
        make_step(2, "Aplicação Inicial", "Pré-tratamento com produto biocida para facilitar a remoção das colonizações."),
        make_step(3, "Lavagem Profissional", "Limpeza com equipamento de pressão regulada linha a linha, sem danificar as telhas."),
        make_step(4, "Tratamento Final", "Aplicação do produto preventivo antimosgo e entrega do relatório de estado."),
    ],
    cta_title="Telhado com musgo? Tratamos hoje!",
    cta_desc="Limpeza profissional com garantia no Porto e Grande Porto. Orçamento gratuito por WhatsApp."
)

# =====================================================================
# PAGE 5: Inspeção Gratuita
# =====================================================================
p5 = page(
    title_tag="Inspeção Gratuita de Telhados no Porto",
    meta_desc="Inspeção gratuita do seu telhado no Porto. Diagnóstico completo sem compromisso. Detectamos problemas antes que se agravem. Tel: +351 937 065 056.",
    page_key="inspecao",
    breadcrumb="Inspeção Gratuita",
    h1="Inspeção Gratuita",
    h1_em="ao seu Telhado no Porto",
    hero_p="Não espere que um pequeno problema se torne uma obra dispendiosa. Oferecemos inspeção gratuita e sem compromisso ao seu telhado, com relatório detalhado e recomendações profissionais.",
    img_url="https://images.unsplash.com/photo-1504307651254-35680f356dfd?w=800&q=80",
    intro_tag="Diagnóstico Gratuito",
    intro_h2="Conheça o Real Estado do seu Telhado",
    intro_p1="Muitos problemas de telhado evoluem silenciosamente durante meses ou anos antes de se tornarem visíveis. Uma infiltração pequena pode estar a deteriorar a estrutura de madeira ou as paredes interiores sem que perceba. A nossa inspeção gratuita dá-lhe tranquilidade e informação precisa.",
    intro_p2="O técnico deslocar-se-á ao local, inspeccionará a cobertura por completo e entregará um relatório fotográfico com a avaliação do estado geral e as intervenções recomendadas — sem qualquer custo ou obrigação de contratar.",
    feat_tag="O Que Inspecionamos",
    feat_h2="Avaliação Completa da sua Cobertura",
    features=[
        make_feature(icon('<path d="M3 9l9-7 9 7v11a2 2 0 01-2 2H5a2 2 0 01-2-2z"/>'), "Estado das Telhas", "Verificação individual das telhas, identificando partidas, deslocadas ou desgastadas."),
        make_feature(icon('<rect x="3" y="3" width="18" height="18" rx="2"/><path d="M3 9h18"/>'), "Caleiras e Drenagem", "Avaliação das caleiras, algerozes e tubos de queda para garantir escoamento eficiente."),
        make_feature(icon('<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>'), "Impermeabilização e Rufos", "Inspeção dos rufos, cumeeiras, criptas e zonas de impermeabilização."),
        make_feature(icon('<polygon points="12 2 2 7 12 12 22 7 12 2"/>'), "Estrutura de Suporte", "Avaliação visual da estrutura de madeira ou metálica quanto a deformações ou degradação."),
        make_feature(icon('<circle cx="12" cy="12" r="10"/>'), "Zonas de Infiltração", "Deteção de manchas de humidade, fungos e pontos de entrada de água."),
        make_feature(icon('<path d="M14 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V8z"/>'), "Relatório Fotográfico", "Entrega de relatório com fotos e recomendações escritas, totalmente gratuito e sem compromisso."),
    ],
    proc_tag="Como Funciona",
    proc_h2="Inspeção Gratuita em 4 Passos",
    steps=[
        make_step(1, "Solicite a Inspeção", "Contacte-nos pelo telefone ou WhatsApp e agende a visita gratuita."),
        make_step(2, "Deslocação Gratuita", "O nosso técnico desloca-se ao local sem qualquer custo para si."),
        make_step(3, "Inspeção Completa", "Avaliação minuciosa de todos os elementos da cobertura com registo fotográfico."),
        make_step(4, "Relatório e Proposta", "Recebe o relatório detalhado e, se necessário, uma proposta de intervenção sem obrigação."),
    ],
    cta_title="Peça já a sua inspeção gratuita!",
    cta_desc="100% gratuito e sem compromisso. Cobrimos todo o Grande Porto."
)

# Write all pages
pages = {
    'remodelacao-telhados.html': p1,
    'reparacao-telhados.html': p2,
    'sistemas-impermeabilizacao.html': p3,
    'limpeza-telhados.html': p4,
    'inspecao-gratuita.html': p5,
}

for filename, content in pages.items():
    filepath = os.path.join(OUTPUT_DIR, filename)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Created: {filename}')

print('\nAll 5 service pages created successfully!')
