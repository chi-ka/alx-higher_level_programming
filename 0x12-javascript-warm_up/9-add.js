#!/usr/bin/node

const arg1 = process.argv[2];
const arg2 = process.argv[3];

function addition(a, b) {
  return a + b;
}

const num1 = parseInt(arg1);
const num2 = parseInt(arg2);

const result = addition(num1, num2);
console.log(result);

