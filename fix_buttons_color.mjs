import fs from 'fs';
import * as cheerio from 'cheerio';

const htmlStr = fs.readFileSync('roovon_clone/newkit.creativemox.com/roovon/index.html', 'utf8');
const $ = cheerio.load(htmlStr);

// A foolproof way is to inject a new <style> block that guarantees these hover states work with !important.
$('head').append(`
<style id="btn-color-fix">
  .crh-btn {
      color: #ffffff !important;
  }
  .crh-btn-navy {
      color: #ffffff !important;
  }
  .crh-btn-navy:hover {
      background: #ffffff !important;
      color: #0d2a45 !important;
  }
  .crh-btn-whatsapp {
      color: #ffffff !important;
  }
  .crh-btn-whatsapp:hover {
      color: #ffffff !important;
  }
</style>
`);

fs.writeFileSync('roovon_clone/newkit.creativemox.com/roovon/index.html', $.html());
console.log('Injected important hover color fixes for buttons');
