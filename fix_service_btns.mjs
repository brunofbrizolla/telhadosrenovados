import fs from 'fs';
import * as cheerio from 'cheerio';

const htmlStr = fs.readFileSync('roovon_clone/newkit.creativemox.com/roovon/index.html', 'utf8');
const $ = cheerio.load(htmlStr);

// Map service names to their pages
const servicePages = {
    'Instalação de Telhados e Coberturas': 'instalacao-telhados.html',
    'Remodelação de Telhados': 'remodelacao-telhados.html',
    'Reparação de Telhados': 'reparacao-telhados.html',
    'Sistemas de Impermeabilização': 'sistemas-impermeabilizacao.html',
    'Limpeza e Manutenção': 'limpeza-telhados.html',
    'Inspeção e Orçamentação': 'inspecao-gratuita.html',
};

// Find the service cards section (icon-box widgets in Elementor)
// Each card has a heading (h3 or .elementor-icon-box-title) and a "Ligar Agora" read-more link
// Strategy: find each icon-box widget, get its title, find the "Ligar Agora" link inside it
// and replace it with "Saiba Mais" linking to the right page

$('.elementor-widget-icon-box').each((i, widget) => {
    const $widget = $(widget);
    
    // Get the service title from the card
    const title = $widget.find('.elementor-icon-box-title').text().trim() ||
                  $widget.find('h3').text().trim() ||
                  $widget.find('h4').text().trim();
    
    // Find the matching page
    let targetPage = '#';
    for (const [service, page] of Object.entries(servicePages)) {
        if (title.includes(service.substring(0, 15))) {
            targetPage = page;
            break;
        }
    }
    
    // Find the "Ligar Agora" button/link inside this card
    $widget.find('a').each((j, link) => {
        const linkText = $(link).text().trim();
        if (linkText.includes('Ligar Agora') || linkText.includes('Saiba Mais') || linkText.includes('Saber Mais')) {
            // Replace the text and href
            $(link).contents().filter(function() { return this.type === 'text'; }).each(function() {
                this.data = 'Saiba Mais ';
            });
            $(link).attr('href', targetPage);
        }
    });
});

// Also find any remaining links in the services section that might have different markup
// Fallback: look at the surrounding text blocks for each "Ligar Agora" and check if near a service name
const serviceOrder = Object.values(servicePages);
let serviceIdx = 0;

$('a').each((i, el) => {
    const txt = $(el).text().trim();
    // Only target "Ligar Agora" buttons that are inside service-related widgets
    if (txt === 'Ligar Agora ') {
        const closestSection = $(el).closest('.elementor-widget-icon-box, .elementor-widget-button');
        if (closestSection.length && serviceIdx < serviceOrder.length) {
            $(el).contents().filter(function() { return this.type === 'text'; }).each(function() {
                this.data = 'Saiba Mais ';
            });
            $(el).attr('href', serviceOrder[serviceIdx]);
            serviceIdx++;
        }
    }
});

fs.writeFileSync('roovon_clone/newkit.creativemox.com/roovon/index.html', $.html());
console.log('Service cards buttons reverted to "Saiba Mais" with correct page links!');
