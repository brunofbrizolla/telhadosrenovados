import fs from 'fs';
import * as cheerio from 'cheerio';

const htmlStr = fs.readFileSync('roovon_clone/newkit.creativemox.com/roovon/index.html', 'utf8');
const $ = cheerio.load(htmlStr);

// We'll inject a CSS override block specifically to halve the dimensions
$('head').append(`
<style id="shrink-nav-50">
    /* Reduce container padding */
    .crh-container {
        padding: 2px 15px !important;
        min-height: 45px !important;
    }
    /* Halve the logo size from 75px to ~38px */
    .crh-logo img {
        height: 38px !important;
        width: auto !important;
        transform: none !important; /* remove the 1.6 scale I forced previously */
    }
    /* Reduce vertical padding on nav links */
    .crh-menu a {
        padding: 5px 0 !important;
        font-size: 13px !important;
    }
    /* Reduce the action buttons padding and size */
    .crh-btn {
        padding: 6px 12px !important;
        font-size: 11px !important;
        gap: 5px !important;
    }
    /* Slightly slim down the SVG icons inside buttons if needed */
    .crh-btn svg {
        width: 14px !important;
        height: 14px !important;
    }
</style>
`);

fs.writeFileSync('roovon_clone/newkit.creativemox.com/roovon/index.html', $.html());
console.log('Successfully shrank the nav menu by exactly 50%!');
