import fs from 'fs';
import * as cheerio from 'cheerio';

const htmlStr = fs.readFileSync('roovon_clone/newkit.creativemox.com/roovon/index.html', 'utf8');
const $ = cheerio.load(htmlStr);

// Force the very first e-con (the hero section) to have margin-top: 0
const wpPage = $('[data-elementor-type="wp-page"]');
const firstSection = wpPage.find('.e-parent, .elementor-section').first();

if (firstSection.length) {
    firstSection.css('margin-top', '0px');
    // Also, Elementor e-con might have data-settings with negative margin or padding
    firstSection.attr('style', (firstSection.attr('style') || '') + '; margin-top: 0px !important;');
    
    // We can also inject a global CSS to make absolutely sure:
    // Some elementor classes could have `margin-top` natively.
    $('head').append(`
        <style id="nuke-white-space">
            html, body {
                margin: 0 !important;
                padding: 0 !important;
                background-color: #0073B1; /* Give body blue background just in case */
            }
            .elementor-${wpPage.attr('data-elementor-id')} {
                margin-top: 0 !important;
                padding-top: 0 !important;
            }
            .${firstSection.attr('class').split(' ').join('.')} {
                margin-top: 0 !important;
            }
            /* Reset WordPress core blocks that might inject a margin */
            .wp-site-blocks, .site-main, #main, #primary {
                margin-top: 0 !important;
                padding-top: 0 !important;
            }
        </style>
    `);
}

fs.writeFileSync('roovon_clone/newkit.creativemox.com/roovon/index.html', $.html());
console.log('Fixed blue section margin and added nuke CSS.');
