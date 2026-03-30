import fs from 'fs';
import * as cheerio from 'cheerio';

const htmlStr = fs.readFileSync('roovon_clone/newkit.creativemox.com/roovon/index.html', 'utf8');
const $ = cheerio.load(htmlStr);

// 1. Completely remove the <header> element
$('header').remove();

// 2. Sometimes Elementor uses <div data-elementor-type="header"> instead of <header>
$('[data-elementor-type="header"]').remove();

// 3. Remove .elementor-location-header if it exists
$('.elementor-location-header').remove();

// 4. In WordPress, body often has margin-top for the admin bar.
// And Elementor sections might have default top margins.
$('head').append(`
<style id="nuke-top-space">
  html {
      margin-top: 0px !important;
      padding-top: 0px !important;
  }
  body, .elementor-page {
      margin-top: 0px !important;
      padding-top: 0px !important;
      background-color: transparent !important;
  }
  #wpadminbar {
      display: none !important;
  }
</style>
`);

// 5. Look for any empty divs before the actual content and remove them.
// The main content in Elementor is usually inside <main> or <div data-elementor-type="wp-page">
// Let's find the first `.e-con-full` or `.elementor-section` and remove any sibling before it that is empty.
const firstMainSection = $('[data-elementor-type="wp-page"] > .elementor-element').first();
if (firstMainSection.length) {
    firstMainSection.prevAll().remove();
    console.log('Removed preceding elements before the main Elementor content wrapper.');
}

// 6. Also check if the wp-page wrapper itself has top padding/margin
$('[data-elementor-type="wp-page"]').attr('style', (i, val) => (val || '') + ' margin-top: 0px !important; padding-top: 0px !important;');

fs.writeFileSync('roovon_clone/newkit.creativemox.com/roovon/index.html', $.html());
console.log('Removed header completely and fixed all top spaces.');
