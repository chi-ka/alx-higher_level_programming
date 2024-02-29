#!/usr/bin/node
exports.esrever = function(list) {
    let newlist = [];

    // Iterate over the list in reverse order
    for (let i = list.length - 1; i >= 0; i--) {
        // Add elements to the new list
        newlist.push(list[i]);
    }

    return newlist;
};
