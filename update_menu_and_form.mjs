import fs from 'fs';
import * as cheerio from 'cheerio';

const htmlStr = fs.readFileSync('roovon_clone/newkit.creativemox.com/roovon/index.html', 'utf8');
const $ = cheerio.load(htmlStr);

// 1. Update the NAV MENU Dropdown to precisely be the 6 services listed in the section
const newDropdownHtml = `
<ul class="crh-dropdown">
    <li><a href="instalacao-telhados.html">Instalação de Telhados e Coberturas</a></li>
    <li><a href="remodelacao-telhados.html">Remodelação de Telhados</a></li>
    <li><a href="reparacao-telhados.html">Reparação de Telhados</a></li>
    <li><a href="sistemas-impermeabilizacao.html">Sistemas de Impermeabilização</a></li>
    <li><a href="limpeza-telhados.html">Limpeza e Manutenção</a></li>
    <li><a href="inspecao-gratuita.html">Inspeção Gratuita do Telhado</a></li>
</ul>
`;
$('.crh-dropdown').replaceWith(newDropdownHtml);

// 2. Form Fields Modification (Remove Date, Insert Select "Tipo Cliente" & Input "Localidade")

// Determine the date field by placeholder or type
let dateInput = $('input[type="date"], input[placeholder*="Data Preferencial"], input[placeholder*="Date"]');

if (dateInput.length) {
    // If it's wrapped in an elementor-field-group, replace the whole group
    let wrapper = dateInput.closest('.elementor-field-group');
    
    const selectHtml = `
    <div class="elementor-field-type-select elementor-field-group elementor-column elementor-col-100">
        <label for="form-field-tipo-cliente" class="elementor-field-label">Tipo Cliente</label>
        <div class="elementor-field elementor-select-wrapper">
            <select name="form_fields[tipo_cliente]" id="form-field-tipo-cliente" class="elementor-field-textual elementor-size-sm" required="required" aria-required="true" style="width: 100%; border-radius: 3px; font-size: 15px; background: transparent; color: #ffffff; border: 1px solid rgba(255, 255, 255, 0.1); padding: 12px 16px;">
                <option value="" disabled selected style="color:#0b162c">Escolha uma opção</option>
                <option value="Particular" style="color:#0b162c">Particular</option>
                <option value="Condomínio" style="color:#0b162c">Condomínio</option>
                <option value="Empresa" style="color:#0b162c">Empresa</option>
            </select>
        </div>
    </div>
    `;

    const localidadeHtml = `
    <div class="elementor-field-type-text elementor-field-group elementor-column elementor-col-100">
        <label for="form-field-localidade" class="elementor-field-label">Localidade</label>
        <input size="1" type="text" name="form_fields[localidade]" id="form-field-localidade" class="elementor-field elementor-size-sm  elementor-field-textual" placeholder="A sua localidade (Ex: Porto, Maia...)" required="required" aria-required="true" style="width: 100%; background: transparent; border: 1px solid rgba(255, 255, 255, 0.1); color: #ffffff; padding: 12px 16px; border-radius: 3px;">
    </div>
    `;

    if (wrapper.length) {
        wrapper.replaceWith(selectHtml + '\\n' + localidadeHtml);
    } else {
        let prevLabel = dateInput.prev('label');
        if (prevLabel.length) prevLabel.remove();
        dateInput.replaceWith(selectHtml + '\\n' + localidadeHtml);
    }
}

// Add CSS marker to make sure the dropdown arrow shows up if missing
$('head').append(`
<style id="form-tipo-fix">
    .elementor-select-wrapper::before {
        content: "\\25BC";
        position: absolute;
        right: 15px;
        top: 50%;
        transform: translateY(-50%);
        color: rgba(255, 255, 255, 0.5);
        pointer-events: none;
        font-size: 12px;
    }
    .elementor-select-wrapper { position: relative; }
</style>
`);

fs.writeFileSync('roovon_clone/newkit.creativemox.com/roovon/index.html', $.html());
console.log('Successfully updated the nav menu dropdown and injected Tipo Cliente + Localidade in the form!');
