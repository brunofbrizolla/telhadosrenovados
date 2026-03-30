import fs from 'fs';
import * as cheerio from 'cheerio';

const htmlStr = fs.readFileSync('roovon_clone/newkit.creativemox.com/roovon/index.html', 'utf8');
const $ = cheerio.load(htmlStr);

// We will replace the entire style block that we appended for the custom header.
// It's easier to just remove the old custom header entirely and prepend the new ultra-premium one!

const premiumHeaderHTML = `
<!-- CUSTOM ROOVON HEADER -->
<header id="custom-roovon-header">
    <div class="crh-container">
        <div class="crh-logo">
            <a href="index.html">
                <img src="https://newkit.creativemox.com/roovon/wp-content/uploads/sites/26/2026/01/logo_roovon.png" alt="Roovon Logo" />
            </a>
        </div>
        <nav class="crh-nav">
            <ul class="crh-menu">
                <li><a href="index.html">Home</a></li>
                <li class="crh-has-dropdown">
                    <a href="#">Serviços <svg viewBox="0 0 320 512" width="10" height="10"><path fill="currentColor" d="M143 352.3L7 216.3c-9.4-9.4-9.4-24.6 0-33.9l22.6-22.6c9.4-9.4 24.6-9.4 33.9 0l96.4 96.4 96.4-96.4c9.4-9.4 24.6-9.4 33.9 0l22.6 22.6c9.4 9.4 9.4 24.6 0 33.9l-136 136c-9.2 9.4-24.4 9.4-33.8 0z"></path></svg></a>
                    <ul class="crh-dropdown">
                        <li><a href="instalacao-telhados-coberturas.html">Instalação de Telhados e Coberturas</a></li>
                        <li><a href="reparacao-telhados.html">Reparação de telhados</a></li>
                        <li><a href="limpeza-telhados.html">Limpeza de Telhados</a></li>
                    </ul>
                </li>
                <li><a href="contactos.html">Contactos</a></li>
            </ul>
        </nav>
        <div class="crh-actions">
            <a href="#" class="crh-btn crh-btn-navy">Faça seu orçamento</a>
            <a href="https://wa.me/5511999999999" target="_blank" class="crh-btn crh-btn-whatsapp">
                <svg viewBox="0 0 448 512" width="18" height="18"><path fill="currentColor" d="M380.9 97.1C339 55.1 283.2 32 223.9 32c-122.4 0-222 99.6-222 222 0 39.1 10.2 77.3 29.6 111L0 480l117.7-30.9c32.4 17.7 68.9 27 106.1 27h.1c122.3 0 224.1-99.6 224.1-222 0-59.3-25.2-115-67.1-157zM223.9 414.7c-33.5 0-66.3-8.8-94.9-25.5l-6.8-4-70.5 18.5 18.8-68.8-4.4-7c-18.4-29.2-28.1-63.1-28.1-98.3 0-103.1 84.1-187.2 187.3-187.2 50 0 97 19.5 132.3 54.8 35.3 35.3 54.8 82.2 54.8 132.3 0 103.3-84.1 187.2-187.1 187.2zM286.2 301.2c-17.7 5.1-42-12.7-44.5-12.7-2.6 0-36.6 22-43.1 26.5s-23.7 14.5-31.5 5.6c-7.9-9.1-17-18-20.1-19.5-3.1-1.6-13.8-6.1-9.9-19 3.8-12.7 15.3-24.4 20.3-27.1 5.1-2.6 10-18.8 6.4-23.9-3.6-5.1-15.6-38.3-21.4-52.6-5.6-14-11.3-11.8-15.5-12-4.1-.1-8.8-.2-13.5-.2-4.7 0-12.3 1.8-18.7 8.8-6.4 6.9-24.5 24.1-24.5 58.7s25.1 68 28.6 72.7c3.5 4.7 49 76.5 119.5 105.8 45.4 18.8 61.8 20.7 83.2 17.5 15.7-2.4 49-20.2 55.8-39.7 6.9-19.5 6.9-36.2 4.8-39.7-2.1-3.6-7.7-5.7-16-9.8z"></path></svg>
                Fale no WhatsApp
            </a>
        </div>
    </div>
</header>
<style>
/* CUSTOM HEADER CSS */
#custom-roovon-header {
    background: rgba(255, 255, 255, 0.98);
    backdrop-filter: blur(8px);
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.04);
    position: sticky;
    top: 0;
    z-index: 99999;
    width: 100%;
    font-family: 'Inter', sans-serif;
    border-bottom: 1px solid rgba(0,0,0,0.03);
}
.crh-container {
    max-width: 1200px;
    margin: 0 auto;
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 10px 15px; 
}
.crh-logo img {
    max-height: 40px; 
    display: block;
    transition: transform 0.3s ease;
}
.crh-logo a:hover img {
    transform: scale(1.02);
}
.crh-nav {
    display: flex;
    align-items: center;
}
.crh-menu {
    list-style: none;
    margin: 0;
    padding: 0;
    display: flex;
    align-items: center;
    gap: 35px;
}
.crh-menu > li {
    position: relative;
}
.crh-menu a {
    text-decoration: none;
    color: #1a202c; /* Softer dark for luxury feel */
    font-weight: 600;
    font-size: 15px;
    display: flex;
    align-items: center;
    gap: 5px;
    padding: 15px 0;
    transition: all 0.3s ease;
}
.crh-menu > li > a:after {
    content: '';
    position: absolute;
    bottom: 5px;
    left: 0;
    width: 0%;
    height: 2px;
    background: #e32228;
    transition: width 0.3s ease;
}
.crh-menu > li > a:hover {
    color: #e32228;
}
.crh-menu > li > a:hover:after {
    width: 100%;
}

/* Dropdown */
.crh-dropdown {
    position: absolute;
    top: 100%;
    left: 0;
    background: #ffffff;
    min-width: 280px;
    list-style: none;
    padding: 8px 0;
    margin: 0;
    border-radius: 8px;
    box-shadow: 0 10px 40px rgba(0, 0, 0, 0.08);
    opacity: 0;
    visibility: hidden;
    transform: translateY(15px);
    transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
    border: 1px solid rgba(0,0,0,0.05);
    border-top: 3px solid #e32228;
}
.crh-has-dropdown:hover .crh-dropdown {
    opacity: 1;
    visibility: visible;
    transform: translateY(0);
}
.crh-dropdown li {
    margin: 0;
}
.crh-dropdown a {
    color: #4a5568;
    font-weight: 500;
    padding: 12px 20px;
    display: block;
    font-size: 14px;
    transition: all 0.2s ease;
}
.crh-dropdown a:after { display: none; }
.crh-dropdown a:hover {
    color: #e32228;
    background: #fff5f5;
    padding-left: 26px;
}

/* Actions Section - Premium Button Designs */
.crh-actions {
    display: flex;
    align-items: center;
    gap: 16px;
}
.crh-btn {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
    padding: 12px 22px;
    font-weight: 600;
    font-size: 14px;
    border-radius: 50px; /* Pill shape for modern look */
    text-decoration: none;
    transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
}

/* Deep Navy Button */
.crh-btn-navy {
    background: #0d2a45;
    color: #ffffff;
    border: 2px solid #0d2a45;
    box-shadow: 0 4px 14px rgba(13, 42, 69, 0.2);
}
.crh-btn-navy:hover {
    background: #ffffff;
    color: #0d2a45;
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(13, 42, 69, 0.3);
}

/* Premium WhatsApp Button */
.crh-btn-whatsapp {
    background: linear-gradient(135deg, #25D366, #1EBE5D);
    color: #ffffff;
    border: 2px solid transparent;
    box-shadow: 0 4px 14px rgba(37, 211, 102, 0.3);
}
.crh-btn-whatsapp:hover {
    background: linear-gradient(135deg, #1EBE5D, #128C7E);
    color: #ffffff;
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(37, 211, 102, 0.4);
}
.crh-btn-whatsapp svg {
    filter: drop-shadow(0 2px 4px rgba(0,0,0,0.1));
}

#nuke-top-space, #nuke-white-space { display: none; }
</style>
`;

$('#custom-roovon-header').remove();
$('body').prepend(premiumHeaderHTML);

fs.writeFileSync('roovon_clone/newkit.creativemox.com/roovon/index.html', $.html());
console.log('Upgraded buttons to ultra-premium design!');
