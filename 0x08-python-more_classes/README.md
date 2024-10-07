# 0x08. Python - More Classes and Objects

## Description

This project delves deeper into Object-Oriented Programming (OOP) in Python, building on the basics of classes and objects. The tasks are designed to explore advanced OOP concepts such as class methods, static methods, and special methods (magic methods). By the end of this project, you will have a solid understanding of how to create and manipulate complex objects in Python.

## Requirements

| Category | Details |
|----------|---------|
| Editors | `vi`, `vim`, `emacs` |
| Interpreter | Ubuntu 20.04 LTS using python3 (version 3.8.5) |
| File Endings | All files should end with a new line |
| README | A `README.md` file at the root of the project folder is mandatory |
| Coding Style | `pycodestyle` (PEP8) |
| Global Variables | Not allowed |
| Functions per File | No more than 5 |
| Allowed Python Standard Library Functions | N/A (No external functions allowed) |
| Header File | N/A (pure Python project) |

## Learning Objectives

By completing this project, you will be able to:

* Understand and implement class and instance attributes
* Use properties for controlled access to attributes
* Create and use class methods and static methods
* Implement special methods like `__str__`, `__repr__`, and `__del__`
* Work with class attributes and methods
* Understand and implement inheritance in Python classes

## Tasks

| Task | Description | File |
|------|-------------|------|
| 0 | Write an empty class `Rectangle` that defines a rectangle. | 0-rectangle.py |
| 1 | Add private instance attributes `width` and `height` to the `Rectangle` class, with property getters and setters. | 1-rectangle.py |
| 2 | Add public instance methods `area()` and `perimeter()` to the `Rectangle` class. | 2-rectangle.py |
| 3 | Implement `__str__` method to print the rectangle with `#` characters. | 3-rectangle.py |
| 4 | Implement `__repr__` method to return a string representation of the rectangle. | 4-rectangle.py |
| 5 | Implement `__del__` method to print a message when an instance is deleted. | 5-rectangle.py |
| 6 | Add a public class attribute `number_of_instances` to keep track of the number of `Rectangle` instances. | 6-rectangle.py |
| 7 | Add a public class attribute `print_symbol` to customize the string representation. | 7-rectangle.py |
| 8 | Implement a static method `bigger_or_equal(rect_1, rect_2)` to compare rectangles based on area. | 8-rectangle.py |
| 9 | Implement a class method `square(cls, size=0)` to create a square `Rectangle` instance. | 9-rectangle.py |

## Advanced Task

| Task | Description | File |
|------|-------------|------|
| 10 | N Queens - Write a program that solves the N queens problem. | 101-nqueens.py |

## Requirements

* All files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
* All files should end with a new line
* The first line of all files should be exactly `#!/usr/bin/python3`
* Code should use the pycodestyle (version 2.8.*)
* All files must be executable
* The length of your files will be tested using `wc`

## Mission Director
This project is supervised by the ALX Software Engineering Program.

## Developer
**Codename**: Achraf Sadeq

## Acknowledgments
 Holberton School, in collaboration with the ALX Software Engineering Program, developed this project for educational purposes.
