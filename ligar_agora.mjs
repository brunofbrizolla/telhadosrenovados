import fs from 'fs';
import * as cheerio from 'cheerio';

const htmlStr = fs.readFileSync('roovon_clone/newkit.creativemox.com/roovon/index.html', 'utf8');
const $ = cheerio.load(htmlStr);

const phone = 'tel:+351937065056';
let count = 0;

// Find all links and buttons with Saiba/Saber/Ligar text
$('a, button').each((i, el) => {
    const txt = $(el).text().trim();
    if (/^(Saiba Mais|Saber Mais|Learn More|Read More|Ver Detalhes|Ver Mais)$/i.test(txt)) {
        // Change text to Ligar Agora
        // Keep any SVG icon children, only change the text node
        $(el).contents().filter(function() {
            return this.type === 'text';
        }).first().replaceWith('Ligar Agora ');
        
        // Also update the href to call the phone
        if ($(el).is('a')) {
            $(el).attr('href', phone);
        }
        count++;
    }
});

fs.writeFileSync('roovon_clone/newkit.creativemox.com/roovon/index.html', $.html());
console.log(`Changed ${count} buttons to "Ligar Agora" linking to +351 937 065 056!`);
