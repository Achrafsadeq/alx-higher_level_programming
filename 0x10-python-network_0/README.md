# 0x10. Python - Network #0

## Background Context

This project focuses on learning and applying Python scripting for network-related tasks, primarily using `curl` to interact with web servers. By completing this project, you will gain hands-on experience with HTTP requests, handling responses, and automating tasks using Bash and Python scripts.

## Requirements

| Category         | Details |
|------------------|---------|
| **Project Type** | Mandatory |
| **Review**       | Manually reviewed by peers or TAs |
| **Ubuntu Version** | Ubuntu 20.04 LTS |
| **Python Version** | Python 3.8.5 |
| **Bash Scripts** | All Bash scripts must be exactly 3 lines long, executable, and end with a new line |
| **Python Scripts** | All Python scripts must start with `#!/usr/bin/python3` and follow PEP 8 style guidelines |
| **README**       | A README.md file at the root of the project folder is mandatory |

## General Requirements

1. **Bash Scripts**: 
   - All Bash scripts must be exactly 3 lines long (`wc -l file` should print 3).
   - The first line of all Bash scripts should be `#!/bin/bash`.
   - The second line should be a comment explaining what the script does.
   - All `curl` commands must use the `-s` (silent mode) option.
   - All files must be executable.

2. **Python Scripts**:
   - The first line of all Python files should be `#!/usr/bin/python3`.
   - Code should follow `pycodestyle` (version 2.8.*).
   - All modules, classes, and functions must be documented with meaningful sentences.

3. **Ubuntu 20.04 LTS**: All files will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3.8.5.

## Tasks

| Task                          | Description                                  | Files                         |
|-------------------------------|----------------------------------------------|-------------------------------|
| **0. cURL body size**         | Write a Bash script that takes in a URL, sends a request, and displays the size of the response body in bytes | 0-body_size.sh |
| **1. cURL to the end**        | Write a Bash script that takes in a URL, sends a GET request, and displays the body of the response (only for 200 status code) | 1-body.sh |
| **2. cURL Method**            | Write a Bash script that sends a DELETE request to a URL and displays the body of the response | 2-delete.sh |
| **3. cURL only methods**      | Write a Bash script that takes in a URL and displays all HTTP methods the server will accept | 3-methods.sh |
| **4. cURL headers**           | Write a Bash script that takes in a URL, sends a GET request with a custom header, and displays the body of the response | 4-header.sh |
| **5. cURL POST parameters**   | Write a Bash script that takes in a URL, sends a POST request with specific parameters, and displays the body of the response | 5-post_params.sh |
| **6. Find a peak**            | Write a Python function that finds a peak in a list of unsorted integers | 6-peak.py, 6-peak.txt |
| **7. Only status code**       | Write a Bash script that sends a request to a URL and displays only the status code of the response | 100-status_code.sh |
| **8. cURL a JSON file**       | Write a Bash script that sends a JSON POST request to a URL and displays the body of the response | 101-post_json.sh |
| **9. Catch me if you can!**   | Write a Bash script that makes a request to a specific URL and causes the server to respond with "You got me!" | 102-catch_me.sh |

## Learning Objectives

By completing this project, you will:

- Understand how to use `curl` to interact with web servers.
- Learn how to write Bash scripts to automate HTTP requests.
- Gain experience with Python scripting for network-related tasks.
- Understand how to handle HTTP responses and extract useful information.
- Learn how to document Python modules, classes, and functions effectively.

## Submission

- **GitHub Repository**: [alx-higher_level_programming](https://github.com/Achrafsadeq/alx-higher_level_programming)
- **Directory**: 0x10-python-network_0

---

### Mission Director

This project is part of the ALX Software Engineering Program.

### Developer

**Codename**: Achraf Sadeq

### Acknowledgments

This project was developed by Holberton School, in collaboration with the ALX Software Engineering Program, to provide practical, hands-on learning experiences in a professional and real-world context. It aims to equip learners with the skills and knowledge necessary to tackle complex challenges in software engineering.
