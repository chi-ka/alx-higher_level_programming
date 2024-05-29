#!/usr/bin/node
// Script that displays the status code of a GET request.

const request = require('request');

// Check that the URL is supplied
if (process.argv.length !== 3) {
    console.log("Usage: node 0-statuscode.js <Url>");
    process.exit(1);
}

const url = process.argv[2];

// Make the GET request and display the status code
request(url, (error, response, body) => {
    if (error) {
        console.log(`Error: ${error.message}`);
    } else {
        console.log(`code: ${response.statusCode}`);
    }
});
