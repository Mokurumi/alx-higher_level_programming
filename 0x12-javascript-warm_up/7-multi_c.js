#!/usr/bin/node

const nums = parseInt(process.argv[2]);

if (!isNaN(nums)) {
  // Loop through and print 'C is fun' x times
  for (let i = 0; i < nums; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
