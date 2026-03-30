import scrape from 'website-scraper';

const options = {
  urls: ['https://newkit.creativemox.com/roovon/'],
  directory: './roovon_clone',
  recursive: false,
  filenameGenerator: 'bySiteStructure',
  request: {
    headers: {
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
  }
};

console.log('Starting website clone of https://newkit.creativemox.com/roovon/ to ./roovon_clone');
scrape(options).then((result) => {
  console.log('Successfully completed website clone!');
}).catch((err) => {
  console.error('An error occurred while cloning the website:', err);
});
