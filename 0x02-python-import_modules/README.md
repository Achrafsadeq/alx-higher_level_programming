## 0x02. Python - Import & Modules

### Description

This project focuses on the usage of Python modules, covering essential topics such as importing functions, creating reusable code, handling command-line arguments, and preventing unwanted code execution upon import. By the end of this project, you'll understand Python’s import mechanisms and how to properly structure programs for modularity and clarity. The project also emphasizes adhering to PEP8 guidelines for code quality.

### Requirements

| Category          | Details                                                              |
|-------------------|----------------------------------------------------------------------|
| **Editors**        | vi, vim, emacs                                                       |
| **Interpreter**    | Ubuntu 20.04 LTS, Python 3 (version 3.8.5)                           |
| **File Endings**   | All files should end with a new line                                 |
| **README**         | A `README.md` file at the root of the project folder is mandatory    |
| **Coding Style**   | Follow PEP8 (pycodestyle)                                            |
| **Global Variables**| Not allowed                                                         |
| **Functions per File**| No more than 5                                                    |
| **Allowed Functions**| `print`, `input`, `int`, `len`, `dir`, `sys`                       |
| **Header File**    | N/A (pure Python project)                                            |

#### Python Coding Guidelines
- All Python scripts must be executable.
- Scripts should begin with `#!/usr/bin/python3` as the first line.
- Python code must comply with `pycodestyle` version 2.8.\*.
- Scripts should handle command-line arguments using the `sys.argv` list.
- Code must not be executed when imported (use `if __name__ == "__main__":`).

### Tasks

| Task # | Description                                                               | File                   |
|--------|---------------------------------------------------------------------------|------------------------|
| **0**  | Import a simple function from a simple file                                | [0-add.py](./0-add.py)  |
| **1**  | Perform basic arithmetic operations using functions from another module    | [1-calculation.py](./1-calculation.py) |
| **2**  | Print the number and list of arguments passed to a script                  | [2-args.py](./2-args.py)|
| **3**  | Add all command line arguments together                                    | [3-infinite_add.py](./3-infinite_add.py) |
| **4**  | Access and print names defined by a module using `dir()`                   | [4-hidden_discovery.py](./4-hidden_discovery.py) |
| **5**  | Import a variable from another file and print its value                    | [5-variable_load.py](./5-variable_load.py) |
| **6**  | Build a program that handles basic arithmetic operations via command line  | [100-my_calculator.py](./100-my_calculator.py) |
| **7**  | Write a Python script that prints all names defined by a compiled module   | [101-easy_print.py](./101-easy_print.py) |
| **8**  | Print the bytecode of a specific Python function                           | [102-magic_calculation.py](./102-magic_calculation.py) |
| **9**  | Write a script that imports all functions from a file and handles operations| [103-fast_alphabet.py](./103-fast_alphabet.py) |

### Learning Objectives

By the end of this project, you will be able to:

- Import functions and variables from other files
- Use the Python `sys` module to handle command-line arguments
- Implement Python modules for better code reuse
- Work with Python's built-in `dir()` function
- Prevent code execution upon module import using the `if __name__ == "__main__":` construct

### Mission Director

This project is supervised by the ALX Software Engineering Program.

### Developer

**Codename:** Achraf Sadeq

### Acknowledgments

This project is part of the ALX Software Engineering Program curriculum and is built for educational purposes.

