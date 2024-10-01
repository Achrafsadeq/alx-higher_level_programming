# 0x06. Python - Classes and Objects

## Description

This project focuses on Object-Oriented Programming (OOP) in Python. The tasks aim to introduce and reinforce key OOP concepts like classes, instances, attributes, methods, and encapsulation. By the end of the project, you'll have experience with defining and working with classes and objects in Python, including handling their attributes and methods.

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

## Python Coding Guidelines

* All Python scripts must be executable.
* All scripts should begin with `#!/usr/bin/python3` as the first line.
* Python code must comply with `pycodestyle` version 2.8.*
* Documentation is mandatory for each module, class, and method using Google-style Python docstrings.

## Tasks

| Task | Description | File |
|------|-------------|------|
| 0 | Write an empty class `Square` that defines a square. | `0-square.py` |
| 1 | Define `Square` with a private instance attribute `size`, and no type or value verification. | `1-square.py` |
| 2 | Add type and value verification for `size`. If size is not an integer, raise a `TypeError`, and if it's negative, raise a `ValueError`. | `2-square.py` |
| 3 | Add a public instance method `area` that returns the area of the square. | `3-square.py` |
| 4 | Add getter and setter methods for `size`. Ensure the setter validates the input. | `4-square.py` |
| 5 | Write a method `my_print` that prints the square using the character `#`. If size is 0, print an empty line. | `5-square.py` |
| 6 | Write a method that compares two `Square` instances. The comparison is based on their area. Add a magic method `__eq__` to compare. | `6-square.py` |

## Advanced Tasks

| Task | Description | File |
|------|-------------|------|
| 100 | Write a method to return the square's string representation as a string that visually resembles the square. Override `__str__`. | `100-square.py` |
| 101 | Write a method that deletes the square and prints a message: `Bye square...`. Override `__del__`. | `101-square.py` |
| 102 | Write a method that sets the position of the square on the terminal output. The position is defined as a tuple of two integers, and must be positive. | `102-square.py` |
| 103 | Write a class method `is_instance` that checks if an object is an instance of `Square`. If the object is a square, it returns `True`; otherwise, `False`. | `103-square.py` |

## Learning Objectives

By the end of this project, you will be able to:

* Understand key OOP concepts: classes, objects, attributes, methods.
* Implement data abstraction, encapsulation, and information hiding.
* Understand the `__init__` method and create constructors.
* Create properties for controlled access to private attributes.
* Overload comparison operators and magic methods like `__eq__` and `__str__`.
* Manage object memory and deletion with `__del__`.
* Validate input within Python class methods.
* Gracefully handle invalid inputs and exceptions.

  ## Mission Director
This project is supervised by the ALX Software Engineering Program.

## Developer
**Codename**: Achraf Sadeq

## Acknowledgments
 Holberton School, in collaboration with the ALX Software Engineering Program, developed this project for educational purposes.
