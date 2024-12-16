#!/usr/bin/node

// Convert arguments to integers
const args = process.argv.slice(2).map(Number);

// Handle cases with 0 or 1 arguments
if (args.length <= 1) {
    console.log(0);
} else {
    // Remove duplicates and sort in descending order
    const uniqueSorted = [...new Set(args)].sort((a, b) => b - a);
    
    // Print the second element (second biggest)
    console.log(uniqueSorted.length > 1 ? uniqueSorted[1] : 0);
}
