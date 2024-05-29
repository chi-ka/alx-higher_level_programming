#!/usr/bin/node
// Script that computes the number of tasks completed by user id.

const request = require('request');

// Check that the API URL is supplied
if (process.argv.length !== 3) {
  console.log('Usage: node 6-completed_tasks.js <API_URL>');
  process.exit(1);
}

const apiUrl = process.argv[2];

// Make the GET request
request(apiUrl, (error, response, body) => {
  if (error) {
    console.log(`Error: ${error.message}`);
  } else {
    try {
      const tasks = JSON.parse(body);
      const completedTasksByUser = {};

      tasks.forEach(task => {
        if (task.completed) {
          if (!completedTasksByUser[task.userId]) {
            completedTasksByUser[task.userId] = 0;
          }
          completedTasksByUser[task.userId]++;
        }
      });

      console.log(completedTasksByUser);
    } catch (parseError) {
      console.log(`Error parsing JSON: ${parseError.message}`);
    }
  }
});
