#!/usr/bin/node
// Script that writes a string to a file.
const fs = require('fs');

// Check that the file path and string are supplied
if (process.argv.length !== 4) {
  console.log('Usage: node 0-write.js <file path> <string>');
  process.exit(1);
}

const filePath = process.argv[2];
const attachString = process.argv[3];

// Write the string to the file using utf-8 encoding
fs.writeFile(filePath, attachString, 'utf-8', (err) => {
  if (err) {
    console.log(err);
  }
});
