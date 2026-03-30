const fs = require('fs');
const path = require('path');

function processDir(dir) {
    const files = fs.readdirSync(dir);
    for (const file of files) {
        const fullPath = path.join(dir, file);
        if (fs.statSync(fullPath).isDirectory()) {
            processDir(fullPath);
        } else if (fullPath.endsWith('.html')) {
            let content = fs.readFileSync(fullPath, 'utf8');
            
            // Remove dropdown items
            content = content.replace(/.*<li.*<a class="dropdown-item" href="(?:\.\.\/)?pladur-pintura\.html".*?<\/li>\r?\n/gi, '');
            content = content.replace(/.*<li.*<a class="dropdown-item" href="(?:\.\.\/)?manutencao-telhados\.html".*?<\/li>\r?\n/gi, '');
            
            // Remove options in select
            content = content.replace(/.*<option value="PLADUR e\/ou Pintura Interior".*?<\/option>\r?\n/gi, '');
            
            // Remove grid service blocks
            content = content.replace(/([ \t]*)<div class="col-lg-4 col-sm-12">\s*<svg[^>]*>[\s\S]*?(?:pladur-pintura\.html)[\s\S]*?<!-- \/\.col-lg-4 -->\r?\n?/gi, '');
            content = content.replace(/([ \t]*)<div class="col-lg-4 col-sm-12">\s*<svg[^>]*>[\s\S]*?(?:manutencao-telhados\.html)[\s\S]*?<!-- \/\.col-lg-4 -->\r?\n?/gi, '');

            // Remove inline references
            content = content.replace(/ \(<a href="#">.*Reparação de Pladur e Pintura de Interiores.*?<\/a>\)/gi, '');
            content = content.replace(/<a href="(?:\.\.\/)?manutencao-telhados\.html">([\s\S]*?)<\/a>/gi, '$1');

            fs.writeFileSync(fullPath, content);
        }
    }
}

const targetDir = path.join(__dirname, 'telhaverde_clone/telhaverde.pt');
processDir(targetDir);

// Finally delete the files
['pladur-pintura.html', 'manutencao-telhados.html'].forEach(f => {
    try {
        fs.unlinkSync(path.join(targetDir, f));
        console.log(`Deleted ${f}`);
    } catch (e) {
        console.log(`Could not delete ${f}:`, e.message);
    }
});
