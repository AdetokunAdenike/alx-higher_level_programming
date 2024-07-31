#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  const tasks = JSON.parse(body);
  const userTaskCount = {};

  tasks.forEach(task => {
    if (task.completed) {
      if (userTaskCount[task.userId]) {
        userTaskCount[task.userId]++;
      } else {
        userTaskCount[task.userId] = 1;
      }
    }
  });

  console.log(userTaskCount);
});
