#!/usr/bin/node
const { dict } = require('./101-data');
const newDict = {};

for (const userId in dict) {
  const occurrences = dict[userId];

  if (!(occurrences in newDict)) {
    newDict[occurrences] = [];
  }

  newDict[occurrences].push(userId);
}

console.log(newDict);
