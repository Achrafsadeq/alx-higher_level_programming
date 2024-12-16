#!/usr/bin/node
// Script to compute and print the factorial of a number iteratively

// Parse the first command-line argument as an integer
const num = parseInt(process.argv[2]);

// Function to compute factorial
function factorial(n) {
  if (isNaN(n) || n <= 1) {
    return 1; // Return 1 if n is NaN or less than or equal to 1
  }
  
  let result = 1; // Initialize result as 1
  
  // Loop from 2 to n to compute the factorial
  for (let i = 2; i <= n; i++) {
    result *= i; // Multiply result by the current number
  }
  
  return result; // Return the computed factorial
}

// Print the factorial of the parsed number
console.log(factorial(num));
