html = '''<!DOCTYPE html>
<html lang="pt-PT">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Telhados Renovados - Instalação e Reparação de Telhados no Porto</title>
    <meta name="description" content="Especialistas em instalação, reparação e manutenção de telhados no Porto e Grande Porto. Orçamento gratuito em 24h.">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <style>
        *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
        :root {
            --navy: #111d35;
            --red: #c0392b;
            --green: #25D366;
            --gray: #64748b;
            --light-gray: #f8fafc;
            --border: #e2e8f0;
            --text: #1e293b;
        }
        html { overflow-x: hidden; scroll-behavior: smooth; }
        body { font-family: 'Inter', sans-serif; color: var(--text); overflow-x: hidden; background: var(--light-gray); }
        img { max-width: 100%; height: auto; }
        .container { max-width: 1200px; margin: 0 auto; padding: 0 24px; }

        /* HEADER */
        #custom-roovon-header {
            background: #fff; position: fixed; top: 0; left: 0; right: 0;
            z-index: 99999; box-shadow: 0 2px 10px rgba(0,0,0,0.05);
            transition: box-shadow 0.3s ease;
        }
        #custom-roovon-header.scrolled { box-shadow: 0 2px 20px rgba(0,0,0,0.12); }
        .crh-container {
            max-width: 1250px; margin: 0 auto;
            display: flex; align-items: center; justify-content: space-between;
            padding: 4px 20px; transition: padding 0.3s ease;
        }
        #custom-roovon-header.scrolled .crh-container { padding: 0px 20px; }
        .crh-logo img {
            height: 90px; margin-top: 20px;
            filter: drop-shadow(0 4px 6px rgba(0,0,0,0.18));
            transition: height 0.35s ease, margin-top 0.35s ease;
        }
        #custom-roovon-header.scrolled .crh-logo img { height: 40px; margin-top: 0; filter: none; }
        .crh-menu { list-style: none; display: flex; gap: 32px; align-items: center; }
        .crh-menu a { text-decoration: none; color: #666; font-weight: 700; font-size: 14.5px; padding: 15px 0; transition: color 0.2s; }
        .crh-menu > li > a:hover { color: #1a202c; }
        .crh-has-dropdown { position: relative; }
        .crh-dropdown {
            position: absolute; top: 100%; left: 0; background: #fff;
            min-width: 280px; list-style: none; padding: 0;
            box-shadow: 0 4px 15px rgba(0,0,0,0.08);
            opacity: 0; visibility: hidden; transform: translateY(10px);
            transition: all 0.2s ease; border-top: 3px solid #0d2a45;
        }
        .crh-has-dropdown:hover .crh-dropdown { opacity: 1; visibility: visible; transform: translateY(0); }
        .crh-dropdown a { color: #4a5568 !important; font-weight: 500 !important; padding: 15px 20px; display: block; border-bottom: 1px solid #f1f5f9; }
        .crh-dropdown a:hover { color: #fff !important; background: #0d2a45 !important; }
        .crh-actions { display: flex; align-items: center; gap: 12px; }
        .crh-btn { padding: 8px 18px; font-weight: 700; font-size: 12px; border-radius: 4px; text-decoration: none; transition: all 0.2s; text-transform: uppercase; }
        .crh-btn-navy { background: #111d35; color: #fff; }
        .crh-btn-whatsapp { background: #25D366; color: #fff; display: flex; align-items: center; gap: 8px; }

        /* HERO with SPLIT layout */
        .hero {
            padding-top: 150px; padding-bottom: 80px;
            background: linear-gradient(135deg, #0d2a45 0%, #111d35 60%, #1a0a0a 100%);
            position: relative; overflow: hidden; min-height: 90vh;
        }
        .hero::before {
            content: ''; position: absolute; inset: 0;
            background: url('img-instalacao.webp') center/cover; opacity: 0.15;
        }
        .hero .container { position: relative; z-index: 1; }
        .hero-split { display: grid; grid-template-columns: 1.1fr 0.9fr; gap: 60px; align-items: center; }
        
        .hero-text .hero-badge {
            display: inline-flex; align-items: center; gap: 8px;
            background: rgba(192,57,43,0.3); border: 1px solid rgba(192,57,43,0.5);
            color: #ffcccc; font-size: 12px; font-weight: 700; text-transform: uppercase;
            letter-spacing: 1.5px; padding: 6px 14px; border-radius: 100px; margin-bottom: 24px;
        }
        .hero-text h1 { color: #fff; font-size: clamp(2.2rem, 4vw, 3.5rem); font-weight: 800; line-height: 1.15; margin-bottom: 24px; text-wrap: balance; }
        .hero-text h1 em { color: #c0392b; font-style: normal; display: block; }
        .hero-text p { color: rgba(255,255,255,0.75); font-size: 1.15rem; line-height: 1.75; margin-bottom: 30px; max-width: 500px; }
        .hero-text .hero-tel { 
            display: inline-flex; align-items: center; gap: 12px;
            font-size: 1.2rem; font-weight: 800; color: #fff; background: rgba(255,255,255,0.1);
            padding: 12px 24px; border-radius: 100px; border: 1px solid rgba(255,255,255,0.2);
            text-decoration: none; transition: 0.2s;
        }
        .hero-text .hero-tel:hover { background: rgba(255,255,255,0.2); }

        /* HERO FORM BOX */
        .hero-form-box {
            background: #fff; border-radius: 16px; padding: 36px 30px;
            box-shadow: 0 20px 40px rgba(0,0,0,0.2);
        }
        .hero-form-box h3 { color: var(--navy); font-size: 1.6rem; font-weight: 800; text-align: center; margin-bottom: 24px; }
        .form-row { margin-bottom: 16px; }
        .form-row.half { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; }
        .form-row label { display: block; color: var(--gray); font-size: 13px; font-weight: 700; margin-bottom: 6px; }
        .form-row input, .form-row select, .form-row textarea {
            width: 100%; border: 1px solid #cbd5e1; border-radius: 6px; padding: 12px 14px;
            font-size: 14px; color: var(--navy); font-family: inherit; transition: 0.2s; background: #fff;
        }
        .form-row input:focus, .form-row select:focus, .form-row textarea:focus { outline: none; border-color: var(--navy); box-shadow: 0 0 0 3px rgba(17,29,53,0.1); }
        .form-row textarea { height: 80px; resize: vertical; }
        .btn-submit { width: 100%; background: var(--red); color: #fff; border: none; padding: 16px; border-radius: 6px; font-size: 16px; font-weight: 800; cursor: pointer; text-transform: uppercase; transition: background 0.2s; margin-top: 10px; }
        .btn-submit:hover { background: #a93226; }

        /* STATS BAR */
        .stats-bar { background: rgba(255,255,255,0.05); border-radius: 12px; padding: 28px 36px; display: grid; grid-template-columns: repeat(4,1fr); gap: 20px; margin-top: 40px; border: 1px solid rgba(255,255,255,0.08); }
        .stat-item { text-align: center; }
        .stat-num { color: #fff; font-size: 2rem; font-weight: 800; display: block; line-height: 1; }
        .stat-label { color: rgba(255,255,255,0.55); font-size: 0.8rem; margin-top: 6px; display: block; text-transform: uppercase; font-weight: 600; }

        /* SECTIONS */
        .section { padding: 90px 0; background: #fff; }
        .section-tag { display: inline-block; background: rgba(192,57,43,0.1); color: var(--red); font-size: 12px; font-weight: 800; text-transform: uppercase; letter-spacing: 2px; padding: 6px 14px; border-radius: 100px; margin-bottom: 16px; }
        .section-title { font-size: clamp(2rem, 4vw, 2.8rem); font-weight: 800; color: var(--navy); line-height: 1.2; margin-bottom: 20px; }
        .section-header { text-align: center; margin-bottom: 50px; max-width: 800px; margin-left: auto; margin-right: auto; }
        .section-header p { color: var(--gray); font-size: 1.1rem; line-height: 1.6; }

        /* SERVICES GRID */
        .services-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; }
        .service-card {
            background: #fff; border: 1px solid var(--border); border-radius: 14px;
            padding: 36px 30px; transition: all 0.3s; text-decoration: none; display: block;
            box-shadow: 0 4px 10px rgba(0,0,0,0.02);
        }
        .service-card:hover { box-shadow: 0 20px 40px rgba(0,0,0,0.08); transform: translateY(-6px); border-color: rgba(192,57,43,0.2); }
        .service-icon { width: 64px; height: 64px; background: rgba(192,57,43,0.08); border-radius: 14px; display: flex; align-items: center; justify-content: center; color: var(--red); margin-bottom: 24px; transition: 0.3s; }
        .service-card:hover .service-icon { background: var(--red); color: #fff; }
        .service-card h3 { font-size: 1.2rem; font-weight: 800; color: var(--navy); margin-bottom: 12px; }
        .service-card p { font-size: 0.95rem; color: var(--gray); line-height: 1.6; margin-bottom: 20px; }
        .service-link { color: var(--red); font-size: 0.9rem; font-weight: 700; display: flex; align-items: center; gap: 6px; }

        /* WHY US */
        .why-section { background: linear-gradient(135deg, #0d2a45, #111d35); padding: 90px 0; color: #fff; }
        .why-grid { display: grid; grid-template-columns: repeat(4,1fr); gap: 24px; margin-top: 50px; }
        .why-card { text-align: center; padding: 40px 24px; background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.08); border-radius: 16px; transition: 0.3s; }
        .why-card:hover { background: rgba(255,255,255,0.08); transform: translateY(-4px); }
        .why-card .icon { font-size: 2.8rem; margin-bottom: 20px; display: block; }
        .why-card h3 { font-size: 1.1rem; font-weight: 800; margin-bottom: 12px; }
        .why-card p { color: rgba(255,255,255,0.65); font-size: 0.9rem; line-height: 1.6; }

        /* CTA */
        .cta-band { background: #c0392b; padding: 60px 0; text-align: center; color: #fff; }
        .cta-band h2 { font-size: 2.2rem; font-weight: 800; margin-bottom: 20px; }
        .cta-band .btn-white { background: #fff; color: #c0392b; padding: 16px 32px; border-radius: 100px; font-weight: 800; text-decoration: none; display: inline-flex; align-items: center; gap: 10px; font-size: 15px; transition: 0.3s; }
        .cta-band .btn-white:hover { transform: scale(1.05); box-shadow: 0 10px 20px rgba(0,0,0,0.15); }

        /* FOOTER */
        footer { background: #05111f; color: rgba(255,255,255,0.6); padding: 70px 0 30px; }
        .footer-inner { display: grid; grid-template-columns: 2fr 1fr 1fr; gap: 50px; margin-bottom: 50px; }
        .footer-logo img { height: 60px; margin-bottom: 20px; }
        .footer-desc { font-size: 0.95rem; line-height: 1.7; max-width: 320px; margin-bottom: 24px; }
        footer h4 { color: #fff; font-size: 1.1rem; font-weight: 800; margin-bottom: 24px; }
        footer ul { list-style: none; }
        footer ul li { margin-bottom: 12px; }
        footer ul li a { color: rgba(255,255,255,0.6); text-decoration: none; font-size: 0.95rem; transition: 0.2s; }
        footer ul li a:hover { color: #fff; }
        .footer-bottom { border-top: 1px solid rgba(255,255,255,0.1); padding-top: 30px; text-align: center; font-size: 0.85rem; }
        .footer-legal { display: flex; gap: 24px; justify-content: center; margin-top: 16px; flex-wrap: wrap; }
        .footer-legal a { color: rgba(255,255,255,0.5); text-decoration: none; }
        .footer-legal a:hover { color: #fff; }

        /* RESPONSIVE */
        .crh-hamburger { display: none; background: none; border: none; cursor: pointer; padding: 6px; flex-direction: column; gap: 5px; }
        .crh-hamburger span { display: block; width: 24px; height: 2px; background: #1a202c; transition: 0.3s; }
        #mobile-wa-fab { position: fixed; bottom: 24px; right: 24px; width: 60px; height: 60px; background: #25D366; color: #fff; border-radius: 50%; display: none; align-items: center; justify-content: center; box-shadow: 0 4px 16px rgba(37,211,102,0.45); z-index: 999998; }

        @media (max-width: 900px) {
            .hero-split { grid-template-columns: 1fr; gap: 40px; }
            .hero { padding-top: 120px; text-align: center; }
            .hero-text p { margin: 0 auto 30px; }
            .stats-bar { grid-template-columns: 1fr 1fr; }
            .services-grid, .why-grid { grid-template-columns: 1fr; }
            .footer-inner { grid-template-columns: 1fr; text-align: center; }
            .footer-desc { margin: 0 auto 24px; }
            .crh-hamburger { display: flex; }
            .crh-nav { display: none; width: 100%; order: 3; background: #fff; border-top: 1px solid #f0f0f0; }
            .crh-nav.open { display: block; }
            .crh-menu { flex-direction: column; gap: 0; }
            .crh-menu > li > a { padding: 15px 20px; border-bottom: 1px solid #f5f5f5; }
            .crh-actions { display: none !important; }
            .crh-logo img { height: 50px; margin-top: 10px; }
            .crh-container { flex-wrap: wrap; }
            #mobile-wa-fab { display: flex; }
            .form-row.half { grid-template-columns: 1fr; }
        }
    </style>
</head>
<body>

<header id="custom-roovon-header">
    <div class="crh-container">
        <div class="crh-logo">
            <a href="index.html"><img src="logo_telhados_renovados.jpg" alt="Telhados Renovados Logo"></a>
        </div>
        <nav class="crh-nav">
            <ul class="crh-menu">
                <li><a href="index.html">Home</a></li>
                <li class="crh-has-dropdown">
                    <a href="#">Servi&ccedil;os <svg viewBox="0 0 320 512" width="10" height="10" style="margin-left:4px"><path fill="currentColor" d="M143 352.3L7 216.3c-9.4-9.4-9.4-24.6 0-33.9l22.6-22.6c9.4-9.4 24.6-9.4 33.9 0l96.4 96.4 96.4-96.4c9.4-9.4 24.6-9.4 33.9 0l22.6 22.6c9.4 9.4 9.4 24.6 0 33.9l-136 136c-9.2 9.4-24.4 9.4-33.8 0z"/></svg></a>
                    <ul class="crh-dropdown">
                        <li><a href="instalacao-telhados.html">Instala&ccedil;&atilde;o de Telhados</a></li>
                        <li><a href="remodelacao-telhados.html">Remodela&ccedil;&atilde;o de Telhados</a></li>
                        <li><a href="reparacao-telhados.html">Repara&ccedil;&atilde;o de Telhados</a></li>
                        <li><a href="sistemas-impermeabilizacao.html">Impermeabiliza&ccedil;&atilde;o</a></li>
                        <li><a href="limpeza-telhados.html">Limpeza e Manuten&ccedil;&atilde;o</a></li>
                        <li><a href="caleiras-rufagem.html">Caleiras e Rufagem</a></li>
                        <li><a href="inspecao-orcamentacao.html">Inspe&ccedil;&atilde;o Gratuita</a></li>
                    </ul>
                </li>
                <li><a href="contactos.html">Contactos</a></li>
            </ul>
        </nav>
        <div class="crh-actions">
            <a href="contactos.html" class="crh-btn crh-btn-navy">FA&Ccedil;A SEU OR&Ccedil;AMENTO</a>
            <a href="https://wa.me/351937065056" target="_blank" class="crh-btn crh-btn-whatsapp">
                <svg viewBox="0 0 448 512" width="14" height="14"><path fill="currentColor" d="M380.9 97.1C339 55.1 283.2 32 223.9 32c-122.4 0-222 99.6-222 222 0 39.1 10.2 77.3 29.6 111L0 480l117.7-30.9c32.4 17.7 68.9 27 106.1 27h.1c122.3 0 224.1-99.6 224.1-222 0-59.3-23.2-115-65.1-157z"/></svg>
                FALE NO WHATSAPP
            </a>
        </div>
        <button class="crh-hamburger" id="crh-hamburger"><span></span><span></span><span></span></button>
    </div>
</header>

<!-- HERO SPLIT -->
<section class="hero">
    <div class="container">
        <div class="hero-split">
            <div class="hero-text">
                <div class="hero-badge">Especialistas no Porto desde 2008</div>
                <h1>Telhados Seguros e Duradouros <em>para a Sua Casa</em></h1>
                <p>Instala&ccedil;&atilde;o, repara&ccedil;&atilde;o e manuten&ccedil;&atilde;o no Grande Porto. Pe&ccedil;a um or&ccedil;amento &agrave; nossa equipa certificada.</p>
                <a href="tel:+351937065056" class="hero-tel">
                    <svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 01-2.18 2 19.79 19.79 0 01-8.63-3.07A19.5 19.5 0 013.07 10.8a19.79 19.79 0 01-3.07-8.68A2 2 0 012 0h3a2 2 0 012 1.72c.127.96.361 1.903.7 2.81a2 2 0 01-.45 2.11L6.09 7.91a16 16 0 006 6l1.27-1.27a2 2 0 012.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0122 14.92z"/></svg>
                    937 065 056
                </a>
                
                <div class="stats-bar">
                    <div class="stat-item"><span class="stat-num">+15</span><span class="stat-label">Anos Experi&ecirc;ncia</span></div>
                    <div class="stat-item"><span class="stat-num">500+</span><span class="stat-label">Projetos Feitos</span></div>
                    <div class="stat-item"><span class="stat-num">5 Anos</span><span class="stat-label">Garantia Escrita</span></div>
                    <div class="stat-item"><span class="stat-num">24H</span><span class="stat-label">Or&ccedil;amento Gr&aacute;tis</span></div>
                </div>
            </div>
            
            <div class="hero-form-box">
                <h3>Pe&ccedil;a j&aacute; um or&ccedil;amento gratuito!</h3>
                <script>var sb_orc=false;</script>
                <iframe name="hframe_orc" id="hframe_orc" style="display:none;" onload="if(sb_orc){document.getElementById('r_orc').innerHTML='<div style=&quot;padding:15px;background:#d4edda;color:#155724;border-radius:6px;margin-top:12px;font-weight:700;text-align:center;&quot;>&#10003; Pedido enviado! Entramos em contacto brevemente.</div>';document.getElementById('form_orc').reset();}"></iframe>
                <form id="form_orc" action="https://script.google.com/macros/s/AKfycbxwzOED42-82fwCVNUV6XSiHVHDCNJcr-7xWCpWzqjImqZKCUkapHEghToBEEV6pkmT/exec" target="hframe_orc" method="POST" onsubmit="sb_orc=true;">
                    <div class="form-row">
                        <label>Nome:</label>
                        <input type="text" name="nome" required>
                    </div>
                    <div class="form-row">
                        <label>Tipo Cliente:</label>
                        <select name="tipo_cliente" required>
                            <option value="" disabled selected>Escolha uma op&ccedil;&atilde;o</option>
                            <option>Particular</option>
                            <option>Condom&iacute;nio</option>
                            <option>Empresa</option>
                        </select>
                    </div>
                    <div class="form-row">
                        <label>Problema:</label>
                        <select name="problema" required>
                            <option value="" disabled selected>Escolha uma op&ccedil;&atilde;o</option>
                            <option>Substitui&ccedil;&atilde;o de Telhado</option>
                            <option>Limpeza / Impermeabiliza&ccedil;&atilde;o</option>
                            <option>Isolamento T&eacute;rmico (Roofmate)</option>
                            <option>Infiltra&ccedil;&atilde;o no Telhado</option>
                            <option>PLADUR e/ou Pintura Interior</option>
                        </select>
                    </div>
                    <div class="form-row half">
                        <div>
                            <label>Localidade:</label>
                            <input type="text" name="localidade" required>
                        </div>
                        <div>
                            <label>Telem&oacute;vel:</label>
                            <input type="tel" name="telemovel" pattern="[0-9()#&amp;+*=.-]+" required>
                        </div>
                    </div>
                    <div class="form-row">
                        <label>Detalhes adicionais:</label>
                        <textarea name="detalhes"></textarea>
                    </div>
                    <button type="submit" class="btn-submit">Pedir Or&ccedil;amento Gr&aacute;tis</button>
                    <div id="r_orc"></div>
                </form>
            </div>
        </div>
    </div>
</section>

<!-- SERVICES -->
<section class="section">
    <div class="container">
        <div class="section-header">
            <span class="section-tag">Os Nossos Servi&ccedil;os</span>
            <h2 class="section-title">Solu&ccedil;&otilde;es Completas para o seu Telhado no Porto</h2>
            <p>Desde a constru&ccedil;&atilde;o de telhados novos &agrave; repara&ccedil;&atilde;o r&aacute;pida de infiltra&ccedil;&otilde;es, atuamos com rapidez e garantia de qualidade total em todos os nossos servi&ccedil;os.</p>
        </div>
        
        <div class="services-grid">
            <a href="instalacao-telhados.html" class="service-card">
                <div class="service-icon"><svg viewBox="0 0 24 24" width="30" height="30" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 9l9-7 9 7v11a2 2 0 01-2 2H5a2 2 0 01-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg></div>
                <h3>Instala&ccedil;&atilde;o de Telhados</h3>
                <p>Constru&ccedil;&atilde;o e substitui&ccedil;&atilde;o de telhados completos com materiais r&uacute;sticos, lusa ou painel sand&uacute;iche.</p>
                <span class="service-link">Saber mais &rarr;</span>
            </a>
            <a href="reparacao-telhados.html" class="service-card">
                <div class="service-icon"><svg viewBox="0 0 24 24" width="30" height="30" fill="none" stroke="currentColor" stroke-width="2"><path d="M14.7 6.3a1 1 0 000 1.4l1.6 1.6a1 1 0 001.4 0l3.77-3.77a6 6 0 01-7.94 7.94l-6.91 6.91a2.12 2.12 0 01-3-3l6.91-6.91a6 6 0 017.94-7.94l-3.76 3.76z"/></svg></div>
                <h3>Repara&ccedil;&atilde;o de Infiltra&ccedil;&otilde;es</h3>
                <p>Identifica&ccedil;&atilde;o e corre&ccedil;&atilde;o r&aacute;pida de fissuras, telhas m&oacute;veis e humidades no interior da sua habita&ccedil;&atilde;o.</p>
                <span class="service-link">Saber mais &rarr;</span>
            </a>
            <a href="sistemas-impermeabilizacao.html" class="service-card">
                <div class="service-icon"><svg viewBox="0 0 24 24" width="30" height="30" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2.69l5.66 5.66a8 8 0 11-11.31 0z"/></svg></div>
                <h3>Impermeabiliza&ccedil;&atilde;o</h3>
                <p>Aplica&ccedil;&atilde;o de telas asf&aacute;lticas, membranas l&iacute;quidas e poliuretano para lajes e terra&ccedil;os sem fugas.</p>
                <span class="service-link">Saber mais &rarr;</span>
            </a>
            <a href="limpeza-telhados.html" class="service-card">
                <div class="service-icon"><svg viewBox="0 0 24 24" width="30" height="30" fill="none" stroke="currentColor" stroke-width="2"><path d="M20.84 4.61a5.5 5.5 0 00-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 00-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 000-7.78z"/></svg></div>
                <h3>Limpeza e Manuten&ccedil;&atilde;o</h3>
                <p>Lavagem a alta press&atilde;o, remo&ccedil;&atilde;o de fungos/verdete e aplica&ccedil;&atilde;o de antifungos de longa dura&ccedil;&atilde;o.</p>
                <span class="service-link">Saber mais &rarr;</span>
            </a>
            <a href="remodelacao-telhados.html" class="service-card">
                <div class="service-icon"><svg viewBox="0 0 24 24" width="30" height="30" fill="none" stroke="currentColor" stroke-width="2"><polyline points="23 4 23 10 17 10"/><path d="M20.49 15a9 9 0 11-2.12-9.36L23 10"/></svg></div>
                <h3>Isolamento T&eacute;rmico</h3>
                <p>Aplica&ccedil;&atilde;o de v&aacute;rias camadas de espuma Roofmate para estancar calores extremos ou perdas t&eacute;rmicas.</p>
                <span class="service-link">Saber mais &rarr;</span>
            </a>
            <a href="inspecao-orcamentacao.html" class="service-card">
                <div class="service-icon"><svg viewBox="0 0 24 24" width="30" height="30" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg></div>
                <h3>Inspe&ccedil;&atilde;o e Or&ccedil;amentos</h3>
                <p>Desloca&ccedil;&atilde;o ao local, recolha de medidas, avalia&ccedil;&atilde;o estrutural e or&ccedil;amenta&ccedil;&atilde;o 100% gratuita.</p>
                <span class="service-link">Saber mais &rarr;</span>
            </a>
        </div>
    </div>
</section>

<!-- WHY US -->
<section class="why-section">
    <div class="container">
        <div class="section-header" style="margin-bottom:30px">
            <span class="section-tag" style="background:rgba(255,255,255,0.1);color:#fff">O Nosso Compromisso</span>
            <h2 class="section-title" style="color:#fff">Porque escolher a Telhados Renovados?</h2>
        </div>
        <div class="why-grid">
            <div class="why-card">
                <span class="icon">&#127919;</span>
                <h3>Profissionais Qualificados</h3>
                <p>Equipas s&eacute;rias e experientes no tratamento e restauro de im&oacute;veis portuenses.</p>
            </div>
            <div class="why-card">
                <span class="icon">&#128196;</span>
                <h3>Garantia Escrita</h3>
                <p>Todos os projetos incluem contrato de garantia at&eacute; 10 anos sobes os materiais e a m&atilde;o de obra.</p>
            </div>
            <div class="why-card">
                <span class="icon">&#9200;</span>
                <h3>Rapidez e Efici&ecirc;ncia</h3>
                <p>Respondemos &agrave; sua chamada e marcamos uma visita para or&ccedil;amento no prazo de 24 horas &uacute;teis.</p>
            </div>
            <div class="why-card">
                <span class="icon">&#128081;</span>
                <h3>Materiais Premium</h3>
                <p>Utilizamos exclusivamente fornecedores certificados de qualidade comprovada e dur&aacute;vel.</p>
            </div>
        </div>
    </div>
</section>

<!-- CTA BAND -->
<section class="cta-band">
    <div class="container">
        <h2>Tem telhas partidas ou pingas no teto?</h2>
        <p style="margin-bottom:30px; font-size:1.1rem">Atuamos de imediato no Porto, Maia, Matosinhos, Gaia, Valongo e Gondomar.</p>
        <a href="https://wa.me/351937065056" target="_blank" class="btn-white">
            <svg viewBox="0 0 448 512" width="20" height="20"><path fill="currentColor" d="M380.9 97.1C339 55.1 283.2 32 223.9 32c-122.4 0-222 99.6-222 222 0 39.1 10.2 77.3 29.6 111L0 480l117.7-30.9c32.4 17.7 68.9 27 106.1 27h.1c122.3 0 224.1-99.6 224.1-222 0-59.3-23.2-115-65.1-157z"/></svg>
            Agendar Visita Agora
        </a>
    </div>
</section>

<!-- FOOTER -->
<footer>
    <div class="container">
        <div class="footer-inner">
            <div>
                <img src="logo_telhados_renovados.jpg" alt="Telhados Renovados" style="height:60px;margin-bottom:20px; border-radius:4px;">
                <p class="footer-desc">Especialistas na constru&ccedil;&atilde;o e repara&ccedil;&atilde;o t&eacute;cnica de telhados para lares confort&aacute;veis.</p>
                <a href="tel:+351937065056" style="color:#fff; font-weight:800; text-decoration:none; font-size:1.2rem; display:block; margin-bottom:10px">+351 937 065 056</a>
                <a href="mailto:contacto@telhadosrenovados.pt" style="color:rgba(255,255,255,0.7); text-decoration:none;">contacto@telhadosrenovados.pt</a>
            </div>
            <div>
                <h4>As Nossas Especialidades</h4>
                <ul>
                    <li><a href="instalacao-telhados.html">Instala&ccedil;&atilde;o de Telhados Pr&oacute;</a></li>
                    <li><a href="reparacao-telhados.html">Repara&ccedil;&atilde;o de Infiltra&ccedil;&otilde;es</a></li>
                    <li><a href="remodelacao-telhados.html">Isolamento T&eacute;rmico</a></li>
                    <li><a href="sistemas-impermeabilizacao.html">Impermeabiliza&ccedil;&atilde;o de Terra&ccedil;os</a></li>
                    <li><a href="limpeza-telhados.html">Limpeza &amp; Conserva&ccedil;&atilde;o</a></li>
                </ul>
            </div>
            <div>
                <h4>&Aacute;rea de Atua&ccedil;&atilde;o</h4>
                <ul>
                    <li><span style="color:rgba(255,255,255,0.6)">Porto Centro</span></li>
                    <li><span style="color:rgba(255,255,255,0.6)">Vila Nova de Gaia</span></li>
                    <li><span style="color:rgba(255,255,255,0.6)">Matosinhos</span></li>
                    <li><span style="color:rgba(255,255,255,0.6)">Maia</span></li>
                    <li><span style="color:rgba(255,255,255,0.6)">Valongo &amp; Gondomar</span></li>
                </ul>
            </div>
        </div>
        <div class="footer-bottom">
            <p>&copy; 2026 Telhados Renovados &ndash; Todos os direitos reservados. &nbsp;|&nbsp; Desenvolvido por <a href="https://foturemkt.com/" target="_blank" style="color:var(--gray);text-decoration:none;font-weight:700;">Foture Mkt</a></p>
            <div class="footer-legal">
                <a href="politica-de-privacidade.html">Pol&iacute;tica de Privacidade</a>
                <a href="termos-e-condicoes.html">Termos e Condi&ccedil;&otilde;es</a>
                <a href="politica-de-cookies.html">Cookies</a>
                <a href="politica-de-garantia.html">Garantia</a>
            </div>
        </div>
    </div>
</footer>

<a id="mobile-wa-fab" href="https://wa.me/351937065056" target="_blank">
    <svg viewBox="0 0 448 512" width="28" height="28"><path fill="currentColor" d="M380.9 97.1C339 55.1 283.2 32 223.9 32c-122.4 0-222 99.6-222 222 0 39.1 10.2 77.3 29.6 111L0 480l117.7-30.9c32.4 17.7 68.9 27 106.1 27h.1c122.3 0 224.1-99.6 224.1-222 0-59.3-23.2-115-65.1-157z"/></svg>
</a>

<script>
    var header = document.getElementById('custom-roovon-header');
    var hamburger = document.getElementById('crh-hamburger');
    var nav = document.querySelector('.crh-nav');
    window.addEventListener('scroll', function() { header.classList.toggle('scrolled', window.scrollY > 40); }, {passive: true});
    hamburger.addEventListener('click', function() { nav.classList.toggle('open'); hamburger.classList.toggle('open'); });
</script>
</body>
</html>'''

with open("roovon_clone/newkit.creativemox.com/roovon/index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Novo index.html Híbrido GERADO COM SUCESSO!")
