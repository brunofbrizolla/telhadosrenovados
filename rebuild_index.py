
html = '''<!DOCTYPE html>
<html lang="pt-PT">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Telhados Renovados - Instalação e Reparação de Telhados no Porto</title>
    <meta name="description" content="Especialistas em instalação, reparação e manutenção de telhados no Porto e Grande Porto. Orçamento gratuito em 24h. Ligue: +351 937 065 056.">
    <meta name="keywords" content="telhados Porto, reparação telhados Porto, instalação telhados, impermeabilização, telhados renovados">
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="https://www.telhadosrenovados.pt/">
    <meta property="og:title" content="Telhados Renovados - Especialistas em Telhados no Porto">
    <meta property="og:description" content="Instalação, reparação e manutenção de telhados no Porto. Orçamento gratuito em 24h.">
    <meta property="og:type" content="website">
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
        body { font-family: \'Inter\', sans-serif; color: var(--text); overflow-x: hidden; }
        img { max-width: 100%; height: auto; }

        /* HEADER */
        #custom-roovon-header {
            background: #fff; position: fixed; top: 0; left: 0; right: 0;
            z-index: 99999; box-shadow: 0 2px 10px rgba(0,0,0,0.05);
            transition: box-shadow 0.3s ease; overflow: visible;
        }
        #custom-roovon-header.scrolled { box-shadow: 0 2px 20px rgba(0,0,0,0.12); }
        .crh-container {
            max-width: 1250px; margin: 0 auto;
            display: flex; align-items: center; justify-content: space-between;
            padding: 4px 20px; overflow: visible; transition: padding 0.3s ease;
        }
        #custom-roovon-header.scrolled .crh-container { padding: 0px 20px; }
        .crh-logo { display: flex; align-items: center; overflow: visible; }
        .crh-logo img {
            height: 90px; width: auto; margin-top: 20px;
            filter: drop-shadow(0 4px 6px rgba(0,0,0,0.18));
            transition: height 0.35s ease, margin-top 0.35s ease;
        }
        #custom-roovon-header.scrolled .crh-logo img { height: 40px; margin-top: 0; filter: none; }
        .crh-menu { list-style: none; display: flex; gap: 32px; align-items: center; }
        .crh-menu a { text-decoration: none; color: #666; font-weight: 700; font-size: 14.5px; display: flex; align-items: center; padding: 15px 0; transition: color 0.2s; }
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
        .crh-dropdown a { color: #4a5568 !important; font-weight: 500 !important; padding: 15px 20px; display: block; font-size: 14px; border-bottom: 1px solid #f1f5f9; }
        .crh-dropdown a:hover { color: #fff !important; background: #0d2a45 !important; }
        .crh-actions { display: flex; align-items: center; gap: 12px; }
        .crh-btn { display: flex; align-items: center; justify-content: center; gap: 8px; padding: 8px 18px; font-weight: 700; font-size: 12px; border-radius: 4px; text-decoration: none; transition: all 0.2s; text-transform: uppercase; }
        .crh-btn-navy { background: #111d35 !important; color: #fff !important; }
        .crh-btn-navy:hover { background: #1e335e !important; }
        .crh-btn-whatsapp { background: #25D366 !important; color: #fff !important; }
        .crh-btn-whatsapp:hover { background: #20b858 !important; }

        /* HERO */
        .hero {
            padding-top: 150px; padding-bottom: 80px;
            background: linear-gradient(135deg, #0d2a45 0%, #111d35 60%, #1a0a0a 100%);
            position: relative; overflow: hidden; min-height: 90vh;
            display: flex; align-items: center;
        }
        .hero::before {
            content: ''; position: absolute; inset: 0;
            background: url('img-instalacao.webp') center/cover; opacity: 0.13;
        }
        .hero .container { position: relative; z-index: 1; }
        
        .hero-layout { display: grid; grid-template-columns: 1.2fr 0.8fr; gap: 40px; align-items: center; }
        
        .hero-badge {
            display: inline-flex; align-items: center; gap: 8px;
            background: rgba(192,57,43,0.2); border: 1px solid rgba(192,57,43,0.4);
            color: #f4a4a4; font-size: 12px; font-weight: 700; text-transform: uppercase;
            letter-spacing: 1.5px; padding: 6px 14px; border-radius: 100px; margin-bottom: 24px;
        }
        .hero h1 { color: #fff; font-size: clamp(1.8rem, 4.5vw, 3.2rem); font-weight: 800; line-height: 1.15; margin-bottom: 24px; }
        .hero h1 em { color: #c0392b; font-style: normal; display: block; }
        .hero p { color: rgba(255,255,255,0.72); font-size: 1.05rem; max-width: 580px; line-height: 1.7; margin-bottom: 30px; }
        .hero-ctas { display: flex; gap: 12px; flex-wrap: wrap; margin-bottom: 40px; }
        
        /* HERO FORM */
        .hero-form-box { background: rgba(255,255,255,0.05); backdrop-filter: blur(10px); border: 1px solid rgba(255,255,255,0.1); border-radius: 16px; padding: 30px; box-shadow: 0 20px 50px rgba(0,0,0,0.3); }
        .hero-form-box h3 { color: #fff; font-size: 1.3rem; font-weight: 800; margin-bottom: 15px; text-align: center; }
        .hero-form-box .form-row { margin-bottom: 12px; }
        .hero-form-box .form-row label { font-size: 11px; margin-bottom: 4px; }
        .hero-form-box input, .hero-form-box select { padding: 11px 14px; font-size: 14px; }
        .hero-form-box .btn-submit { padding: 14px; font-size: 14px; }

        @media (max-width: 1000px) {
            .hero-layout { grid-template-columns: 1fr; text-align: center; }
            .hero h1 { margin-left: auto; margin-right: auto; }
            .hero p { margin-left: auto; margin-right: auto; }
            .hero-ctas { justify-content: center; }
            .hero-badge { justify-content: center; }
            .stats-bar { margin: 40px auto 0; }
        }

        /* STATS BAR */
        .stats-bar { background: rgba(255,255,255,0.06); border: 1px solid rgba(255,255,255,0.1); border-radius: 12px; padding: 28px 36px; display: grid; grid-template-columns: repeat(4,1fr); gap: 20px; max-width: 740px; }
        .stat-item { text-align: center; }
        .stat-num { color: #fff; font-size: 2rem; font-weight: 800; display: block; line-height: 1; }
        .stat-label { color: rgba(255,255,255,0.55); font-size: 0.8rem; margin-top: 4px; display: block; }

        /* BUTTONS */
        .btn-primary { background: #c0392b; color: #fff; padding: 16px 32px; border-radius: 4px; font-weight: 700; font-size: 14px; text-decoration: none; text-transform: uppercase; transition: background 0.2s; display: inline-flex; align-items: center; gap: 10px; }
        .btn-primary:hover { background: #a93226; }
        .btn-outline { border: 2px solid rgba(255,255,255,0.35); color: #fff; padding: 16px 32px; border-radius: 4px; font-weight: 700; font-size: 14px; text-decoration: none; text-transform: uppercase; transition: all 0.2s; display: inline-flex; align-items: center; gap: 10px; }
        .btn-outline:hover { background: rgba(255,255,255,0.1); border-color: #fff; }
        .btn-wa { background: #25D366; color: #fff; padding: 16px 32px; border-radius: 4px; font-weight: 700; font-size: 14px; text-decoration: none; text-transform: uppercase; display: inline-flex; align-items: center; gap: 10px; transition: background 0.2s; }
        .btn-wa:hover { background: #20b858; }
        .btn-call { background: rgba(255,255,255,0.1); border: 2px solid rgba(255,255,255,0.3); color: #fff; padding: 16px 32px; border-radius: 4px; font-weight: 700; font-size: 14px; text-decoration: none; text-transform: uppercase; display: inline-flex; align-items: center; gap: 10px; transition: all 0.2s; }
        .btn-call:hover { background: rgba(255,255,255,0.2); }

        /* SECTIONS */
        .section { padding: 88px 0; }
        .section.gray { background: var(--light-gray); }
        .container { max-width: 1200px; margin: 0 auto; padding: 0 24px; }
        .section-tag { display: inline-block; background: rgba(192,57,43,0.1); color: var(--red); font-size: 12px; font-weight: 700; text-transform: uppercase; letter-spacing: 2px; padding: 6px 14px; border-radius: 100px; margin-bottom: 14px; }
        .section-title { font-size: clamp(1.7rem, 4vw, 2.5rem); font-weight: 800; color: var(--navy); line-height: 1.2; margin-bottom: 16px; }
        .section-sub { color: var(--gray); font-size: 1.05rem; line-height: 1.75; max-width: 640px; }

        /* SERVICES GRID */
        .services-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; margin-top: 48px; }
        .service-card {
            background: #fff; border: 1px solid var(--border); border-radius: 14px;
            padding: 32px 28px; transition: box-shadow 0.25s, transform 0.25s; text-decoration: none; display: block;
            position: relative; overflow: hidden;
        }
        .service-card::after { content: \'\'; position: absolute; bottom: 0; left: 0; right: 0; height: 3px; background: var(--red); transform: scaleX(0); transition: transform 0.25s; transform-origin: left; }
        .service-card:hover { box-shadow: 0 10px 40px rgba(0,0,0,0.1); transform: translateY(-4px); }
        .service-card:hover::after { transform: scaleX(1); }
        .service-icon { width: 56px; height: 56px; background: rgba(192,57,43,0.1); border-radius: 12px; display: flex; align-items: center; justify-content: center; color: var(--red); margin-bottom: 20px; }
        .service-card h3 { font-size: 1.05rem; font-weight: 700; color: var(--navy); margin-bottom: 10px; }
        .service-card p { font-size: 0.9rem; color: var(--gray); line-height: 1.65; margin-bottom: 18px; }
        .service-link { color: var(--red); font-size: 0.88rem; font-weight: 700; display: flex; align-items: center; gap: 6px; }

        /* TWO COL */
        .two-col { display: grid; grid-template-columns: 1fr 1fr; gap: 64px; align-items: center; }
        .two-col img { border-radius: 14px; box-shadow: 0 8px 40px rgba(0,0,0,0.12); width: 100%; height: 400px; object-fit: cover; }

        /* WHY US */
        .why-grid { display: grid; grid-template-columns: repeat(4,1fr); gap: 24px; margin-top: 48px; }
        .why-card { text-align: center; padding: 32px 20px; background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1); border-radius: 14px; }
        .why-card .icon { font-size: 2.4rem; margin-bottom: 16px; display: block; }
        .why-card h3 { color: #fff; font-size: 1rem; font-weight: 700; margin-bottom: 10px; }
        .why-card p { color: rgba(255,255,255,0.6); font-size: 0.88rem; line-height: 1.6; }

        /* FORM SECTION */
        .form-section { background: linear-gradient(135deg, var(--navy), #1a335e); padding: 88px 0; }
        .form-inner { display: grid; grid-template-columns: 1fr 1fr; gap: 64px; align-items: start; }
        .form-info h2 { color: #fff; font-size: clamp(1.6rem,4vw,2.4rem); font-weight: 800; margin-bottom: 16px; }
        .form-info p { color: rgba(255,255,255,0.7); font-size: 1rem; line-height: 1.75; margin-bottom: 28px; }
        .form-contact-item { display: flex; align-items: center; gap: 14px; margin-bottom: 18px; }
        .form-contact-item .icon { width: 44px; height: 44px; background: rgba(255,255,255,0.1); border-radius: 50%; display: flex; align-items: center; justify-content: center; color: #fff; flex-shrink: 0; }
        .form-contact-item a { color: rgba(255,255,255,0.85); text-decoration: none; font-size: 0.95rem; font-weight: 500; }
        .form-contact-item a:hover { color: #fff; }
        .orcamento-form { background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1); border-radius: 16px; padding: 36px; }
        .form-row { margin-bottom: 18px; }
        .form-row label { display: block; color: rgba(255,255,255,0.75); font-size: 13px; font-weight: 600; margin-bottom: 7px; text-transform: uppercase; letter-spacing: 0.5px; }
        .form-row input, .form-row select, .form-row textarea {
            width: 100%; background: rgba(255,255,255,0.06); border: 1px solid rgba(255,255,255,0.15);
            color: #fff; padding: 13px 16px; border-radius: 6px; font-family: inherit; font-size: 15px;
            transition: border-color 0.2s;
        }
        .form-row input::placeholder, .form-row textarea::placeholder { color: rgba(255,255,255,0.35); }
        .form-row input:focus, .form-row select:focus, .form-row textarea:focus { outline: none; border-color: rgba(255,255,255,0.4); }
        .form-row select option { background: #111d35; color: #fff; }
        .form-row textarea { height: 100px; resize: vertical; }
        .btn-submit { width: 100%; background: #c0392b; color: #fff; border: none; padding: 16px; border-radius: 6px; font-size: 15px; font-weight: 700; cursor: pointer; text-transform: uppercase; letter-spacing: 0.5px; transition: background 0.2s; }
        .btn-submit:hover { background: #a93226; }

        /* CTA BAND */
        .cta-band { background: linear-gradient(135deg, var(--navy), #1e335e); padding: 72px 0; text-align: center; }
        .cta-band h2 { color: #fff; font-size: clamp(1.5rem,4vw,2.3rem); font-weight: 800; margin-bottom: 12px; }
        .cta-band p { color: rgba(255,255,255,0.7); font-size: 1.05rem; margin-bottom: 36px; }
        .cta-buttons { display: flex; gap: 16px; justify-content: center; flex-wrap: wrap; }

        /* FOOTER */
        footer { background: #05111f; color: rgba(255,255,255,0.6); padding: 56px 0 24px; }
        .footer-inner { display: grid; grid-template-columns: 2fr 1fr 1fr; gap: 40px; margin-bottom: 40px; }
        .footer-logo img { height: 60px; margin-bottom: 16px; }
        .footer-desc { font-size: 0.9rem; line-height: 1.7; max-width: 300px; margin-bottom: 20px; }
        footer h4 { color: #fff; font-size: 0.95rem; font-weight: 700; margin-bottom: 16px; }
        footer ul { list-style: none; }
        footer ul li { margin-bottom: 9px; }
        footer ul li a { color: rgba(255,255,255,0.55); text-decoration: none; font-size: 0.88rem; transition: color 0.2s; }
        footer ul li a:hover { color: #fff; }
        .footer-bottom { border-top: 1px solid rgba(255,255,255,0.1); padding-top: 24px; text-align: center; font-size: 0.82rem; }
        .footer-legal { display: flex; gap: 20px; justify-content: center; margin-top: 10px; flex-wrap: wrap; }
        .footer-legal a { color: rgba(255,255,255,0.4); text-decoration: none; font-size: 0.8rem; }
        .footer-legal a:hover { color: rgba(255,255,255,0.7); }

        /* HAMBURGER */
        .crh-hamburger { display: none; flex-direction: column; gap: 5px; background: none; border: none; cursor: pointer; padding: 6px; }
        .crh-hamburger span { display: block; width: 24px; height: 2px; background: #1a202c; border-radius: 2px; transition: transform 0.3s, opacity 0.3s; }
        .crh-hamburger.open span:nth-child(1) { transform: translateY(7px) rotate(45deg); }
        .crh-hamburger.open span:nth-child(2) { opacity: 0; }
        .crh-hamburger.open span:nth-child(3) { transform: translateY(-7px) rotate(-45deg); }

        /* MOBILE WA FAB */
        #mobile-wa-fab { position: fixed; bottom: 22px; right: 22px; width: 56px; height: 56px; background: #25D366; color: #fff; border-radius: 50%; display: flex; align-items: center; justify-content: center; box-shadow: 0 4px 16px rgba(37,211,102,0.45); z-index: 999998; text-decoration: none; transition: transform 0.2s, box-shadow 0.2s; }
        #mobile-wa-fab:hover { transform: scale(1.1); }

        @media (max-width: 900px) {
            .crh-hamburger { display: flex; }
            .crh-nav { display: none; width: 100%; order: 3; background: #fff; border-top: 1px solid #f0f0f0; padding: 8px 0; }
            .crh-nav.open { display: block; }
            .crh-menu { flex-direction: column; gap: 0; width: 100%; }
            .crh-menu > li > a { padding: 12px 20px; border-bottom: 1px solid #f5f5f5; }
            .crh-dropdown { position: static; box-shadow: none; opacity: 1; visibility: visible; transform: none; display: none; border-left: 3px solid #0d2a45; margin-left: 20px; min-width: auto; border-top: none; }
            .crh-has-dropdown.open-mobile .crh-dropdown { display: block; }
            .crh-actions { display: none !important; }
            .crh-actions.open { display: flex !important; flex-direction: column; width: 100%; padding: 12px 16px; background: #fff; border-top: 1px solid #f0f0f0; }
            .crh-logo img { height: 55px; margin-top: 8px; }
            .crh-container { flex-wrap: wrap; }
            .services-grid, .why-grid { grid-template-columns: 1fr; }
            .two-col, .form-inner { grid-template-columns: 1fr; }
            .footer-inner { grid-template-columns: 1fr; }
            .stats-bar { grid-template-columns: 1fr 1fr; }
            #mobile-wa-fab { display: flex; }
        }
        @media (min-width: 901px) { #mobile-wa-fab { display: none; } }
        @media (max-width: 600px) {
            .hero { min-height: auto; padding-top: 110px; }
            .stats-bar { grid-template-columns: 1fr 1fr; }
        }
    </style>
</head>
<body>

<!-- HEADER -->
<header id="custom-roovon-header">
    <div class="crh-container">
        <div class="crh-logo">
            <a href="index.html"><img src="logo_telhados_renovados.jpg" alt="Telhados Renovados Logo"></a>
        </div>
        <nav class="crh-nav">
            <ul class="crh-menu">
                <li><a href="index.html">Home</a></li>
                <li class="crh-has-dropdown">
                    <a href="#">Servi&ccedil;os <svg viewBox="0 0 320 512" width="10" height="10" style="margin-left:3px"><path fill="currentColor" d="M143 352.3L7 216.3c-9.4-9.4-9.4-24.6 0-33.9l22.6-22.6c9.4-9.4 24.6-9.4 33.9 0l96.4 96.4 96.4-96.4c9.4-9.4 24.6-9.4 33.9 0l22.6 22.6c9.4 9.4 9.4 24.6 0 33.9l-136 136c-9.2 9.4-24.4 9.4-33.8 0z"/></svg></a>
                    <ul class="crh-dropdown">
                        <li><a href="instalacao-telhados.html">Instala&ccedil;&atilde;o de Telhados e Coberturas</a></li>
                        <li><a href="remodelacao-telhados.html">Remodela&ccedil;&atilde;o de Telhados</a></li>
                        <li><a href="reparacao-telhados.html">Repara&ccedil;&atilde;o de Telhados</a></li>
                        <li><a href="inspecao-orcamentacao.html">Inspe&ccedil;&atilde;o e Or&ccedil;amenta&ccedil;&atilde;o</a></li>
                        <li><a href="limpeza-telhados.html">Limpeza e Manuten&ccedil;&atilde;o</a></li>
                        <li><a href="sistemas-impermeabilizacao.html">Sistemas de Impermeabiliza&ccedil;&atilde;o</a></li>
                        <li><a href="caleiras-rufagem.html">Caleiras e Rufagem</a></li>
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
        <button class="crh-hamburger" id="crh-hamburger" aria-label="Menu">
            <span></span><span></span><span></span>
        </button>
    </div>
</header>

<!-- HERO -->
<section class="hero">
    <div class="container">
        <div class="hero-layout">
            <div class="hero-content">
                <div class="hero-badge">
                    <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
                    Especialistas em Telhados no Porto desde 2008
                </div>
                <h1>Telhados Seguros e Duradouros <em>para a Sua Casa</em></h1>
                <p>Instala&ccedil;&atilde;o, repara&ccedil;&atilde;o e manuten&ccedil;&atilde;o de telhados no Porto e Grande Porto. Equipa certificada, materiais premium e garantia por escrito em todos os trabalhos.</p>
                <div class="hero-ctas">
                    <a href="tel:+351937065056" class="btn-primary">
                        <svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 01-2.18 2 19.79 19.79 0 01-8.63-3.07A19.5 19.5 0 013.07 10.8a19.79 19.79 0 01-3.07-8.68A2 2 0 012 0h3a2 2 0 012 1.72c.127.96.361 1.903.7 2.81a2 2 0 01-.45 2.11L6.09 7.91a16 16 0 006 6l1.27-1.27a2 2 0 012.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0122 14.92z"/></svg>
                        Ligar Agora &bull; 937 065 056
                    </a>
                </div>
                <div class="stats-bar">
                    <div class="stat-item"><span class="stat-num">+15</span><span class="stat-label">Anos de Experi&ecirc;ncia</span></div>
                    <div class="stat-item"><span class="stat-num">500+</span><span class="stat-label">Telhados Realizados</span></div>
                    <div class="stat-item"><span class="stat-num">5</span><span class="stat-label">Anos de Garantia</span></div>
                    <div class="stat-item"><span class="stat-num">24h</span><span class="stat-label">Or&ccedil;amento Gratuito</span></div>
                </div>
            </div>
            
            <div class="hero-form-column">
                <div class="hero-form-box">
                    <h3>Or&ccedil;amento Gratuito em 24h</h3>
                    <script>var heroSubmitted=false;</script>
                    <iframe name="hero_iframe" id="hero_iframe" style="display:none;" onload="if(heroSubmitted){document.getElementById('hero-response').innerHTML='<div style=&quot;padding:12px;background:#d4edda;color:#155724;border-radius:6px;font-size:14px;margin-top:10px;&quot;>&#10003; Recebemos o seu pedido! Ligamos em breve.</div>';document.getElementById('heroForm').reset();}"></iframe>
                    <form id="heroForm" action="https://script.google.com/macros/s/AKfycbwh-oIofPUVh99nRIF7tBSchelbkounkRtY3x4AXnLmLYjKwDKmn--_DsaXJyKyFm9o/exec" target="hero_iframe" method="POST" onsubmit="heroSubmitted=true;">
                        <div class="form-row">
                            <label>O Seu Nome</label>
                            <input type="text" name="nome" placeholder="Nome Completo" required>
                        </div>
                        <div class="form-row">
                            <label>Contacto Telef&oacute;nico</label>
                            <input type="tel" name="telemovel" placeholder="9XX XXX XXX" required>
                        </div>
                        <div class="form-row">
                            <label>Localidade (Concelho)</label>
                            <input type="text" name="localidade" placeholder="Ex: Porto, Maia..." required>
                        </div>
                        <div class="form-row">
                            <label>Servi&ccedil;o Pretendido</label>
                            <select name="tipoProblema" required>
                                <option value="" disabled selected>O que precisa?</option>
                                <option>Instala&ccedil;&atilde;o de Telhado</option>
                                <option>Repara&ccedil;&atilde;o Úrgente</option>
                                <option>Impermeabiliza&ccedil;&atilde;o</option>
                                <option>Limpeza / Manuten&ccedil;&atilde;o</option>
                            </select>
                        </div>
                        <input type="hidden" name="detalhes" value="Mensagem enviada via formulário da capa (Home)">
                        <button type="submit" class="btn-submit">Pedir Agora &rarr;</button>
                        <div id="hero-response"></div>
                    </form>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- SERVICES -->
<section class="section">
    <div class="container">
        <div style="text-align:center;margin-bottom:8px"><span class="section-tag">Os Nossos Servi&ccedil;os</span></div>
        <h2 class="section-title" style="text-align:center">Servi&ccedil;os de Telhados Fi&aacute;veis Concebidos Para um Desempenho a Longo Prazo</h2>
        <div class="services-grid">
            <a href="instalacao-telhados.html" class="service-card">
                <div class="service-icon"><svg viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 9l9-7 9 7v11a2 2 0 01-2 2H5a2 2 0 01-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg></div>
                <h3>Instala&ccedil;&atilde;o de Telhados</h3>
                <p>Constru&ccedil;&atilde;o de novos telhados com telha cer&acirc;mica, painel sand&uacute;iche e estruturas met&aacute;licas. Projeto completo com garantia incluída.</p>
                <span class="service-link">Saiba mais <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg></span>
            </a>
            <a href="remodelacao-telhados.html" class="service-card">
                <div class="service-icon"><svg viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="2"><polyline points="23 4 23 10 17 10"/><path d="M20.49 15a9 9 0 11-2.12-9.36L23 10"/></svg></div>
                <h3>Remodela&ccedil;&atilde;o de Telhados</h3>
                <p>Substitui&ccedil;&atilde;o completa de coberturas antigas, com novos materiais e isolamento t&eacute;rmico. Garantia escrita de 5 anos.</p>
                <span class="service-link">Saiba mais <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg></span>
            </a>
            <a href="reparacao-telhados.html" class="service-card">
                <div class="service-icon"><svg viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="2"><path d="M14.7 6.3a1 1 0 000 1.4l1.6 1.6a1 1 0 001.4 0l3.77-3.77a6 6 0 01-7.94 7.94l-6.91 6.91a2.12 2.12 0 01-3-3l6.91-6.91a6 6 0 017.94-7.94l-3.76 3.76z"/></svg></div>
                <h3>Repara&ccedil;&atilde;o de Telhados</h3>
                <p>Corre&ccedil;&atilde;o de infiltra&ccedil;&otilde;es, telhas partidas, cumeiras e caleiras. Diagn&oacute;stico gratuito e interven&ccedil;&atilde;o r&aacute;pida.</p>
                <span class="service-link">Saiba mais <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg></span>
            </a>
            <a href="sistemas-impermeabilizacao.html" class="service-card">
                <div class="service-icon"><svg viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2.69l5.66 5.66a8 8 0 11-11.31 0z"/></svg></div>
                <h3>Sistemas de Impermeabiliza&ccedil;&atilde;o</h3>
                <p>Aplica&ccedil;&atilde;o de membranas, poliuretano e sistemas de sel&atilde;o contra humidades e infiltra&ccedil;&otilde;es. Garantia de 5-10 anos.</p>
                <span class="service-link">Saiba mais <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg></span>
            </a>
            <a href="limpeza-telhados.html" class="service-card">
                <div class="service-icon"><svg viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="2"><path d="M20.84 4.61a5.5 5.5 0 00-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 00-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 000-7.78z"/></svg></div>
                <h3>Limpeza e Manuten&ccedil;&atilde;o</h3>
                <p>Limpeza profissional de musgos e l&iacute;quenes, tratamento anti-vegetativo e inspe&ccedil;&atilde;o preventiva anual.</p>
                <span class="service-link">Saiba mais <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg></span>
            </a>
            <a href="inspecao-orcamentacao.html" class="service-card">
                <div class="service-icon"><svg viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg></div>
                <h3>Inspe&ccedil;&atilde;o e Or&ccedil;amenta&ccedil;&atilde;o</h3>
                <p>Diagn&oacute;stico gratuito ao estado do telhado com relat&oacute;rio fotogr&aacute;fico e or&ccedil;amento detalhado sem compromisso.</p>
                <span class="service-link">Saiba mais <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg></span>
            </a>
        </div>
    </div>
</section>

<!-- WHY US - dark section -->
<section style="background:linear-gradient(135deg,#0d2a45,#111d35);padding:88px 0;">
    <div class="container">
        <div style="text-align:center;margin-bottom:8px"><span class="section-tag" style="background:rgba(255,255,255,0.1);color:rgba(255,255,255,0.8)">Porque Nos Escolher</span></div>
        <h2 class="section-title" style="color:#fff;text-align:center;margin-bottom:48px">O Compromisso que nos distingue</h2>
        <div class="why-grid">
            <div class="why-card">
                <span class="icon">&#127919;</span>
                <h3>15+ Anos de Experi&ecirc;ncia</h3>
                <p>Mais de uma d&eacute;cada a executar telhados no Porto e Grande Porto com qualidade comprovada.</p>
            </div>
            <div class="why-card">
                <span class="icon">&#128196;</span>
                <h3>Garantia por Escrito</h3>
                <p>Todos os nossos trabalhos incluem garantia documental de 5 a 10 anos sobre materiais e m&atilde;o de obra.</p>
            </div>
            <div class="why-card">
                <span class="icon">&#9200;</span>
                <h3>Or&ccedil;amento em 24 Horas</h3>
                <p>Visita gratuita ao local e or&ccedil;amento detalhado entregue no pr&oacute;ximo dia &uacute;til, sem compromisso.</p>
            </div>
            <div class="why-card">
                <span class="icon">&#128081;</span>
                <h3>Equipa Certificada</h3>
                <p>Profissionais qualificados, segurados e com forma&ccedil;&atilde;o cont&iacute;nua nas mais recentes t&eacute;cnicas de cobertura.</p>
            </div>
        </div>
    </div>
</section>

<!-- INTRO / ABOUT -->
<section class="section">
    <div class="container">
        <div class="two-col">
            <div>
                <span class="section-tag">Quem Somos</span>
                <h2 class="section-title">Especialistas em Coberturas no Porto h&aacute; mais de 15 Anos</h2>
                <p class="section-sub" style="margin-bottom:20px">A Telhados Renovados &eacute; uma empresa portuense especializada na instala&ccedil;&atilde;o, repara&ccedil;&atilde;o e manuten&ccedil;&atilde;o de coberturas para habita&ccedil;&otilde;es, condom&iacute;nios e edif&iacute;cios comerciais em todo o distrito do Porto.</p>
                <p class="section-sub" style="margin-bottom:32px">Trabalhamos com os melhores materiais do mercado &mdash; telha cer&acirc;mica, painel sand&uacute;iche, membranas impermeabilizantes &mdash; e entregamos sempre garantia por escrito. Orçamento gratuito em 24 horas.</p>
                <a href="contactos.html" class="btn-primary">Pedir Or&ccedil;amento Gratuito</a>
            </div>
            <img src="img-remodelacao.jpeg" alt="Equipa Telhados Renovados a trabalhar no Porto" loading="lazy">
        </div>
    </div>
</section>

<!-- FORM SECTION -->
<section class="form-section">
    <div class="container">
        <div class="form-inner">
            <div class="form-info">
                <span class="section-tag" style="background:rgba(255,255,255,0.1);color:rgba(255,255,255,0.8)">Contacto Directo</span>
                <h2>Solicite um Or&ccedil;amento Gratuito</h2>
                <p>Preencha o formul&aacute;rio e entraremos em contacto em menos de 24 horas com um or&ccedil;amento detalhado, sem compromisso.</p>
                <div class="form-contact-item">
                    <div class="icon"><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 01-2.18 2 19.79 19.79 0 01-8.63-3.07A19.5 19.5 0 013.07 10.8a19.79 19.79 0 01-3.07-8.68A2 2 0 012 0h3a2 2 0 012 1.72c.127.96.361 1.903.7 2.81a2 2 0 01-.45 2.11L6.09 7.91a16 16 0 006 6l1.27-1.27a2 2 0 012.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0122 14.92z"/></svg></div>
                    <a href="tel:+351937065056">+351 937 065 056</a>
                </div>
                <div class="form-contact-item">
                    <div class="icon"><svg viewBox="0 0 448 512" width="20" height="20"><path fill="currentColor" d="M380.9 97.1C339 55.1 283.2 32 223.9 32c-122.4 0-222 99.6-222 222 0 39.1 10.2 77.3 29.6 111L0 480l117.7-30.9c32.4 17.7 68.9 27 106.1 27h.1c122.3 0 224.1-99.6 224.1-222 0-59.3-23.2-115-65.1-157z"/></svg></div>
                    <a href="https://wa.me/351937065056" target="_blank">WhatsApp: 937 065 056</a>
                </div>
                <div class="form-contact-item">
                    <div class="icon"><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg></div>
                    <a href="mailto:contacto@telhadosrenovados.pt">contacto@telhadosrenovados.pt</a>
                </div>
            </div>
            <div class="orcamento-form">
                <script>var submitted=false;</script>
                <iframe name="hidden_iframe" id="hidden_iframe" style="display:none;" onload="if(submitted){document.getElementById('response').innerHTML='<div style=&quot;padding:15px;background:#d4edda;color:#155724;border-radius:6px;margin-top:12px;&quot;>&#10003; Pedido enviado com sucesso! Entraremos em contacto brevemente.</div>';document.getElementById('contactForm').reset();}"></iframe>
                <form id="contactForm" action="https://script.google.com/macros/s/AKfycbwh-oIofPUVh99nRIF7tBSchelbkounkRtY3x4AXnLmLYjKwDKmn--_DsaXJyKyFm9o/exec" target="hidden_iframe" method="POST" onsubmit="submitted=true;">
                    <div class="form-row">
                        <label>Nome Completo</label>
                        <input type="text" name="nome" placeholder="O seu nome" required>
                    </div>
                    <div class="form-row">
                        <label>Telemovel / WhatsApp</label>
                        <input type="tel" name="telemovel" placeholder="9XX XXX XXX" pattern="[0-9()#&amp;+*=.-]+" required>
                    </div>
                    <div class="form-row">
                        <label>Localidade</label>
                        <input type="text" name="localidade" placeholder="Ex: Porto, Maia, Matosinhos..." required>
                    </div>
                    <div class="form-row">
                        <label>Tipo de Servi&ccedil;o</label>
                        <select name="tipoProblema" required>
                            <option value="" disabled selected>Escolha uma op&ccedil;&atilde;o</option>
                            <option>Instala&ccedil;&atilde;o de Telhado Novo</option>
                            <option>Remodela&ccedil;&atilde;o de Telhado</option>
                            <option>Repara&ccedil;&atilde;o / Infiltra&ccedil;&otilde;es</option>
                            <option>Impermeabiliza&ccedil;&atilde;o</option>
                            <option>Limpeza e Manuten&ccedil;&atilde;o</option>
                            <option>Inspe&ccedil;&atilde;o Gratuita</option>
                            <option>Caleiras e Rufagem</option>
                            <option>Outro</option>
                        </select>
                    </div>
                    <div class="form-row">
                        <label>Detalhes (opcional)</label>
                        <textarea name="detalhes" placeholder="Descreva brevemente o seu caso..."></textarea>
                    </div>
                    <button type="submit" class="btn-submit">Enviar Pedido de Or&ccedil;amento</button>
                    <div id="response"></div>
                </form>
            </div>
        </div>
    </div>
</section>

<!-- CTA BAND -->
<section class="cta-band">
    <div class="container">
        <h2>Pronto para resolver o seu telhado?</h2>
        <p>Entre em contacto agora. Or&ccedil;amento gratuito e sem compromisso em 24 horas para todo o Grande Porto.</p>
        <div class="cta-buttons">
            <a href="https://wa.me/351937065056" target="_blank" class="btn-wa">
                <svg viewBox="0 0 448 512" width="18" height="18"><path fill="currentColor" d="M380.9 97.1C339 55.1 283.2 32 223.9 32c-122.4 0-222 99.6-222 222 0 39.1 10.2 77.3 29.6 111L0 480l117.7-30.9c32.4 17.7 68.9 27 106.1 27h.1c122.3 0 224.1-99.6 224.1-222 0-59.3-23.2-115-65.1-157z"/></svg>
                WhatsApp Agora
            </a>
            <a href="tel:+351937065056" class="btn-call">
                <svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 01-2.18 2 19.79 19.79 0 01-8.63-3.07A19.5 19.5 0 013.07 10.8a19.79 19.79 0 01-3.07-8.68A2 2 0 012 0h3a2 2 0 012 1.72c.127.96.361 1.903.7 2.81a2 2 0 01-.45 2.11L6.09 7.91a16 16 0 006 6l1.27-1.27a2 2 0 012.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0122 14.92z"/></svg>
                +351 937 065 056
            </a>
        </div>
    </div>
</section>

<!-- FOOTER -->
<footer>
    <div class="container">
        <div class="footer-inner">
            <div>
                <div class="footer-logo"><img src="logo_telhados_renovados.jpg" alt="Telhados Renovados"></div>
                <p class="footer-desc">Especialistas em instala&ccedil;&atilde;o, repara&ccedil;&atilde;o e manuten&ccedil;&atilde;o de telhados no Porto e Grande Porto h&aacute; mais de 15 anos.</p>
                <a href="https://wa.me/351937065056" target="_blank" style="display:inline-flex;align-items:center;gap:8px;background:#25D366;color:#fff;padding:10px 18px;border-radius:6px;text-decoration:none;font-size:13px;font-weight:700;">
                    <svg viewBox="0 0 448 512" width="14" height="14"><path fill="currentColor" d="M380.9 97.1C339 55.1 283.2 32 223.9 32c-122.4 0-222 99.6-222 222 0 39.1 10.2 77.3 29.6 111L0 480l117.7-30.9c32.4 17.7 68.9 27 106.1 27h.1c122.3 0 224.1-99.6 224.1-222 0-59.3-23.2-115-65.1-157z"/></svg>
                    Falar no WhatsApp
                </a>
            </div>
            <div>
                <h4>Servi&ccedil;os</h4>
                <ul>
                    <li><a href="instalacao-telhados.html">Instala&ccedil;&atilde;o de Telhados</a></li>
                    <li><a href="remodelacao-telhados.html">Remodela&ccedil;&atilde;o de Telhados</a></li>
                    <li><a href="reparacao-telhados.html">Repara&ccedil;&atilde;o de Telhados</a></li>
                    <li><a href="sistemas-impermeabilizacao.html">Impermeabiliza&ccedil;&atilde;o</a></li>
                    <li><a href="limpeza-telhados.html">Limpeza e Manuten&ccedil;&atilde;o</a></li>
                    <li><a href="caleiras-rufagem.html">Caleiras e Rufagem</a></li>
                    <li><a href="inspecao-orcamentacao.html">Inspe&ccedil;&atilde;o Gratuita</a></li>
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
        <div class="footer-bottom">
            <p>Copyright &copy; 2026 Telhados Renovados &ndash; Todos os direitos reservados. Porto, Portugal. &nbsp;|&nbsp; Desenvolvido por <a href="https://foturemkt.com/" target="_blank" rel="noopener" style="color:rgba(255,255,255,0.5);text-decoration:none;font-weight:600;">Foture MKt</a></p>
            <div class="footer-legal">
                <a href="politica-de-privacidade.html">Pol&iacute;tica de Privacidade</a>
                <a href="termos-e-condicoes.html">Termos e Condi&ccedil;&otilde;es</a>
                <a href="politica-de-cookies.html">Pol&iacute;tica de Cookies</a>
                <a href="politica-de-garantia.html">Pol&iacute;tica de Garantia</a>
            </div>
        </div>
    </div>
</footer>

<!-- Floating WA -->
<a id="mobile-wa-fab" href="https://wa.me/351937065056" target="_blank" aria-label="WhatsApp">
    <svg viewBox="0 0 448 512" width="26" height="26"><path fill="currentColor" d="M380.9 97.1C339 55.1 283.2 32 223.9 32c-122.4 0-222 99.6-222 222 0 39.1 10.2 77.3 29.6 111L0 480l117.7-30.9c32.4 17.7 68.9 27 106.1 27h.1c122.3 0 224.1-99.6 224.1-222 0-59.3-23.2-115-65.1-157z"/></svg>
</a>

<script>
(function() {
    var header = document.getElementById(\'custom-roovon-header\');
    var hamburger = document.getElementById(\'crh-hamburger\');
    var nav = document.querySelector(\'.crh-nav\');
    var actions = document.querySelector(\'.crh-actions\');
    var servicos = document.querySelector(\'.crh-has-dropdown\');

    window.addEventListener(\'scroll\', function() {
        header.classList.toggle(\'scrolled\', window.scrollY > 60);
    }, { passive: true });

    if (hamburger) {
        hamburger.addEventListener(\'click\', function() {
            var isOpen = nav.classList.contains(\'open\');
            hamburger.classList.toggle(\'open\', !isOpen);
            nav.classList.toggle(\'open\', !isOpen);
            if (actions) actions.classList.toggle(\'open\', !isOpen);
        });
    }

    if (servicos) {
        servicos.querySelector(\'a\').addEventListener(\'click\', function(e) {
            if (window.innerWidth <= 900) {
                e.preventDefault();
                servicos.classList.toggle(\'open-mobile\');
            }
        });
    }
})();
</script>
</body>
</html>'''

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('index.html rebuilt successfully!')
print(f'Size: {len(html)} chars')
