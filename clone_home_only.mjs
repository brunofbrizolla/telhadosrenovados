import scrape from 'website-scraper';

const options = {
  urls: ['https://newkit.creativemox.com/roovon/'],
  directory: './temp_home_clone',
  recursive: false,
  maxDepth: 1,
  filenameGenerator: 'bySiteStructure',
  request: {
    headers: {
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
  }
};

console.log('Starting single-page clone of roovon home...');
scrape(options).then((result) => {
  console.log('Successfully cloned to ./temp_home_clone');
}).catch((err) => {
  console.error('Error:', err);
});
