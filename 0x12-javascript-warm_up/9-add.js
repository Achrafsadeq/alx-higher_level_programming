#!/usr/bin/node
// Script to add two integers passed as command-line arguments

// Extract and convert arguments to numbers
const [a, b] = process.argv.slice(2).map(Number);

// Check if both arguments are valid numbers
if (isNaN(a) || isNaN(b)) {
  console.log('NaN'); // Print 'NaN' if any argument is not a number
} else {
  console.log(a + b); // Print the sum of the two numbers
}
