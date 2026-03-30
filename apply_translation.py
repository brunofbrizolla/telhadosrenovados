import json
from bs4 import BeautifulSoup
import re

translations = {
    "Luctus efficitur purus malesuada sed conubia primis. Libero morbi montes orci neque lacinia nibh gravida bibendum litora. Nostra potenti maximus et iaculis ante. Amet eros pulvinar lorem quis sem augue proin dictumst donec parturient curae.": "A Telhados Renovados é especialista na montagem de caleiras, instalação de painéis sanduíche, isolamentos térmicos e impermeabilizações. Atendemos no Grande Porto com qualidade e rigor.",
    "Proin posuere mollis interdum rhoncus vehicula sed enim fermentum ridiculus. Litora pharetra sed sit lectus egestas aenean fermentum. In velit a pulvinar tempus neque.": "Prestamos serviços completos para habitações ou edifícios comerciais. Reparamos telhas partidas, infiltrações e humidades com resposta rápida e orçamento gratuito no Porto.",
    "Eget luctus enim tristique magnis litora. Senectus si tellus natoque adipiscing suscipit mollis ut curabitur. Commodo phasellus lorem eu quis scelerisque hac.": "Construímos e remodelamos telhados do zero utilizando materiais duradouros. Asseguramos um serviço limpo, seguro e com garantia de satisfação para proteção do seu lar.",
    "Gain expert evaluation for your manufacturing or automation needs. We focus on efficiency, safety, and long-term performance.": "Obtenha uma avaliação especializada para as necessidades do seu telhado. Focamo-nos na eficiência térmica, segurança contra humidades e desempenho a longo prazo.",
    "Dignissim vehicula augue finibus eget class scelerisque purus erat natoque hendrerit aptent ex accumsan urna": "Inspeção completa a estruturas de madeira ou metal para garantir a segurança da sua cobertura.",
    "Eleifend curabitur metus nam libero magna mauris consequat sociosqu sagittis pretium ut": "Tratamento antimussgo e impermeabilização profissional para aumentar a durabilidade do seu telhado.",
    "Habitasse habitant platea arcu eu egestas litora sem convallis orci pharetra senectus": "Substituição rápida de telhas cerâmicas, lusa ou painel sanduíche em qualquer configuração.",
    "Sem litora lacus sollicitudin sapien proin aliquam posuere penatibus facilisis": "Equipas experientes e devidamente seguradas para execução de obras rápidas e seguras no Porto.",
    "Feugiat quisque nam lorem justo dis velit magna himenaeos tempus in letius": "Atendimento rápido a urgências de infiltrações e danos causados por intempéries e tempestades.",
    "Copyright © 2026 Roovon, All rights reserved. Present by MoxCreative.": "Copyright © 2026 Telhados Renovados. Todos os direitos reservados. Serviços no Porto, Portugal.",
    "Receive personalized advice without any obligation or commitment.": "Receba aconselhamento personalizado sem qualquer tipo de compromisso.",
    "Si erat luctus viverra netus pulvinar facilisi dis duis maximus": "Excelência e profissionalismo reconhecidos em todo o distrito do Porto.",
    "Reliable Roofing Services Designed For Long Term Performance": "Serviços de Telhados Fiáveis Concebidos Para um Desempenho a Longo Prazo",
    "Roofing Excellence Supported By Strong Performance Metrics": "Excelência em Coberturas Suportada pela Satisfação dos Nossos Clientes",
    "Why Homeowners Trust Roovon For Lasting Protection": "Por Que os Moradores do Porto Confiam na Telhados Renovados Para Proteção Duradoura",
    "Book Professional Roofing Services Online Today": "Agende os Seus Serviços Profissionais de Restauro Hoje",
    "Our Story And Commitment To Roofing Excellence": "A Nossa História e Compromisso com a Excelência de Telhados no Porto",
    "Premium Roofing Services For Modern Buildings": "Construção de Telhados Premium para Edifícios Modernos",
    "Nisl vestibulum per letius in vehicula": "Forte atenção aos detalhes em cada obra realizada.",
    "Request A Free Roofing Consultation": "Solicite uma Inspeção de Telhado Gratuita",
    "Transparent Upfront Pricing": "Preços Transparentes desde o Início",
    "High-Quality Materials Only": "Lidamos Apenas Com Materiais de Alta Qualidade",
    "Eco-Friendly Material Usage": "Utilização de Materiais Ecológicos",
    "Material Quality Standards": "Padrões Rigorosos de Qualidade",
    "Excellent Customer Reviews": "Excelentes Avaliações de Clientes",
    "Fast & Clean Installation": "Instalação Rápida e Limpa",
    "Positive Service Feedback": "Feedback Positivo do Serviço",
    "Lifetime Warranty Options": "Opções de Garantia Prolongada",
    "Project Completion Rate": "Taxa de Conclusão de Projetos",
    "Professional Integrity": "Integridade e Profissionalismo",
    "Waterproofing Systems": "Sistemas de Impermeabilização",
    "Sustainable Practices": "Práticas Sustentáveis na Construção",
    "Trusted Craftsmanship": "Mão de Obra de Confiança",
    "Reliable Performance": "Desempenho Fiável",
    "Innovative Solutions": "Soluções Inovadoras",
    "Free Roof Inspection": "Inspeção Gratuita do Telhado",
    "Technical Expertise": "Experiência Técnica e Liderança",
    "Years of Experience": "Anos de Experiência no Setor",
    "Customer Commitment": "Compromisso Absoluto com o Cliente",
    "Quality Excellence": "Excelência Transparente",
    "Roofing Excellence": "Excelência em Coberturas",
    "Satisfaction Rate": "Taxa de Satisfação",
    "Roof Maintenance": "Limpeza e Manutenção",
    "Terms Conditions": "Termos e Condições",
    "Roof Inspection": "Inspeção e Orçamentação",
    "Talk To Experts": "Fale com os Nossos Especialistas",
    "Warranty Policy": "Política de Garantia",
    "Choose Package": "Escolher Serviço",
    "Privacy Policy": "Política de Privacidade",
    "Cookie Policy": "Política de Cookies",
    "Happy Clients": "Clientes Satisfeitos no Porto",
    "Project Done": "Projetos Concluídos",
    "User Ratings": "Avaliações 5 Estrelas",
    "Our Company": "A Nossa Empresa",
    "About Us": "Sobre Nós",
    "Get Expert Roofing Services Today": "Obtenha o Melhor Serviço Especializado Hoje",
    "Providing expert installation, repair, and maintenance for a safe, durable roof built to last through every season.": "Oferecemos instalação, reparação e manutenção especializada para garantir um telhado seguro, resistente e feito para durar durante todas as estações chuvosas no Porto.",
    "Contact Us": "Contacto"
}

def apply_translations():
    filepath = 'roovon_clone/newkit.creativemox.com/roovon/index.html'
    
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    soup = BeautifulSoup(html, 'lxml')

    count = 0
    # Process text nodes directly
    for tag in soup.find_all(string=True):
        text = tag.string.strip()
        if text in translations:
            tag.string.replace_with(tag.string.replace(tag.string, translations[text]))
            count += 1
            
    # Also iterate over our dictionary for a raw replacement just to be sure some hidden tags don't escape
    html_out = str(soup)
    for en, pt in translations.items():
        if en in html_out:
            html_out = html_out.replace(en, pt)
            
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html_out)
        
    print(f"Applied translation mapping. Direct node hits: {count}")

if __name__ == '__main__':
    apply_translations()
