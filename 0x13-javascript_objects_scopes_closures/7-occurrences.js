#!/usr/bin/node

// 7-occurrences.js
exports.nbOccurences = function (list, searchElement) {
    return list.reduce((count, current) => (current === searchElement ? count + 1 : count), 0);
};

// 7-main.js
const nbOccurences = require('./7-occurrences').nbOccurences;

console.log(nbOccurences([1, 2, 3, 4, 5, 6], 3));
console.log(nbOccurences([3, 2, 3, 4, 5, 3, 3], 3));
console.log(nbOccurences(["S", 12, "c", "S", "School", 8], "S"));

