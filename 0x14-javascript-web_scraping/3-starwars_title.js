#!/usr/bin/node
// Script that prints the title of a Star Wars movie where the episode number matches a given integer.

const request = require('request');

// Check that the episode ID is supplied
if (process.argv.length !== 3) {
  console.log('Usage: node 0-statuscode.js <episode number>');
  process.exit(1);
}

const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

// Make the GET request and display the movie title
request(url, (error, response, body) => {
  if (error) {
    console.log(`Error: ${error.message}`);
  } else {
    try {
      const output = JSON.parse(body);
      const title = output.title;
      console.log(title);
    } catch (parseError) {
      console.log(`Error parsing JSON: ${parseError.message}`);
    }
  }
});
