import fs from 'fs';
import * as cheerio from 'cheerio';

const htmlStr = fs.readFileSync('roovon_clone/newkit.creativemox.com/roovon/index.html', 'utf8');
const $ = cheerio.load(htmlStr);

// 1. Fix "Saiba Mais" / "Saber Mais" everywhere they still appear as text nodes
let btnCount = 0;
$('a, button').each((i, el) => {
    const $el = $(el);
    const fullText = $el.text().trim();
    if (/^(Saiba Mais|Saber Mais|Learn More|Read More|Ver Detalhes)$/i.test(fullText)) {
        // Replace only the text node, keep SVG icons
        $el.contents().filter(function() { return this.type === 'text'; }).each(function() {
            this.data = 'Ligar Agora ';
        });
        if ($el.is('a')) $el.attr('href', 'tel:+351937065056');
        btnCount++;
    }
});

// 2. Add WhatsApp button to the mobile menu (inside .crh-actions which opens on hamburger)
// .crh-actions already has both buttons for desktop. On mobile the actions div opens.
// The WhatsApp button is already there (.crh-btn-whatsapp).
// But if the user only sees the hamburger and not the actions — we also add a sticky WA button on mobile nav.

// Inject a floating mobile-only WhatsApp button at the body level
if ($('#mobile-wa-fab').length === 0) {
    $('body').append(`
    <!-- Mobile WhatsApp Floating Button -->
    <a id="mobile-wa-fab" href="https://wa.me/351937065056" target="_blank" aria-label="WhatsApp" rel="noopener">
        <svg viewBox="0 0 448 512" width="26" height="26">
            <path fill="currentColor" d="M380.9 97.1C339 55.1 283.2 32 223.9 32c-122.4 0-222 99.6-222 222 0 39.1 10.2 77.3 29.6 111L0 480l117.7-30.9c32.4 17.7 68.9 27 106.1 27h.1c122.3 0 224.1-99.6 224.1-222 0-59.3-23.2-115-65.1-157zM223.9 437c-33.5 0-66.3-8.8-94.9-25.5l-6.8-4-70.5 18.5 18.8-68.8-4.4-7c-18.4-29.2-28.1-63.1-28.1-98.3 0-103.1 84.1-187.2 187.3-187.2 50 0 97 19.5 132.3 54.8 35.3 35.3 54.8 82.2 54.8 132.3 0 103.3-84.1 187.2-187.1 187.2zm102.8-140.8c-5.6-2.8-33.2-16.4-38.3-18.3-5.1-1.9-8.9-2.8-12.6 2.8-3.7 5.6-14.4 18.3-17.6 22.1-3.2 3.7-6.5 4.2-12.1 1.4-5.6-2.8-23.8-8.8-45.3-27.9-16.7-14.9-28-33.3-31.3-38.9-3.2-5.6-.3-8.6 2.4-11.4 2.5-2.5 5.6-6.5 8.4-9.7 2.8-3.2 3.7-5.6 5.6-9.3 1.9-3.7.9-6.9-.5-9.7-1.4-2.8-12.6-30.4-17.3-41.6-4.6-10.9-9.2-9.4-12.6-9.6-3.2-.2-6.9-.2-10.6-.2-3.7 0-9.7 1.4-14.8 6.9-5.1 5.6-19.4 19-19.4 46.3 0 27.3 19.9 53.7 22.6 57.4 2.8 3.7 39.1 59.7 94.8 83.8 13.2 5.7 23.5 9.1 31.6 11.7 13.3 4.2 25.4 3.6 34.9 2.2 10.6-1.6 33.2-13.6 37.9-26.7 4.7-13.1 4.7-24.3 3.3-26.7-1.4-2.4-5.1-3.7-10.7-6.5z"/>
        </svg>
    </a>
    <style id="mobile-wa-fab-css">
        /* Floating WhatsApp button — shows on all screens */
        #mobile-wa-fab {
            position: fixed;
            bottom: 22px;
            right: 22px;
            width: 56px;
            height: 56px;
            background: #25D366;
            color: #fff;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            box-shadow: 0 4px 16px rgba(37,211,102,0.45);
            z-index: 999998;
            text-decoration: none;
            transition: transform 0.2s ease, box-shadow 0.2s ease;
        }
        #mobile-wa-fab:hover {
            transform: scale(1.1);
            box-shadow: 0 6px 22px rgba(37,211,102,0.6);
        }
        /* On desktop, hide the FAB because the nav already has the WA button */
        @media (min-width: 901px) {
            #mobile-wa-fab {
                display: none;
            }
        }
    </style>
    `);
}

fs.writeFileSync('roovon_clone/newkit.creativemox.com/roovon/index.html', $.html());
console.log(`Ligar Agora: ${btnCount} buttons updated. WhatsApp FAB injected for mobile!`);
