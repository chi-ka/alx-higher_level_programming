#!/usr/bin/node

const request = require('request');

// Check if the correct number of arguments are provided
if (process.argv.length !== 3) {
  console.log('Usage: node script.js <movie_id>');
  process.exit(1);
}

const movieId = process.argv[2];
const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

// Make the GET request to fetch movie details
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(`Error: ${error}`);
    process.exit(1);
  }

  if (response.statusCode !== 200) {
    console.error(`Error: Failed to fetch movie details. Status code: ${response.statusCode}`);
    process.exit(1);
  }

  const movie = JSON.parse(body);
  const charactersUrls = movie.characters;

  // Function to fetch character details
  // Function to fetch character details
  const fetchCharacterDetails = (characterUrl) => {
    return new Promise((resolve, reject) => {
      request(characterUrl, (error, response, body) => {
        if (error) {
          reject(new Error(error)); // Use Error object here
        }

        if (response.statusCode !== 200) {
          reject(new Error(`Failed to fetch character details. Status code: ${response.statusCode}`)); // Use Error object here
        }

        const character = JSON.parse(body);
        resolve(character.name);
      });
    });
  };

  // Fetch and print character names
  Promise.all(charactersUrls.map(url => fetchCharacterDetails(url)))
    .then(characterNames => {
      characterNames.forEach(name => console.log(name));
    })
    .catch(error => {
      console.error(`Error: ${error}`);
      process.exit(1);
    });
});
