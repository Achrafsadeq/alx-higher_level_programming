# 0x13. JavaScript - Objects, Scopes, and Closures

## Description

This project introduces advanced concepts in JavaScript programming, including working with objects, closures, and managing scopes. It builds on the foundational knowledge from previous JavaScript projects and explores new functionalities.

## Learning Objectives

At the end of this project, you should be able to explain:

- How to create objects in JavaScript and work with their properties and methods
- The significance of closures and how they work
- The distinction between the different scopes in JavaScript
- How inheritance works using `class` and `extends`
- Manipulating and iterating through objects and arrays
- How to export and import modules in JavaScript

## Requirements

- **OS**: Ubuntu 20.04 LTS
- **Node.js**: v14.x
- **Code Style**: Semi-standard (v16.x.x)
- **Interpreter**: `#!/usr/bin/node`
- All files should end with a new line and be executable.

## Project Tasks

| **Task**                     | **Description**                                                                                       | **File**                |
|------------------------------|-------------------------------------------------------------------------------------------------------|-------------------------|
| **0. Rectangle #0**          | Write an empty class `Rectangle` that defines a rectangle.                                           | `0-rectangle.js`        |
| **1. Rectangle #1**          | Add a constructor to the `Rectangle` class to initialize width and height.                          | `1-rectangle.js`        |
| **2. Rectangle #2**          | Create an empty object if width or height is invalid.                                               | `2-rectangle.js`        |
| **3. Rectangle #3**          | Add a `print` method to the `Rectangle` class to print the rectangle using the `X` character.       | `3-rectangle.js`        |
| **4. Rectangle #4**          | Add `rotate` and `double` methods to the `Rectangle` class.                                         | `4-rectangle.js`        |
| **5. Square #0**             | Create a class `Square` that inherits from `Rectangle`.                                             | `5-square.js`           |
| **6. Square #1**             | Add a `charPrint` method to the `Square` class to print the square with a custom character.         | `6-square.js`           |
| **7. Occurrences**           | Write a function to count the number of occurrences of an element in a list.                        | `7-occurrences.js`      |
| **8. Esrever**               | Write a function that reverses a list without using `reverse`.                                      | `8-esrever.js`          |
| **9. Log me**                | Write a function that logs the number of arguments already printed.                                 | `9-logme.js`            |
| **10. Number conversion**    | Write a function that converts a number from base 10 to another base.                               | `10-converter.js`       |
| **11. Factor index**         | Modify the order of an array based on the index of elements.                                        | `100-map.js`            |
| **12. Sorted occurrences**   | Sort and reduce an array by adding unique values.                                                   | `101-sorted.js`         |
| **13. Concat files**         | Concatenate the contents of two files into a new file.                                              | `102-concat.js`         |

## Setup Instructions

### Install Node.js 14
```bash
curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
sudo apt-get install -y nodejs
```

### Install Semi-Standard
```bash
sudo npm install semistandard --global
```

## Mission Director
This project is supervised by the ALX Software Engineering Program.

## Developer
**Codename**: Achraf Sadaeq

## Acknowledgments
Holberton School, in collaboration with the ALX Software Engineering Program, developed this project for educational purposes.
