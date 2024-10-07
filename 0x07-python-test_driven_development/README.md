# 0x07. Python - Test-Driven Development

## Description

This project covers the principles of **Test-Driven Development (TDD)** in Python. The goal is to write unit tests before implementing the actual functions. It involves creating test cases using the `unittest` module and ensuring that each function works as expected under various conditions, including edge cases.


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

## Project Structure

| Task | Description | File |
|------|-------------|------|
| 0 | Write a function `add_integer(a, b=98)` that adds two integers. | `0-add_integer.py` |
| 1 | Write a function `matrix_divided(matrix, div)` that divides all elements of a matrix by `div`. | `2-matrix_divided.py` |
| 2 | Write a function `say_my_name(first_name, last_name="")` that prints `My name is <first name> <last name>`. | `3-say_my_name.py` |
| 3 | Write a function `print_square(size)` that prints a square with the character `#`. | `4-print_square.py` |
| 4 | Write a function `text_indentation(text)` that prints a text with 2 new lines after each of the characters: `.`, `?`, and `:`. | `5-text_indentation.py` |
| 5 | Write unit tests for the function `max_integer(list=[])`. | `tests/6-max_integer_test.py` |

### Advanced Tasks

| Task | Description | File |
|------|-------------|------|
| 100 | Write a function `matrix_mul(m_a, m_b)` that multiplies two matrices. | `100-matrix_mul.py` |
| 101 | Write a function `lazy_matrix_mul(m_a, m_b)` that multiplies two matrices using NumPy. | `101-lazy_matrix_mul.py` |
| 102 | Write a function `print_python_string(p)` that prints information about a Python string object. | `102-python.c` |

## Learning Objectives

By the end of this project, you should be able to:

- Understand the principles and benefits of Test-Driven Development.
- Write unit tests for different Python functions and classes.
- Develop robust code by identifying edge cases and handling exceptions.
- Implement docstrings and follow best practices for Python documentation.
- Create and validate test cases using the `unittest` module and `doctest`.
- Use matrix multiplication with error handling and type checking.

## Files

All `.py` files should include a corresponding test file in the `tests` folder, using the following naming convention:

- For `0-add_integer.py`, the test file should be named `tests/0-add_integer_test.py`.
- For `2-matrix_divided.py`, the test file should be named `tests/2-matrix_divided_test.py`, etc.

Each test file should contain various test cases to validate the logic, including edge cases, invalid inputs, and expected outputs.

## Usage

To run the test cases for a specific function:

```bash
$ python3 -m unittest tests/0-add_integer_test.py
```
## Mission Director

This project is supervised by the ALX Software Engineering Program.

## Developer

**Codename**: Achraf Sadeq

## Acknowledgments

 Holberton School, in collaboration with the ALX Software Engineering Program, developed this project for educational purposes.
