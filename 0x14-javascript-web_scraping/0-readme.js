#!/usr/bin/node
// script that reads and prints the content of a file
const fs = require('fs');

// Check if a file path is provided as an argument
if (process.argv.length < 3) {
  console.log('Usage: node 0-readme.js <file path>');
  process.exit(1);
}

const filePath = process.argv[2];

// Read the file using utf-8 encoding
fs.readFile(filePath, 'utf-8', (err, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
