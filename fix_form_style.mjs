import fs from 'fs';

let html = fs.readFileSync('roovon_clone/newkit.creativemox.com/roovon/index.html', 'utf8');

// Remove any literal \n that appeared between the two new form field blocks
html = html.replace(/\\n/g, '');

// Now inject CSS to make the new fields (Tipo Cliente select + Localidade input)
// match visually the existing dark-themed Elementor form fields
// The existing fields use transparent bg with white text and subtle borders

const cssfix = `
<style id="form-new-fields-fix">
/* Make Tipo Cliente (Select) and Localidade (Text) match existing dark form fields */
#form-field-tipo-cliente,
#form-field-localidade {
    background-color: transparent !important;
    border: 1px solid rgba(255,255,255,0.15) !important;
    color: #ffffff !important;
    padding: 12px 16px !important;
    font-size: 15px !important;
    width: 100% !important;
    display: block !important;
    border-radius: 3px !important;
    font-family: inherit !important;
    transition: border-color 0.2s ease !important;
    box-sizing: border-box !important;
}
#form-field-tipo-cliente:focus,
#form-field-localidade:focus {
    border-color: rgba(255,255,255,0.4) !important;
    outline: none !important;
}
/* Option items in select box */
#form-field-tipo-cliente option {
    background-color: #0b162c !important;
    color: #fff !important;
}
/* Labels for new fields should match existing label styling */
label[for="form-field-tipo-cliente"],
label[for="form-field-localidade"] {
    color: #ffffff !important;
    font-weight: 700 !important;
    font-size: 15px !important;
    display: block !important;
    margin-bottom: 6px !important;
}
/* Reset any white background bleeding from the parent containers */
.elementor-field-type-select,
.elementor-field-type-text {
    background: transparent !important;
}
.elementor-select-wrapper {
    background: transparent !important;
    position: relative;
}
</style>
`;

// Replace the old broken CSS style block (if any) and inject the new one 
html = html.replace(/<style id="form-tipo-fix">[\s\S]*?<\/style>/g, '');
html = html.replace('</head>', cssfix + '</head>');

fs.writeFileSync('roovon_clone/newkit.creativemox.com/roovon/index.html', html);
console.log('Fixed visual inconsistency of new form fields!');
