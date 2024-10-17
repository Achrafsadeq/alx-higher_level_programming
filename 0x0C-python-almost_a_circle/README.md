# 0x0C. Python - Almost a circle

## Description
This project focuses on object-oriented programming in Python, covering topics such as inheritance, unittest, and file I/O. You'll work with classes representing rectangles and squares, implementing various methods and serialization/deserialization techniques.

## Requirements

| Category | Details |
|----------|---------|
| Editors | vi, vim, emacs |
| Interpreter | Ubuntu 20.04 LTS using python3 (version 3.8.5) |
| File Endings | All files should end with a new line |
| Shebang | The first line of all files should be exactly `#!/usr/bin/python3` |
| README | A README.md file at the root of the project folder is mandatory |
| Coding Style | pycodestyle (version 2.8.*) |
| Executable Files | All files must be executable |
| File Length | The length of files will be tested using wc |
| Documentation | Modules, classes, and functions should be documented |
| Plagiarism | Any form of plagiarism is strictly forbidden and will result in removal from the program |

## Python Unit Tests
- Allowed editors: vi, vim, emacs
- All your files should end with a new line
- All your test files should be inside a folder `tests`
- You have to use the `unittest` module
- All your test files should be python files (extension: .py)
- All your test files and folders should start with `test_`
- Your file organization in the tests folder should be the same as your project: ex: for `models/base.py`, unit tests must be in: `tests/test_models/test_base.py`
- All your tests should be executed by using this command: `python3 -m unittest discover tests`
- You can also test file by file by using this command: `python3 -m unittest tests/test_models/test_base.py`
- We strongly encourage you to work together on test cases so that you don't miss any edge case

## Tasks
 
| Task | Description | File |
|------|-------------|------|
| 0 | Unit testing and PEP 8 validation | tests/ |
| 1 | First class Base | models/base.py, models/__init__.py |
| 2 | First Rectangle | models/rectangle.py |
| 3 | Validate attributes | models/rectangle.py |
| 4 | Area first | models/rectangle.py |
| 5 | Display #0 | models/rectangle.py |
| 6 | __str__ | models/rectangle.py |
| 7 | Display #1 | models/rectangle.py |
| 8 | Update #0 | models/rectangle.py |
| 9 | Update #1 | models/rectangle.py |
| 10 | And now, the Square! | models/square.py |
| 11 | Square size | models/square.py |
| 12 | Square update | models/square.py |
| 13 | Rectangle instance to dictionary representation | models/rectangle.py |
| 14 | Square instance to dictionary representation | models/square.py |
| 15 | Dictionary to JSON string | models/base.py |
| 16 | JSON string to file | models/base.py |
| 17 | JSON string to dictionary | models/base.py |
| 18 | Dictionary to Instance | models/base.py |
| 19 | File to instances | models/base.py |
| 20 | JSON ok, but CSV? | models/ |
| 21 | Let's draw it | models/base.py |

## Resources
- [args/kwargs](https://yasoob.me/2013/08/04/args-and-kwargs-in-python-explained/)
- [JSON encoder and decoder](https://docs.python.org/3/library/json.html)
- [unittest module](https://docs.python.org/3/library/unittest.html)
- [Python test cheatsheet](https://www.pythonsheets.com/notes/python-tests.html)


## Mission Director
This project is supervised by the ALX Software Engineering Program.

## Developer
**Codename**: Achraf Sadaeq

## Acknowledgments
Holberton School, in collaboration with the ALX Software Engineering Program, developed this project for educational purposes.

