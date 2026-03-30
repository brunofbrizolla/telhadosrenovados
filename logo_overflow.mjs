import fs from 'fs';

let html = fs.readFileSync('roovon_clone/newkit.creativemox.com/roovon/index.html', 'utf8');

// Remove existing logo scale fix style
html = html.replace(/<style id="logo-scale-fix">[\s\S]*?<\/style>/g, '');
html = html.replace(/<style id="shrink-nav-50">[\s\S]*?<\/style>/g, '');

// Inject the overflow logo effect + keep nav slim
const css = `
<style id="logo-overflow-effect">
    /* Keep nav bar slim */
    #custom-roovon-header {
        overflow: visible !important; /* Allow the logo to bleed out */
        position: sticky !important;
        top: 0 !important;
        z-index: 99999 !important;
    }

    /* Main row stays compact */
    .crh-container {
        padding: 4px 20px !important;
        min-height: 48px !important;
        align-items: center !important;
        position: relative !important;
        overflow: visible !important;
    }

    /* Logo wrapper: overflow it above and below the nav */
    .crh-logo {
        position: relative !important;
        z-index: 100000 !important;
        overflow: visible !important;
        display: flex !important;
        align-items: center !important;
    }

    /* The actual logo image: taller than the nav bar itself */
    .crh-logo img {
        height: 90px !important;        /* Bigger than the nav row */
        width: auto !important;
        max-height: none !important;
        transform: none !important;
        /* Float it so it sticks out below the white bar slightly */
        margin-top: 20px !important;   /* Push it down so it bleeds below the bar */
        /* Add drop shadow so it "pops" out visually */
        filter: drop-shadow(0px 4px 6px rgba(0,0,0,0.18)) !important;
        display: block !important;
    }

    /* Prevent the logo from pushing adjacent menu items up */
    .crh-nav,
    .crh-actions {
        align-self: center !important;
    }
</style>
`;

html = html.replace('</head>', css + '</head>');

fs.writeFileSync('roovon_clone/newkit.creativemox.com/roovon/index.html', html);
console.log('Applied overflow logo effect!');
