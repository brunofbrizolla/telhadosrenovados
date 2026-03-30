import fs from 'fs';
import * as cheerio from 'cheerio';

const htmlStr = fs.readFileSync('roovon_clone/newkit.creativemox.com/roovon/index.html', 'utf8');
const $ = cheerio.load(htmlStr);

// 1. Add hamburger button to the custom header (inside .crh-container, after logo)
const hamburgerBtn = `<button class="crh-hamburger" id="crh-hamburger" aria-label="Abrir menu" aria-expanded="false">
    <span></span><span></span><span></span>
</button>`;

// Insert the hamburger button as last child of crh-container
$('.crh-container').append(hamburgerBtn);

// 2. Inject responsive CSS + hamburger JS
$('head').append(`
<style id="responsive-css">
/* ===== RESPONSIVE BREAKPOINTS ===== */

/* Viewport meta already injected by page, but just in case */
/* @viewport { width: device-width; } */

/* --- DESKTOP: 1200px+ stays as before --- */

/* --- TABLET & MOBILE HEADER: ≤ 900px --- */
@media (max-width: 900px) {
    .crh-container {
        flex-wrap: wrap !important;
        padding: 4px 16px !important;
        position: relative !important;
    }

    /* Logo stays left */
    .crh-logo {
        flex: 1 !important;
    }

    /* Show hamburger button */
    .crh-hamburger {
        display: flex !important;
        flex-direction: column !important;
        justify-content: space-between !important;
        gap: 5px !important;
        background: none !important;
        border: none !important;
        cursor: pointer !important;
        padding: 6px !important;
        z-index: 100001 !important;
    }
    .crh-hamburger span {
        display: block !important;
        width: 24px !important;
        height: 2px !important;
        background: #1a202c !important;
        border-radius: 2px !important;
        transition: transform 0.3s ease, opacity 0.3s ease !important;
    }
    /* Animated X when open */
    .crh-hamburger.open span:nth-child(1) { transform: translateY(7px) rotate(45deg) !important; }
    .crh-hamburger.open span:nth-child(2) { opacity: 0 !important; }
    .crh-hamburger.open span:nth-child(3) { transform: translateY(-7px) rotate(-45deg) !important; }

    /* Nav: hidden by default, shown as full-width dropdown when open */
    .crh-nav {
        display: none !important;
        width: 100% !important;
        order: 3 !important;
        background: #ffffff !important;
        border-top: 1px solid #f0f0f0 !important;
        padding: 8px 0 !important;
    }
    .crh-nav.open {
        display: block !important;
    }

    .crh-menu {
        flex-direction: column !important;
        gap: 0 !important;
        width: 100% !important;
    }
    .crh-menu > li {
        width: 100% !important;
    }
    .crh-menu > li > a {
        padding: 12px 20px !important;
        border-bottom: 1px solid #f5f5f5 !important;
        font-size: 14px !important;
    }

    /* Dropdown mobile: always visible under Serviços */
    .crh-dropdown {
        position: static !important;
        box-shadow: none !important;
        opacity: 1 !important;
        visibility: visible !important;
        transform: none !important;
        display: none !important;
        border-top: 1px solid #e8e8e8 !important;
        border-left: 3px solid #0d2a45 !important;
        margin-left: 20px !important;
        min-width: auto !important;
    }
    .crh-has-dropdown.open-mobile .crh-dropdown {
        display: block !important;
    }
    .crh-dropdown a {
        font-size: 13px !important;
        padding: 10px 16px !important;
    }

    /* Actions (buttons): full width row below nav */
    .crh-actions {
        display: none !important;
        width: 100% !important;
        order: 4 !important;
        flex-direction: column !important;
        gap: 8px !important;
        padding: 12px 16px !important;
        background: #fff !important;
        border-top: 1px solid #f0f0f0 !important;
    }
    .crh-actions.open {
        display: flex !important;
    }
    .crh-btn {
        width: 100% !important;
        justify-content: center !important;
        padding: 14px !important;
        font-size: 13px !important;
    }

    /* Logo overflow effect adjustment for mobile */
    .crh-logo img {
        height: 55px !important;
        margin-top: 8px !important;
    }
}

/* --- MOBILE: ≤ 480px extra tweaks --- */
@media (max-width: 480px) {
    .crh-logo img {
        height: 45px !important;
        margin-top: 5px !important;
    }
    
    /* Page Elementor content sections: avoid horizontal scroll */
    .elementor-section, .e-con {
        max-width: 100% !important;
        overflow-x: hidden !important;
    }
    
    /* Hero text fix */
    h1 { font-size: 1.8rem !important; }
    h2 { font-size: 1.4rem !important; }
}

/* Hide hamburger on desktop */
@media (min-width: 901px) {
    .crh-hamburger {
        display: none !important;
    }
}

/* General global responsive polishes */
* {
    box-sizing: border-box;
}
html {
    overflow-x: hidden !important;
}
body {
    overflow-x: hidden !important;
}
img {
    max-width: 100%;
    height: auto;
}
</style>
`);

// 3. Inject JS for hamburger toggle (at end of body)
$('body').append(`
<script id="responsive-hamburger-js">
(function() {
    var hamburger = document.getElementById('crh-hamburger');
    var nav = document.querySelector('.crh-nav');
    var actions = document.querySelector('.crh-actions');
    var servicos = document.querySelector('.crh-has-dropdown');

    if (hamburger) {
        hamburger.addEventListener('click', function() {
            var isOpen = nav && nav.classList.contains('open');
            hamburger.classList.toggle('open', !isOpen);
            hamburger.setAttribute('aria-expanded', String(!isOpen));
            if (nav) nav.classList.toggle('open', !isOpen);
            if (actions) actions.classList.toggle('open', !isOpen);
        });
    }

    // Toggle services dropdown on mobile tap
    if (servicos) {
        var link = servicos.querySelector('a');
        link.addEventListener('click', function(e) {
            if (window.innerWidth <= 900) {
                e.preventDefault();
                servicos.classList.toggle('open-mobile');
            }
        });
    }
})();
</script>
`);

fs.writeFileSync('roovon_clone/newkit.creativemox.com/roovon/index.html', $.html());
console.log('Full responsive layout applied with hamburger menu!');
