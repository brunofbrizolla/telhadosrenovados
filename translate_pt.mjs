import fs from 'fs';
import * as cheerio from 'cheerio';

const htmlStr = fs.readFileSync('roovon_clone/newkit.creativemox.com/roovon/index.html', 'utf8');
const $ = cheerio.load(htmlStr);

// A mapping of english phrases found in the Roovon template to PT-PT equivalents with SEO
const translations = {
    "Expert Roofing Services For Modern Buildings": "Serviços Especializados em Telhados e Coberturas no Porto",
    "Our certified professionals provide reliable roofing solutions for residential and commercial projects.": "Os nossos profissionais certificados oferecem soluções fiáveis e definitivas para telhados em projetos residenciais e comerciais no Porto, Portugal.",
    "Discover more": "Saiba Mais",
    "Book Professional Roofing Service Now": "Solicite um Orçamento Gratuito",
    "Full Name": "Nome Completo",
    "Enter Your Full Name": "Insira o seu Nome Completo",
    "Phone Number": "Contacto Telefónico",
    "Enter Your Phone Number": "Insira o seu Telemóvel/WhatsApp",
    "Email": "E-mail",
    "Enter Your Email Address": "Insira o seu Endereço de E-mail",
    "Date": "Data Preferencial",
    "Select Service": "Selecione o Serviço",
    "Roof Installation": "Instalação de Telhados e Coberturas",
    "Roof Replacement": "Remodelação de Telhados",
    "Roof Repair": "Reparação de Telhados",
    "Roof Maintanance": "Limpeza e Manutenção de Telhados",
    "Schedule Free Consultation": "Agendar Diagnóstico Gratuito",
    "ABOUT US": "A NOSSA EMPRESA",
    "Building Trust Through Quality Roofing Solutions": "Construímos Confiança Através de Excelência em Telhados no Porto",
    "Eget ullamcorper litora pellentesque ad a justo sagittis suspendisse augue turpis. Vel porttitor penatibus lobortis nostra sociosqu. Fusce tristique taciti pulvinar vel porttitor sapien eros sed. Id fames quam elit nam lobortis.": "Somos uma empresa de referência no Porto, especializada na instalação, reparação e limpeza de telhados. Com foco rigoroso na qualidade e segurança, os nossos especialistas garantem durabilidade contra o clima rigoroso de Portugal.",
    "Provide Best Roofing Services": "Os Melhores Serviços de Coberturas da Região",
    "Quality Materials": "Materiais de Primeira Qualidade",
    "Expert Workmanship": "Mão de Obra Especializada",
    "15+": "15+",
    "Years Of Experience": "Anos de Experiência"
};

// 1. Traverse all text nodes and translate matching ones
function replaceTextNodes(node) {
    if (node.type === 'text') {
        let text = node.data;
        let normalizedText = text.trim();
        
        // Exact matches
        if (translations[normalizedText]) {
            node.data = text.replace(normalizedText, translations[normalizedText]);
        } else {
            // Partial heuristic replacements for lorem ipsum or generic texts not perfectly matching
            if (normalizedText.toLowerCase().includes('lorem ipsum')) {
                node.data = "Oferecemos os melhores serviços de isolamento térmico e impermeabilização no Porto, focados na máxima eficiência do seu telhado.";
            }
        }
    } else {
        if (node.children) {
            node.children.forEach(replaceTextNodes);
        }
    }
}

// Start recursive text replacement on the body
$('body').each(function() {
    replaceTextNodes(this);
});

// Update inputs placeholder text
$('input, textarea').each((i, el) => {
    const ph = $(el).attr('placeholder');
    if (ph && translations[ph]) {
        $(el).attr('placeholder', translations[ph]);
    }
});

// Update specific elements if recursive failed (like inside spans)
for (const [en, pt] of Object.entries(translations)) {
    // Basic catch-all to replace text anywhere
    $('*').contents().filter(function() {
        return this.type === 'text' && this.data.trim() === en;
    }).replaceWith(pt);
}

// 2. Replace all phones, emails and WA links
$('a').each((i, el) => {
    let href = $(el).attr('href');
    if (href) {
        if (href.startsWith('tel:')) {
            $(el).attr('href', 'tel:+351937065056');
        } else if (href.startsWith('mailto:')) {
            $(el).attr('href', 'mailto:contacto@telhadosrenovados.pt');
        } else if (href.includes('wa.me') || href.includes('whatsapp.com')) {
            $(el).attr('href', 'https://wa.me/351937065056');
        }
    }
});

// Replace visual phone numbers and emails anywhere in the text
let updatedHtml = $.html();
updatedHtml = updatedHtml.replace(/\+1[ \-\.]?\d{3}[ \-\.]?\d{3}[ \-\.]?\d{4}/g, '+351 937 065 056');
updatedHtml = updatedHtml.replace(/(contact|info)@roovon\.com/gi, 'contacto@telhadosrenovados.pt');

fs.writeFileSync('roovon_clone/newkit.creativemox.com/roovon/index.html', updatedHtml);
console.log('Finished comprehensive translation to PT-PT and injected SEO/Contacts!');
