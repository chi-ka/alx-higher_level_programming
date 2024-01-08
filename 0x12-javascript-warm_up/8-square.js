#!/usr/bin/node

const size = process.argv[2];
const num = parseInt(size);

if (isNaN(num)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < num; i++) {
    console.log('X'.repeat(num));
  }
}

