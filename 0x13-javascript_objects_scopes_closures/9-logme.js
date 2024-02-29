#!/usr/bin/node
let count = 0; // Initialize a counter for the number of arguments already printed

exports.logMe = function(item) {
    // Print the number of arguments already printed and the current argument value
    console.log(`${count}: ${item}`);

    // Increment the counter for the number of arguments printed
    count++;
};
