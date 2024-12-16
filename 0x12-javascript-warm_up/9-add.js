#!/usr/bin/node

// Function to add two numbers
function add(a, b) {
  return a + b;
}

// Get the arguments and convert them to integers
const args = process.argv;
const a = parseInt(args[2], 10);
const b = parseInt(args[3], 10);

// Print the result of the addition
console.log(isNaN(a) || isNaN(b) ? 'NaN' : add(a, b));
