#!/usr/bin/node

const args = process.argv.slice(2);

function findSecondBiggest(numbers) {
  let max = -Infinity, secondMax = -Infinity;

  for (let i = 0; i < numbers.length; i++) {
    const num = parseInt(numbers[i], 10);

    if (num > max) {
      secondMax = max;
      max = num;
    } else if (num > secondMax && num < max) {
      secondMax = num;
    }
  }

  return secondMax;
}

if (args.length < 2) {
  console.log(0);
} else {
  console.log(findSecondBiggest(args));
}

