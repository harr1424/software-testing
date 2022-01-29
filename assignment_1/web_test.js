const puppeteer = require('puppeteer');

// Create a browser object
(async () => {
  const browser = await puppeteer.launch({
    headless: false,
    defaultViewport: {
      width: 1200,
      height: 820,
    },
    slowMo: 500,
  });

  // Obtain a screen shot of the home page of former project
  // This verifies that this test can load the page and run a basic test
  const main_page = await browser.newPage();
  await main_page.goto('http://webdev.cs.umt.edu/~jh243191/Resort_Database/home.html');
  await main_page.screenshot({ path: 'screenshot.png'});

  await browser.close();
}) ();

// Verify all links contained on the home page are working as expected
// Note that any pages that interact with the MariaDB used to power
// the backend of this project output an error: "ERROR COULD NOT CONNECT"
// And so testing should detect this, and output a list of pages
// whoose boday contains the word "ERROR"
