import fs from 'fs';

let html = fs.readFileSync('roovon_clone/newkit.creativemox.com/roovon/index.html', 'utf8');

// Inject a CSS fix: switch from sticky to fixed and add a body padding to compensate
const css = `
<style id="fixed-header-fix">
    /* Use position:fixed instead of sticky — more reliable, always sticks to top */
    #custom-roovon-header {
        position: fixed !important;
        top: 0 !important;
        left: 0 !important;
        right: 0 !important;
        width: 100% !important;
        z-index: 99999 !important;
    }

    /* Add padding to body so section below doesn't hide under the fixed header */
    body {
        padding-top: 0px !important; /* The hero section already starts here, so 0 is fine */
    }

    /* Ensure the first section (hero/capa) starts right below the fixed header */
    /* We adjust it with a margin equal to the header height */
    body > *:not(#custom-roovon-header):not(style):not(script):first-of-type,
    [data-elementor-type="wp-page"] {
        margin-top: 0 !important;
    }

    /* Compensate for fixed header: push the whole page content down by the header height */
    /* Header is ~48px when scrolled, ~95px when at top (because of logo overflow) */
    /* We add a spacer via ::before on body as a hack */
    body::before {
        content: '';
        display: block;
        height: 48px; /* Match the compact header height */
    }
</style>
`;

// Remove any old fixed/sticky overrides
html = html.replace(/<style id="fixed-header-fix">[\s\S]*?<\/style>/g, '');
html = html.replace('</head>', css + '</head>');

fs.writeFileSync('roovon_clone/newkit.creativemox.com/roovon/index.html', html);
console.log('Fixed: header now uses position:fixed — always stays on top!');
