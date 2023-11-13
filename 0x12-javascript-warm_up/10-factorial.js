#!/usr/bin/node

const factorial = (n) => {
	// Base case: factorial of 0 or NaN is 1
	if (isNaN(n) || n === 0) {
		return 1;
	}
	
	// Recursive case: n! = n * (n-1)!
	return n * factorial(n - 1);
};

// Convert the first argument to an integer
const number = parseInt(process.argv[2]);

// Call the factorial function and print the result
console.log(factorial(number));
