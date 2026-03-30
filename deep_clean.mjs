import fs from 'fs';
import * as cheerio from 'cheerio';

const htmlStr = fs.readFileSync('roovon_clone/newkit.creativemox.com/roovon/index.html', 'utf8');
const $ = cheerio.load(htmlStr);

// 1. Remove ANY li that contains the text 'Project' (case insensitive)
$('li').each((i, el) => {
    const text = $(el).text().trim().toLowerCase();
    if (text.includes('project')) {
        $(el).remove();
    }
});

// 2. Remove ANY buttons containing 'Booking' or 'Free Estimate'
$('a').each((i, el) => {
    const text = $(el).text().trim().toLowerCase();
    if (text.includes('booking') || text.includes('free estimate') || text.includes('free') || text.includes('estimate')) {
        // In Elementor, buttons are wrapped by .elementor-widget. Let's remove the widget.
        const widget = $(el).closest('.elementor-widget, .elementor-element');
        if (widget.length) {
            // Find the highest elementor-widget wrapper so we don't accidentally leave an empty container
            if (widget.hasClass('elementor-widget')) {
                widget.remove();
            } else {
                widget.remove();
            }
        } else {
            $(el).remove();
        }
    }
});

// 3. To remove the white space above the menu.
// Let's identify the wrapper that holds the logo and nav menu.
const navMenu = $('.elementor-widget-nav-menu').first();
if (navMenu.length) {
    const navContainer = navMenu.closest('.e-con.e-parent, .elementor-section, .elementor-element');
    if (navContainer.length) {
        // remove any preceding siblings of the container inside the header!
        navContainer.prevAll().remove();
        
        // It's possible the header itself has a top padding. We inject an inline style to the nav container
        // to strictly force 0 padding on top, and do the same for the header.
        const header = navContainer.closest('header');
        if (header.length) {
            header.attr('style', (header.attr('style') || '') + ' margin-top: 0 !important; padding-top: 0 !important;');
        }
        navContainer.attr('style', (navContainer.attr('style') || '') + ' margin-top: 0 !important; padding-top: 0 !important;');
        navContainer.css({ 'margin-top': '0', 'padding-top': '0' });
    }
}

// Ensure the CSS override is in the <head>
$('head').append(`
<style id="custom-header-fix">
  html, body {
      margin-top: 0px !important;
      padding-top: 0px !important;
  }
  header, [data-elementor-type="header"], .elementor-location-header {
      margin-top: 0px !important;
      padding-top: 0px !important;
  }
  /* Target the exact specific container inside the header */
  header .e-con, header .e-con-boxed, header .e-con-inner, header .elementor-widget-wrap {
      padding-top: 0px !important;
      margin-top: 0px !important;
  }
</style>
`);

fs.writeFileSync('roovon_clone/newkit.creativemox.com/roovon/index.html', $.html());
console.log('Deep cleaner run completed!');
