const puppeteer = require('puppeteer');

// Create a browser object
(async () => {
  const browser = await puppeteer.launch({
    defaultViewport: {
      width: 1200,
      height: 820,
    },
  });

  // TEST ONE: Obtain a screen shot of the home page of a former project.
  // This verifies that the testing software can load the page and run a basic test.
  const page = await browser.newPage();
  await page.goto('http://webdev.cs.umt.edu/~jh243191/Resort_Database/home.html');
  await page.screenshot({ path: 'screenshot.png'});

  // TEST TWO: Verify all links contained on the home page are working as expected.
  // Note that any pages that interact with the MariaDB used to power
  // the backend of this project output an error: "ERROR COULD NOT CONNECT"
  // Testing should detect this, and output a list of pages
  // whose body contains the word "ERROR COULD NOT CONNECT"
  const urls = await page.$$eval('a', anchors => anchors.map(a => a.href));
  for (let url of urls) {
    try{
      await page.goto(url);
      await page.waitForSelector('body');
      const bodyContent = await page.$eval('body', b => b.innerHTML);
      if (bodyContent.includes("ERROR COULD NOT CONNECT")) {
        console.log("ERROR COULD NOT CONNECT (known MariaDB issue) at ", url);
      }
    } catch (error) {
      console.log(error);
      console.log('At', url);
    }
  }

  // TEST THREE: Similar to above, but this time check HTTP response codes.
  // If all pages return an HTTP response code of 200, output a message to tester.
  // Else, the page(s) not returning an HTTP response code of 200 will be output.
  var all_response_ok = new Boolean(true);
  for (let url of urls) {
    try{
      const response = await page.goto(url);
      const statusCode = response.status();
      if (statusCode != 200) {
        all_response_ok = false;
        console.log(url, statusCode);
      }
    } catch (error) {
      console.log(error);
      console.log('At',url);
    }
  }
  if (all_response_ok) {
    console.log("All HTTP responses were of type 200");
  }

  await browser.close();
}) ();

// Create a new browser object with headless set to false.
// Useful for watching the test program type input to the web page.
(async () => {
  const browser = await puppeteer.launch({
    headless: false,
    slowMo: 50,
    defaultViewport: {
      width: 1200,
      height: 820,
    },
  });


  // Since the two tests above are quite similar, TEST FOUR
  // will attempt to submit form data. Ideally, a site administrator
  // could then verify the test data was submitted, but in this case,
  // as mentioned above, the MariaDB that powers this functionality is
  // not working.
  const page = await browser.newPage();
  await page.goto('http://webdev.cs.umt.edu/~jh243191/Resort_Database/reservation.html');
  await page.waitForSelector('#arrive', {timeout: 60000});
  await page.type('#arrive', '2222-1-01 00:00:00');
  await page.type('#depart', '2222-12-31 00:00:00');
  await page.type('#fname', 'Thomas');
  await page.type('#lname', 'Anderson');
  await page.type('#dob', '1971-09-13'); //https://scifi.stackexchange.com/questions/80211/was-neo-actually-born-on-9-11
  await page.type('#phone', '4067210911');
  await page.type('#email', 'tanderson@pm.me');
  await page.type('#street', 'TEST ADDRESS');
  await page.type('#city', 'Capitol City');
  await page.type('#state', 'TEST');
  await page.type('#country', 'USA');
  await page.type('#postal', '00000');
  await page.type('#status', 'TEST');
  await page.type('#bank', 'Deutsch Bank');
  await page.type('#account', 'TEST');
  await page.type('#special', 'TEST');
  await page.type('#type', 'TEST');
  await page.type('#event', 'TEST');
  await page.type('#referral', 'Morpheus');
  await page.keyboard.press('Enter');

  await browser.close();
}) ();
