#!/usr/bin/node
exports.nbOccurences = function(list, searchElement) {
    // Initialize a counter for occurrences
    let count = 0;

    // Iterate over the list
    for (let i = 0; i < list.length; i++) {
        // Check if the current element is equal to the search element
        if (list[i] === searchElement) {
            // If equal, increment the counter
            count++;
        }
    }

    // Return the count of occurrences
    return count;
};
