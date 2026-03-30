import fs from 'fs';
import * as cheerio from 'cheerio';

const htmlStr = fs.readFileSync('roovon_clone/newkit.creativemox.com/roovon/index.html', 'utf8');
const $ = cheerio.load(htmlStr);

// Let's find the absolute first .elementor-element after the custom header
const firstEcon = $('[data-elementor-type="wp-page"] > .elementor-element').first();

if (firstEcon.length) {
    // We add a specific class to it so we can target it with CSS to bring it up
    firstEcon.addClass('hero-capa-fixed');
    
    // Inject a <style> block that ensures NO GAP exists between header and capa
    // And reduces the inner padding of the capa so the content goes UP
    if ($('#fix-capa-gap').length === 0) {
        $('head').append(`
        <style id="fix-capa-gap">
            /* Kill any top spacing on the page wrapper */
            html, body, .elementor-page, [data-elementor-type="wp-page"] {
                margin-top: 0 !important;
                padding-top: 0 !important;
            }
            
            /* Bring the first container (Capa) right up against the nav menu */
            .hero-capa-fixed {
                margin-top: 0 !important;
                /* By default this might have 150px or 10rem of padding-top to account for the old header, let's reduce it to 40px */
                padding-top: 60px !important; 
            }

            /* Also check if it has a pseudo-element wrapper pushing it */
            .hero-capa-fixed > .e-con-inner {
                padding-top: 0 !important;
                margin-top: 0 !important;
            }
        </style>
        `);
    }
}

fs.writeFileSync('roovon_clone/newkit.creativemox.com/roovon/index.html', $.html());
console.log('Fixed the cover image gap!');
