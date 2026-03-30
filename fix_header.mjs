import fs from 'fs';
import * as cheerio from 'cheerio';

const htmlStr = fs.readFileSync('roovon_clone/newkit.creativemox.com/roovon/index.html', 'utf8');
const $ = cheerio.load(htmlStr);

// 1. Remove "Project" from nav/footer menus
$('li').each((i, el) => {
    const a = $(el).find('> a, > span');
    if (a.length) {
        const text = a.first().text().trim().toLowerCase();
        if (text === 'project' || text === 'projects') {
            $(el).remove();
        }
    }
});

// 2. Remove "Booking" and "Free Estimate" buttons
$('a').each((i, el) => {
    const text = $(el).text().trim().toLowerCase();
    if (text === 'booking' || text === 'free estimate' || text === 'booking ') {
        // remove the closest widget container so it takes out the whole button
        const widget = $(el).closest('.elementor-widget');
        if (widget.length) {
            widget.remove();
        } else {
            $(el).remove(); // fallback
        }
    }
});

// 3. Fix the gap above header
// Sometimes Elementor adds generic min-height or padding to the header.
// I'll add a CSS rule to forcefully remove top margins and paddings on html, body, and header.
$('head').append(`
<style>
  html, body {
      margin-top: 0 !important;
      padding-top: 0 !important;
  }
  header {
      margin-top: 0 !important;
      padding-top: 0 !important;
  }
  header > .elementor-container, header > .elementor-element > .e-con-inner, header .e-con-boxed {
      margin-top: 0 !important;
      padding-top: 0 !important;
  }
  /* If there is a spacer widget before the nav, hide it */
  .elementor-widget-spacer {
      display: none !important;
  }
</style>
`);

// Just in case there is any other block before the nav container
const navMenu = $('.elementor-widget-nav-menu').first();
if (navMenu.length) {
    const navContainer = navMenu.closest('.e-con.e-parent, .elementor-section');
    if (navContainer.length) {
        // Remove ALL preceding siblings in case `prev()` only removed one and there were others
        navContainer.prevAll().remove();
    }
}

// Remove empty containers inside header
$('header .e-con, header .elementor-section').each((i, el) => {
    if ($(el).text().trim() === '' && $(el).find('img, nav, svg, .elementor-widget').length === 0) {
        // This container is practically empty (only whitespace)
        $(el).remove();
    }
});

fs.writeFileSync('roovon_clone/newkit.creativemox.com/roovon/index.html', $.html());
console.log('Fixed space, removed buttons and Project link.');
