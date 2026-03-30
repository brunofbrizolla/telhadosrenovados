import fs from 'fs';
import * as cheerio from 'cheerio';

const htmlStr = fs.readFileSync('roovon_clone/newkit.creativemox.com/roovon/index.html', 'utf8');
const $ = cheerio.load(htmlStr);

let sectionsRemoved = 0;

// 1. Remove "Need More Help?" section
$('*').filter((i, el) => $(el).text().includes('Need More Help') && [ 'H1', 'H2', 'H3', 'H4', 'P', 'SPAN', 'DIV' ].includes(el.tagName.toUpperCase())).each((i, el) => {
    // Find the closest full-width elementor container
    const section = $(el).closest('.elementor-element.e-parent, .elementor-element.e-con-full');
    if (section.length) {
        console.log('Found Need More Help section, removing...');
        section.remove();
        sectionsRemoved++;
    }
});

// 2. Remove "Stay Updated With Premium Roofing Insights" section
$('*').filter((i, el) => $(el).text().includes('Stay Updated With Premium Roofing Insights') && [ 'H1', 'H2', 'H3', 'H4', 'P', 'SPAN', 'DIV' ].includes(el.tagName.toUpperCase())).each((i, el) => {
    const section = $(el).closest('.elementor-element.e-parent, .elementor-element.e-con-full');
    if (section.length) {
        console.log('Found Stay Updated section, removing...');
        section.remove();
        sectionsRemoved++;
    }
});

// 3. Keep only Home, Contato, and Serviços in menus and footer
const removeTexts = ['About Us', 'Projects', 'Pages', 'FAQ', 'Blog Archive', 'Single Post', 'Error 404', 'Our Team', 'Pricing Plan', 'Booking', 'Services'];

let linksRenamed = 0;
let linksRemoved = 0;

$('li').each((i, el) => {
    const a = $(el).find('> a, > span'); // Check direct anchor or span inside li
    if (a.length) {
        const text = a.first().text().trim().replace(/[\r\n\t]/g, '');
        
        // Let's normalize text just in case (sometimes it's uppercase)
        const textLower = text.toLowerCase();

        // Items to definitely remove
        if (['about us', 'projects', 'pages', 'faq', 'blog archive', 'single post', 'error 404', 'our team', 'pricing plan', 'booking'].includes(textLower)) {
            $(el).remove();
            linksRemoved++;
        }
        else if (textLower === 'services') {
            a.first().text('Serviços');
            linksRenamed++;
            // Remove its submenus (like drop-downs for services)
            $(el).find('.sub-menu').remove();
            // Remove the dropdown icon if it exists
            $(el).find('a > span > svg').remove();
            $(el).removeClass('menu-item-has-children');
        }
        else if (textLower === 'contact us') {
            a.first().text('Contato');
            linksRenamed++;
        }
        else if (textLower === 'home') {
            // keep home
        }
    }
});

// For any straggler 'Services' or 'Contact Us' outside of lists (like basic links)
$('a, span, h1, h2, h3, h4, p').each((i, el) => {
    if ($(el).children().length === 0) {
        const text = $(el).text().trim().toLowerCase();
        if (text === 'services') {
            $(el).text('Serviços');
        }
        if (text === 'contact us') {
            $(el).text('Contato');
        }
    }
});

fs.writeFileSync('roovon_clone/newkit.creativemox.com/roovon/index.html', $.html());
console.log('Modifications completed! Sections removed:', sectionsRemoved, 'Links removed:', linksRemoved, 'Links renamed:', linksRenamed);
