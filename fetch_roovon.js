const puppeteer = require('puppeteer');
const fs = require('fs');

(async () => {
    console.log('Starting puppeteer...');
    const browser = await puppeteer.launch({ headless: "new" });
    const page = await browser.newPage();

    console.log('Navigating to page...');
    await page.goto('https://newkit.creativemox.com/roovon/', { waitUntil: 'networkidle2' });

    // Scroll to the bottom to trigger lazy loading
    await page.evaluate(async () => {
        await new Promise((resolve, reject) => {
            let totalHeight = 0;
            const distance = 100;
            const timer = setInterval(() => {
                const scrollHeight = document.body.scrollHeight;
                window.scrollBy(0, distance);
                totalHeight += distance;

                if (totalHeight >= scrollHeight) {
                    clearInterval(timer);
                    resolve();
                }
            }, 100);
        });
    });

    console.log('Extracting HTML...');
    const html = await page.content();
    fs.writeFileSync('roovon_clone/newkit.creativemox.com/roovon/index.html', html);
    
    console.log('Saved to roovon_clone/newkit.creativemox.com/roovon/index.html');
    await browser.close();
})();
