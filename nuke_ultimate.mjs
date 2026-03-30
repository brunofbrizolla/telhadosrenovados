import fs from 'fs';
import * as cheerio from 'cheerio';

const htmlStr = fs.readFileSync('roovon_clone/newkit.creativemox.com/roovon/index.html', 'utf8');
const $ = cheerio.load(htmlStr);

$('head').append(`
<style>
/* CSS RESET FOR WORDPRESS THEMES & ELEMENTOR STRUCTURES */
/* Kill all known structural gaps */
#content, #primary, #main, main, .site-main, .site-content, .wp-site-blocks, .elementor.elementor-837, [data-elementor-type="wp-page"], .elementor-page {
    margin-top: 0px !important;
    padding-top: 0px !important;
    margin-bottom: 0px !important;
}

/* Force the literal FIRST section inside the page to have zero margin */
main .elementor-element:first-child,
.site-content .elementor-element:first-child,
[data-elementor-type="wp-page"] > .elementor-element:first-child {
    margin-top: 0px !important;
}

/* Override any default WordPress gaps */
html, body {
    margin-top: 0px !important;
    padding-top: 0px !important;
}
#wpadminbar {
    display: none !important;
}
</style>
`);

// ALSO, let's aggressively set margin-top to negative 3000px if we find an empty text node or invisible div.
// Remove anything between header and the main content.
const header = $('#custom-roovon-header');
let nextEl = header.next();
let safeCount = 0;
while (nextEl.length > 0 && safeCount < 10) {
    const isWpPage = nextEl.attr('data-elementor-type') === 'wp-page';
    const isMain = nextEl.prop('tagName').toLowerCase() === 'main' || nextEl.hasClass('site-main') || nextEl.attr('id') === 'content';
    
    if (isWpPage || isMain) {
        break; // Stop when we reach the actual content
    }
    
    // If it's not the content and it's invisible or useless, remove it
    if (!nextEl.is('script, style, noscript')) {
        nextEl.remove();
        console.log('REMOVED GHOST NODE BETWEEN HEADER AND CONTENT:', nextEl.prop('tagName'));
    }
    nextEl = header.next();
    safeCount++;
}

// Ensure the first element inside the main container has no margin
// Elementor often adds classes like .elementor-element-xyz
const wpPage = $('[data-elementor-type="wp-page"]');
if (wpPage.length > 0) {
    const firstChild = wpPage.children().first();
    // In elementor often the first top level section has a huge padding
    // We'll reduce padding-top heavily but dynamically so it sticks!
    let currentPadding = firstChild.css('padding-top');
    // We just inject a strong style directly
    firstChild.attr('style', (firstChild.attr('style') || '') + ' margin-top: 0 !important; padding-top: 40px !important;');
}

fs.writeFileSync('roovon_clone/newkit.creativemox.com/roovon/index.html', $.html());
console.log('Destroyed structural gaps!');
