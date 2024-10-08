# 0x09. Python - Everything is Object

## Description

This project explores Python's object model, focusing on the fundamental principles of object identity, equality, and mutability. It covers the concept of objects and their relationships, emphasizing how Python handles data types and memory management.

## Requirements

| Category | Details |
|----------|---------|
| Editors | vi, vim, emacs |
| Interpreter | Ubuntu 20.04 LTS using python3 (version 3.8.5) |
| File Endings | All files should end with a new line |
| README | A README.md file at the root of the project folder is mandatory |
| Coding Style | pycodestyle (PEP8) |
| Global Variables | Not allowed |
| Functions per File | No more than 5 |
| Allowed Python Standard Library Functions | N/A (No external functions allowed) |

## Project Structure

| Task | Description | File |
|------|-------------|------|
| 0. Who am I? | What function would you use to get the type of an object? | 0-answer.txt |
| 1. Where are you? | How do you get the variable identifier (memory address in CPython)? | 1-answer.txt |
| 2. Right count | Do `a` and `b` point to the same object? `a = 89`, `b = 100` | 2-answer.txt |
| 3. Right count = | Do `a` and `b` point to the same object? `a = 89`, `b = 89` | 3-answer.txt |
| 4. Right count = | Do `a` and `b` point to the same object? `a = 89`, `b = a` | 4-answer.txt |
| 5. Right count =+ | Do `a` and `b` point to the same object? `a = 89`, `b = a + 1` | 5-answer.txt |
| 6. Is equal | What do these 3 lines print? `s1 = "Best School"`, `s2 = s1`, `print(s1 == s2)` | 6-answer.txt |
| 7. Is the same | What do these 3 lines print? `s1 = "Best"`, `s2 = s1`, `print(s1 is s2)` | 7-answer.txt |
| 8. Is really equal | What do these 3 lines print? `s1 = "Best School"`, `s2 = "Best School"`, `print(s1 == s2)` | 8-answer.txt |
| 9. Is really the same | What do these 3 lines print? `s1 = "Best School"`, `s2 = "Best School"`, `print(s1 is s2)` | 9-answer.txt |
| 10. And with a list, is it equal | What do these 3 lines print? `l1 = [1, 2, 3]`, `l2 = [1, 2, 3]`, `print(l1 == l2)` | 10-answer.txt |
| 11. And with a list, is it the same | What do these 3 lines print? `l1 = [1, 2, 3]`, `l2 = [1, 2, 3]`, `print(l1 is l2)` | 11-answer.txt |
| 12. And with a list, is it really equal | What do these 3 lines print? `l1 = [1, 2, 3]`, `l2 = l1`, `print(l1 == l2)` | 12-answer.txt |
| 13. And with a list, is it really the same | What do these 3 lines print? `l1 = [1, 2, 3]`, `l2 = l1`, `print(l1 is l2)` | 13-answer.txt |
| 14. List append | What does this script print? (List manipulation) | 14-answer.txt |
| 15. List add | What does this script print? (List manipulation) | 15-answer.txt |
| 16. Integer incrementation | What does this script print? (Integer manipulation) | 16-answer.txt |
| 17. List incrementation | What does this script print? (List manipulation) | 17-answer.txt |
| 18. List assignation | What does this script print? (List manipulation) | 18-answer.txt |
| 19. Copy a list object | Write a function that returns a copy of a list | 19-copy_list.py |
| 20. Tuple or not? | Is `a = ()` a tuple? | 20-answer.txt |
| 21. Tuple or not? | Is `a = (1, 2)` a tuple? | 21-answer.txt |
| 22. Tuple or not? | Is `a = (1)` a tuple? | 22-answer.txt |
| 23. Tuple or not? | Is `a = (1, )` a tuple? | 23-answer.txt |
| 24. Who I am? | What does this script print? `a = (1)`, `b = (1)`, `a is b` | 24-answer.txt |
| 25. Tuple or not | What does this script print? `a = (1, 2)`, `b = (1, 2)`, `a is b` | 25-answer.txt |
| 26. Empty is not empty | What does this script print? `a = ()`, `b = ()`, `a is b` | 26-answer.txt |
| 27. Still the same? | Will the last line of this script print 139926795932424? | 27-answer.txt |
| 28. Same or not? | Will the last line of this script print 139926795932424? | 28-answer.txt |
| 29. #pythonic | Write a function `magic_string()` that returns a string "BestSchool" n times | 100-magic_string.py |
| 30. Low memory cost | Write a class LockedClass that prevents dynamic creation of new instance attributes | 101-locked_class.py |
| 31. int 1/3 | How many int objects are created by the execution of the first line of the script? | 103-line1.txt, 103-line2.txt |
| 32. int 2/3 | Answer questions about int object creation and deletion | 104-line1.txt, 104-line2.txt, 104-line3.txt, 104-line4.txt, 104-line5.txt |
| 33. int 3/3 | How many int objects have been created and are still in memory? | 105-line1.txt |
| 34. Clear strings | Answer questions about string object creation and deletion | 106-line1.txt, 106-line2.txt, 106-line3.txt, 106-line4.txt, 106-line5.txt |

## Repository

- GitHub repository: [alx-higher_level_programming](https://github.com/Achrafsadeq/alx-higher_level_programming)
- Directory: 0x09-python-everything_is_object

 ## Learning Objectives

By the end of this project, you should be able to:

- Understand Python's object model and memory management.
- Distinguish between object identity and equality.
- Explore mutability and immutability of objects.
- Develop skills in writing and understanding simple Python functions.
- Examine and validate Python expressions involving objects and their types.

## Files

All `.py` files should include the appropriate logic for the tasks specified. Each answer file should contain only the expected result or the requested response.

## Usage

To view any specific answer, simply open the corresponding text file:

```bash
$ cat 0-answer.txt
```

## Mission Director

This project is supervised by the ALX Software Engineering Program.

## Developer

**Codename**: Achraf Sadeq

## Acknowledgments

Holberton School, in collaboration with the ALX Software Engineering Program, developed this project for educational purposes.
