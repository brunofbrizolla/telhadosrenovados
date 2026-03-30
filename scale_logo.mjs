import fs from 'fs';
import * as cheerio from 'cheerio';

const htmlStr = fs.readFileSync('roovon_clone/newkit.creativemox.com/roovon/index.html', 'utf8');
const $ = cheerio.load(htmlStr);

$('head').append(`
<style id="logo-scale-fix">
    /* Fix the logo being too small because of internal image padding */
    .crh-logo {
        position: relative;
        display: flex;
        align-items: center;
        justify-content: center;
        width: 150px; /* Give it enough horizontal room */
    }
    .crh-logo img {
        height: auto !important;
        width: 100% !important;
        max-height: none !important;
        transform: scale(1.6); /* Scale it up strongly without affecting header height */
        transform-origin: center center;
    }
</style>
`);

// The user screenshot showed the nav menu glued correctly. We just tweak the logo size
fs.writeFileSync('roovon_clone/newkit.creativemox.com/roovon/index.html', $.html());
console.log('Scaled up the logo!');
