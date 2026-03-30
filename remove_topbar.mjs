import fs from 'fs';
import * as cheerio from 'cheerio';

const htmlStr = fs.readFileSync('roovon_clone/newkit.creativemox.com/roovon/index.html', 'utf8');
const $ = cheerio.load(htmlStr);

// Find the nav menu wrapper
const navMenu = $('.elementor-widget-nav-menu').first();
if (navMenu.length) {
    // Nav menu is usually inside a container (.e-con), and the topbar is a separate container BEFORE it.
    // The top bar might be a sibling container to the nav menu's container, or they might all be inside a single header parent.
    const header = navMenu.closest('header');
    if (header.length) {
        console.log('Found Header!');
        // Let's identify the main header container (the one containing the nav)
        const navContainer = navMenu.closest('.e-con.e-parent, .elementor-section');
        
        if (navContainer.length) {
            console.log('Found Nav Container! Siblings before it:');
            let prev = navContainer.prev();
            let count = 0;
            while(prev.length) {
                console.log('- Preceding element class:', prev.attr('class'));
                prev.remove();
                prev = navContainer.prev();
                count++;
            }
            console.log(`Removed ${count} preceding siblings of the nav container.`);
        }
    }
}

fs.writeFileSync('roovon_clone/newkit.creativemox.com/roovon/index.html', $.html());
console.log('Done!');
