import fs from 'fs';
import * as cheerio from 'cheerio';

const htmlStr = fs.readFileSync('roovon_clone/newkit.creativemox.com/roovon/index.html', 'utf8');
const $ = cheerio.load(htmlStr);

// Let's find the text string
let heroContainer = null;
const allElements = $('*');

// Find the node containing the exact text
$('*').each((i, el) => {
    if ($(el).text().includes('Expert Roofing Services For Modern Buildings')) {
        // Walk up until we find the highest level e-con or elementor-section 
        // that is a direct child of the data-elementor-type="wp-page"
        const topLevelParent = $(el).closest('.elementor-element.e-con-full, .elementor-element.e-con-boxed, .elementor-section, .e-con');
        if (topLevelParent.length && topLevelParent.parent().attr('data-elementor-type') === 'wp-page') {
            heroContainer = topLevelParent;
            return false; // Break the each loop
        }
    }
});

if (heroContainer && heroContainer.length) {
    // Delete literally everything before it!
    let count = 0;
    heroContainer.prevAll().each((i, el) => {
        $(el).remove();
        count++;
    });
    console.log(`Removed ${count} top-level ghost elements before the Hero section.`);

    // Now, force its top margins and padding
    heroContainer.attr('style', (heroContainer.attr('style') || '') + ' margin-top: 0 !important; top: 0 !important;');
    
    // Sometimes there's also an elementor-location-header or an invisible row wrapper between body and wp-page
    const wpPage = $('[data-elementor-type="wp-page"]');
    wpPage.prevAll().each((i, el) => {
        // Don't remove the custom header we added!
        if ($(el).attr('id') !== 'custom-roovon-header' && !$(el).is('style, link, script, noscript, meta, title')) {
            $(el).remove();
            console.log('Removed an invisible wrapper outside wp-page');
        }
    });

    // Make absolutely sure there's no margin pushing wp-page down
    wpPage.attr('style', (wpPage.attr('style') || '') + ' margin-top: 0 !important; padding-top: 0 !important;');

    // Optional: add a negative margin just to kill any invisible DOM node spacing
    let heroClass = heroContainer.attr('class').split(' ').filter(c => c.startsWith('elementor-element-'));
    if (heroClass.length > 0) {
        $('head').append(`
            <style>
            .${heroClass[0]} { margin-top: 0px !important; }
            </style>
        `);
    }

} else {
    // Fallback: Just append a very aggressive negative margin
    $('head').append(`
        <style>
        .e-con.e-parent:first-child, .elementor-section:first-child {
            margin-top: 0px !important;
        }
        </style>
    `);
}

fs.writeFileSync('roovon_clone/newkit.creativemox.com/roovon/index.html', $.html());
console.log('Done deep glueing.');
