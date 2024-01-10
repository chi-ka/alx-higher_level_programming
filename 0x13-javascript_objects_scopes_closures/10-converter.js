#!/usr/bin/node

// Function to create a converter for a specific base
exports.converter = function (base) {
  return function (number) {
    return number.toString(base);
  };
};

// Test the function
const converter = require('./10-converter').converter;

let myConverter = converter(10);

console.log(myConverter(2));  // 2 in base 10
console.log(myConverter(12)); // 12 in base 10
console.log(myConverter(89)); // 89 in base 10

myConverter = converter(16);

console.log(myConverter(2));  // 2 in base 16 (hexadecimal) is "2"
console.log(myConverter(12)); // 12 in base 16 is "c"
console.log(myConverter(89)); // 89 in base 16 is "59"

