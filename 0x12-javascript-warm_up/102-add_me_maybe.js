#!/usr/bin/node
// Define the function
function addMeMaybe(number, theFunction) {
    // Increment the number
    number++;

    // Call the function with the incremented number as an argument
    theFunction(number);
}

// Export the function
module.exports.addMeMaybe = addMeMaybe;
