#!/usr/bin/node

function factorial (n) {
  // Handle NaN case
  if (isNaN(n)) {
    return 1;
  }

  // Base cases
  if (n === 0 || n === 1) {
    return 1;
  }

  // Recursive case
  return n * factorial(n - 1);
}

// Get the first argument, convert to number
const num = Number(process.argv[2]);

// Print the factorial
console.log(factorial(num));
