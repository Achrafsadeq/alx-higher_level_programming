#!/usr/bin/node
// Script to compute and print the factorial of a number

// Recursive function to compute factorial
function factorial(n) {
  if (isNaN(n) || n <= 0) {
    return 1; // Base case: factorial of NaN or numbers <= 0 is 1
  }
  return n * factorial(n - 1); // Recursive case
}

// Get the first command-line argument and cast it to an integer
const num = parseInt(process.argv[2]);

// Compute and print the factorial
console.log(factorial(num));
