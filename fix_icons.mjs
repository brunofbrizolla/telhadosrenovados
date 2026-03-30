import fs from 'fs';
import * as cheerio from 'cheerio';

const htmlStr = fs.readFileSync('roovon_clone/newkit.creativemox.com/roovon/index.html', 'utf8');
const $ = cheerio.load(htmlStr);

// These small red squares are broken icon elements from Elementor's icon widget
// The icon fonts (eicons, FontAwesome) are not available in the static clone
// Strategy: Replace each broken icon <i> with a clean SVG appropriate for each service card
// Or simply hide the broken icon boxes and keep titles/text

const serviceIcons = {
    // Map common eicons to SVG icons relevant to roofing
    'default': `<svg viewBox="0 0 24 24" width="28" height="28" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path><polyline points="9 22 9 12 15 12 15 22"></polyline></svg>`,
};

// Find all broken icon elements (eicon classes or fa classes with red square appearance)
let iconCount = 0;
$('i[class*="eicon"], i[class*="fa "], i[class*="fas "], i[class*="far "], i.fa, span.eicon, i[class*="eicons-"]').each((i, el) => {
    const svgIcon = serviceIcons['default'];
    // We replace the <i> with the SVG wrapped in a span maintaining the styling
    $(el).replaceWith(`<span class="crh-icon-svg" style="display:inline-flex;align-items:center;justify-content:center;color:currentColor;">${svgIcon}</span>`);
    iconCount++;
});

// Also inject a CSS fix: hide any remaining broken icon placeholder boxes
$('head').append(`
<style id="fix-broken-icons">
    /* Hide any remaining broken icon glyphs that show as empty squares */
    i[class*="eicon-"]:empty,
    i[class*="fa-"]:empty,
    span.eicon:empty {
        display: none !important;
    }
    
    /* Make sure our SVG icons inherit the color */
    .crh-icon-svg svg {
        width: 28px;
        height: 28px;
    }
    
    /* The icon box wrapper inside service cards — make icons look proper */
    .elementor-icon-box-icon .crh-icon-svg {
        width: 60px;
        height: 60px;
        background: #c0392b;
        border-radius: 4px;
        display: flex !important;
        align-items: center;
        justify-content: center;
        color: #ffffff;
    }
    
    /* Also fix icon on stats counters area */
    .elementor-counter .crh-icon-svg {
        color: #c0392b;
    }
</style>
`);

fs.writeFileSync('roovon_clone/newkit.creativemox.com/roovon/index.html', $.html());
console.log(`Replaced ${iconCount} broken icon elements with SVG house icons!`);
