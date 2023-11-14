#!/usr/bin/node

// Convert all arguments to integers
const nums = process.argv.slice(2).map(Number);

// Check the number of arguments
const numArgs = nums.length;

// Check if no arguments or only one argument is passed
if (numArgs === 0 || numArgs === 1) {
	console.log(0);
} else {
	// Sort the array in descending order
	nums.sort((a, b) => b - a);

	// Find and print the second biggest integer
	console.log(nums[1]);
}
