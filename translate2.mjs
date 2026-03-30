import fs from 'fs';
let html = fs.readFileSync('roovon_clone/newkit.creativemox.com/roovon/index.html', 'utf8');

const t = {
    'Discover more': 'Saiba Mais',
    'Read More': 'Ler Mais',
    'Explore Our Services': 'Explore os Nossos Serviços',
    'Why Choose Us': 'Por Que Nos Escolher',
    'Working Process': 'O Nosso Processo',
    'Residential Roofing': 'Telhados Residenciais no Porto',
    'Commercial Roofing': 'Coberturas Comerciais',
    'View Details': 'Ver Detalhes',
    'Get A Quote': 'Pedir Orçamento',
    'Our Services': 'Nossos Serviços',
    'Learn More': 'Saber Mais',
    'Testimonials': 'Testemunhos',
    'What They Say': 'O Que Dizem os Nossos Clientes',
    'Pricing Plan': 'Preços',
    'Send Message': 'Enviar Mensagem',
    'Latest News': 'Últimas Novidades',
    'Follow Us': 'Siga-nos',
    'Quick Links': 'Links Rápidos',
    'Contact Info': 'Informações de Contacto',
    'Location': 'Localização',
    'Find Us Here': 'Encontre-nos no Porto'
};

for (const [en, pt] of Object.entries(t)) {
    // Regex that catches the text inside tags even if there's minor whitespace
    const regex = new RegExp(`>\\s*${en}\\s*<`, 'gi');
    html = html.replace(regex, `>${pt}<`);
}

// Update the placeholder html title and lang
html = html.replace('lang="en-US"', 'lang="pt-PT"');
html = html.replace('<title>Roovon</title>', '<title>Telhados Renovados - Instalação e Reparação de Telhados no Porto</title>');

// Generic replacement for placeholder numbers
html = html.replace(/(\+0|[0-9]{3})\s?[0-9]{3}\s?[0-9]{4}/g, '+351 937 065 056');

fs.writeFileSync('roovon_clone/newkit.creativemox.com/roovon/index.html', html);
console.log('Finished pass 2 of translation!');
