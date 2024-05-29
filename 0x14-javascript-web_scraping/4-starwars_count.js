#!/usr/bin/node
// Script that prints the number of movies where the character "Wedge Antilles" is present.

const request = require('request');

// Check that the URL is supplied
if (process.argv.length !== 3) {
  console.log('Usage: node 0-statuscode.js <url>');
  process.exit(1);
}

const url = process.argv[2];

// Make the GET request and count the movies with "Wedge Antilles"
request(url, (error, response, body) => {
  if (error) {
    console.log(`Error: ${error.message}`);
  } else {
    try {
      const films = JSON.parse(body).results;
      let count = 0;

      films.forEach(film => {
        if (film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')) {
          count++;
        }
      });

      console.log(count);
    } catch (parseError) {
      console.log(`Error parsing JSON: ${parseError.message}`);
    }
  }
});
