#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.error('error:', error);
  } else {
    const results = JSON.parse(body);
    const completed = {};
    for (const task of results) {
      if (task.completed) {
        if (completed[task.userId]) {
          completed[task.userId]++;
        } else {
          completed[task.userId] = 1;
        }
      }
    }
    console.log(completed);
  }
});
