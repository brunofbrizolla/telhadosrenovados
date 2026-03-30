import fs from 'fs';
import * as cheerio from 'cheerio';

const htmlStr = fs.readFileSync('roovon_clone/newkit.creativemox.com/roovon/index.html', 'utf8');
const $ = cheerio.load(htmlStr);

// The menu structure
const headerHTML = `
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
                    <a href="#">Serviços <svg viewBox="0 0 320 512" width="12" height="12"><path fill="currentColor" d="M143 352.3L7 216.3c-9.4-9.4-9.4-24.6 0-33.9l22.6-22.6c9.4-9.4 24.6-9.4 33.9 0l96.4 96.4 96.4-96.4c9.4-9.4 24.6-9.4 33.9 0l22.6 22.6c9.4 9.4 9.4 24.6 0 33.9l-136 136c-9.2 9.4-24.4 9.4-33.8 0z"></path></svg></a>
                    <ul class="crh-dropdown">
                        <li><a href="instalacao-telhados-coberturas.html">Instalação de Telhados e Coberturas</a></li>
                        <li><a href="reparacao-telhados.html">Reparação de telhados</a></li>
                        <li><a href="limpeza-telhados.html">Limpeza de Telhados</a></li>
                    </ul>
                </li>
                <li><a href="contactos.html">Contactos</a></li>
            </ul>
        </nav>
    </div>
</header>
<style>
/* CUSTOM HEADER CSS */
#custom-roovon-header {
    background: #ffffff;
    box-shadow: 0 4px 24px rgba(0, 0, 0, 0.06);
    position: sticky;
    top: 0;
    z-index: 99999;
    width: 100%;
    font-family: 'Inter', sans-serif; /* Roovon uses Inter/Figtree */
}
.crh-container {
    max-width: 1200px;
    margin: 0 auto;
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 15px 20px;
}
.crh-logo img {
    max-height: 45px;
    display: block;
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
    color: #0d2a45; /* Roovon Deep Navy */
    font-weight: 600;
    font-size: 16px;
    display: flex;
    align-items: center;
    gap: 6px;
    padding: 10px 0;
    transition: color 0.3s ease;
}
.crh-menu > li > a:hover {
    color: #e32228; /* Roovon Red */
}

/* Dropdown */
.crh-dropdown {
    position: absolute;
    top: 100%;
    left: 0;
    background: #ffffff;
    min-width: 280px;
    list-style: none;
    padding: 10px 0;
    margin: 0;
    border-radius: 6px;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
    opacity: 0;
    visibility: hidden;
    transform: translateY(15px);
    transition: all 0.3s ease;
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
    font-size: 15px;
    border-bottom: 1px solid #f1f5f9;
}
.crh-dropdown li:last-child a {
    border-bottom: none;
}
.crh-dropdown a:hover {
    color: #e32228;
    background: #fafafa;
    padding-left: 25px; /* nice little sliding effect */
}

/* Remove any existing custom sticky nuke rules that might break the sticky header */
#nuke-top-space, #nuke-white-space { display: none; }
</style>
`;

// Prepend to body
// wait, we stripped everything. Let's make sure the body receives this as the very first element.
// Also we remove any leftovers of our previous injected custom headers if they exist
$('#custom-roovon-header').remove();

$('body').prepend(headerHTML);

fs.writeFileSync('roovon_clone/newkit.creativemox.com/roovon/index.html', $.html());
console.log('Injected custom premium Roovon header!');
