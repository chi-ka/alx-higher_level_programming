#!/usr/bin/node
// Script that gets the contents of a webpage and stores it in a file.

const request = require('request');
const fs = require('fs');

// Check that the URL and file path are supplied
if (process.argv.length !== 4) {
  console.log('Usage: node 0-statuscode.js <url> <file path>');
  process.exit(1);
}

const url = process.argv[2];
const filepath = process.argv[3];

// Make the GET request
request(url, (error, response, body) => {
  if (error) {
    console.log(`Error: ${error.message}`);
  } else {
    // Write the response body to the file
    fs.writeFile(filepath, body, 'utf-8', (err) => {
      if (err) {
        console.log(`Error writing to file: ${err.message}`);
      }
    });
  }
});
