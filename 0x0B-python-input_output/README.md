# 0x0B. Python - Input/Output

## Description
This project focuses on file handling, JSON serialization/deserialization, and working with structured data in Python. You'll learn how to read from and write to files, convert Python objects to JSON representations and vice versa, and manipulate complex data structures.

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
| File Length | The length of files will be tested using `wc` |
| Documentation | Modules, classes, and functions should be documented |
| Plagiarism | Any form of plagiarism is strictly forbidden and will result in removal from the program |

## Project Structure

| Task | Description | File |
|------|-------------|------|
| 0 | Write a function that reads a text file (UTF8) and prints it to stdout | 0-read_file.py |
| 1 | Write a function that writes a string to a text file (UTF8) and returns the number of characters written | 1-write_file.py |
| 2 | Write a function that appends a string at the end of a text file (UTF8) and returns the number of characters added | 2-append_write.py |
| 3 | Write a function that returns the JSON representation of an object (string) | 3-to_json_string.py |
| 4 | Write a function that returns an object (Python data structure) represented by a JSON string | 4-from_json_string.py |
| 5 | Write a function that writes an Object to a text file, using a JSON representation | 5-save_to_json_file.py |
| 6 | Write a function that creates an Object from a "JSON file" | 6-load_from_json_file.py |
| 7 | Write a script that adds all arguments to a Python list, and then save them to a file | 7-add_item.py |
| 8 | Write a function that returns the dictionary description with simple data structure for JSON serialization of an object | 8-class_to_json.py |
| 9 | Write a class Student that defines a student | 9-student.py |
| 10 | Write a class Student that defines a student (based on 9-student.py) | 10-student.py |
| 11 | Write a class Student that defines a student (based on 10-student.py) | 11-student.py |
| 12 | Create a function def pascal_triangle(n): that returns a list of lists of integers representing the Pascal's triangle of n | 12-pascal_triangle.py |
| 13 | Write a function that inserts a line of text to a file, after each line containing a specific string | 100-append_after.py |
| 14 | Write a script that reads stdin line by line and computes metrics | 101-stats.py |

### General
- Why Python programming is awesome
- How to open a file
- How to write text in a file
- How to read the full content of a file
- How to read a file line by line
- How to move the cursor in a file
- How to make sure a file is closed after using it
- What is and how to use the `with` statement
- What is JSON
- What is serialization
- What is deserialization
- How to convert a Python data structure to a JSON string
- How to convert a JSON string to a Python data structure


### Python Test Cases
- Allowed editors: vi, vim, emacs
- All your files should end with a new line
- All your test files should be inside a folder `tests`
- All your test files should be text files (extension: .txt)
- All your tests should be executed by using this command: `python3 -m doctest ./tests/*`
- All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
- A documentation is not a simple word, it's a real sentence explaining what's the purpose of the module, class or method (the length of it will be verified)
- We strongly encourage you to work together on test cases, so that you don't miss any edge case

## Mission Director
This project is supervised by the ALX Software Engineering Program.

## Developer
**Codename**: Achraf Sadaeq

## Acknowledgments
Holberton School, in collaboration with the ALX Software Engineering Program, developed this project for educational purposes.
