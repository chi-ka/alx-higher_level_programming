#!/usr/bin/node
// Script that prints all characters of a Star Wars movie

const request = require('request');

// Check that the API URL is supplied
if (process.argv.length !== 3) {
  console.log('Usage: node 6-completed_tasks.js <id>');
  process.exit(1);
}
const id = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${id}`;

// Make the GET request
request(apiUrl, (error, response, body) => {
  if (error) {
    console.log(`Error: ${error.message}`);
  } else {
    const films = JSON.parse(body);
    const characters = films.characters;
    characters.forEach(character => {
      request(character, (error, response, body) => {
        if (error) {
          console.log(`Error: ${error.message}`);
        } else {
          const output = JSON.parse(body);
          console.log(`${output.name}`);
        }
      });
    });
  }
});
