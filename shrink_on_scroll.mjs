import fs from 'fs';
import * as cheerio from 'cheerio';

const htmlStr = fs.readFileSync('roovon_clone/newkit.creativemox.com/roovon/index.html', 'utf8');
const $ = cheerio.load(htmlStr);

// Remove old scroll script if any
$('#shrink-scroll-js').remove();

// Inject CSS transitions for the shrink effect
$('head').append(`
<style id="shrink-scroll-css">
    /* Base transition for smooth shrink */
    #custom-roovon-header {
        transition: box-shadow 0.3s ease, background 0.3s ease !important;
    }
    #custom-roovon-header .crh-container {
        transition: padding 0.35s ease, min-height 0.35s ease !important;
    }
    #custom-roovon-header .crh-logo img {
        transition: height 0.35s ease, margin-top 0.35s ease !important;
    }
    #custom-roovon-header .crh-btn {
        transition: padding 0.3s ease, font-size 0.3s ease, all 0.3s ease !important;
    }
    #custom-roovon-header .crh-menu a {
        transition: padding 0.3s ease, font-size 0.3s ease !important;
    }

    /* === SCROLLED STATE === */
    #custom-roovon-header.scrolled {
        box-shadow: 0 2px 20px rgba(0,0,0,0.12) !important;
        background: rgba(255,255,255,0.97) !important;
        backdrop-filter: blur(8px) !important;
    }
    #custom-roovon-header.scrolled .crh-container {
        padding: 0px 20px !important;
        min-height: 36px !important;
    }
    #custom-roovon-header.scrolled .crh-logo img {
        height: 40px !important;
        margin-top: 0px !important;
        filter: none !important;
    }
    #custom-roovon-header.scrolled .crh-btn {
        padding: 6px 14px !important;
        font-size: 11px !important;
    }
    #custom-roovon-header.scrolled .crh-btn svg {
        width: 13px !important;
        height: 13px !important;
    }
    #custom-roovon-header.scrolled .crh-menu a {
        padding: 8px 0 !important;
        font-size: 13px !important;
    }
    #custom-roovon-header.scrolled .crh-menu {
        gap: 24px !important;
    }

    /* Mobile: also shrink on scroll */
    @media (max-width: 900px) {
        #custom-roovon-header.scrolled .crh-logo img {
            height: 32px !important;
        }
    }
</style>
`);

// Inject the scroll JS listener
$('body').append(`
<script id="shrink-scroll-js">
(function() {
    var header = document.getElementById('custom-roovon-header');
    var scrollThreshold = 60; // pixels to scroll before shrinking

    if (!header) return;

    function onScroll() {
        if (window.scrollY > scrollThreshold) {
            header.classList.add('scrolled');
        } else {
            header.classList.remove('scrolled');
        }
    }

    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll(); // Run once on load in case page is already scrolled
})();
</script>
`);

fs.writeFileSync('roovon_clone/newkit.creativemox.com/roovon/index.html', $.html());
console.log('Shrink-on-scroll effect applied!');
