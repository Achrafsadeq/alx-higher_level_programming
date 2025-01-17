# 0x11. Python - Network #1

## Background Context

This project builds on the foundational knowledge of Python scripting for network-related tasks. It focuses on using Python's `urllib` and `requests` libraries to interact with web servers, handle HTTP requests, and process responses. By completing this project, you will gain a deeper understanding of how to automate web interactions and handle various HTTP scenarios.

## Requirements

| Category         | Details |
|------------------|---------|
| **Project Type** | Mandatory |
| **Review**       | Manually reviewed by peers or TAs |
| **Ubuntu Version** | Ubuntu 20.04 LTS |
| **Python Version** | Python 3.8.5 |
| **Python Scripts** | All Python scripts must start with `#!/usr/bin/python3` and follow PEP 8 style guidelines |
| **README**       | A README.md file at the root of the project folder is mandatory |

## General Requirements

1. **Python Scripts**:
   - The first line of all Python files should be `#!/usr/bin/python3`.
   - Code should follow `pycodestyle` (version 2.8.*).
   - All modules, classes, and functions must be documented with meaningful sentences.
   - All files must be executable.
   - The length of your files will be tested using `wc`.
   - Your code should not be executed when imported (use `if __name__ == "__main__":`).

2. **Ubuntu 20.04 LTS**: All files will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3.8.5.

## Tasks

| Task                          | Description                                  | Files                         |
|-------------------------------|----------------------------------------------|-------------------------------|
| **0. What's my status? #0**   | Write a Python script that fetches `https://alx-intranet.hbtn.io/status` using `urllib` | 0-hbtn_status.py |
| **1. Response header value #0** | Write a Python script that takes in a URL, sends a request, and displays the value of the `X-Request-Id` header | 1-hbtn_header.py |
| **2. POST an email #0**       | Write a Python script that takes in a URL and an email, sends a POST request with the email as a parameter, and displays the response body | 2-post_email.py |
| **3. Error code #0**          | Write a Python script that takes in a URL, sends a request, and displays the body of the response. Handle `urllib.error.HTTPError` exceptions | 3-error_code.py |
| **4. What's my status? #1**   | Write a Python script that fetches `https://alx-intranet.hbtn.io/status` using `requests` | 4-hbtn_status.py |
| **5. Response header value #1** | Write a Python script that takes in a URL, sends a request, and displays the value of the `X-Request-Id` header using `requests` | 5-hbtn_header.py |
| **6. POST an email #1**       | Write a Python script that takes in a URL and an email, sends a POST request with the email as a parameter, and displays the response body using `requests` | 6-post_email.py |
| **7. Error code #1**          | Write a Python script that takes in a URL, sends a request, and displays the body of the response. Handle HTTP status codes >= 400 using `requests` | 7-error_code.py |
| **8. Search API**             | Write a Python script that takes in a letter, sends a POST request to `http://0.0.0.0:5000/search_user` with the letter as a parameter, and processes the JSON response | 8-json_api.py |
| **9. My GitHub!**             | Write a Python script that takes your GitHub credentials (username and password), uses the GitHub API to display your id | 10-my_github.py |
| **10. Time for an interview!** | Write a Python script that lists 10 commits (from the most recent to oldest) of the repository “rails” by the user “rails” using the GitHub API | 100-github_commits.py |

## Learning Objectives

By completing this project, you will:

- Understand how to use Python's `urllib` and `requests` libraries to interact with web servers.
- Learn how to handle HTTP requests and responses in Python.
- Gain experience with error handling in network requests.
- Understand how to process JSON responses from APIs.
- Learn how to authenticate and interact with the GitHub API.

## Submission

- **GitHub Repository**: [alx-higher_level_programming](https://github.com/Achrafsadeq/alx-higher_level_programming)
- **Directory**: 0x11-python-network_1

---

### Mission Director

This project is part of the ALX Software Engineering Program.

### Developer

**Codename**: Achraf Sadeq

### Acknowledgments

This project was developed by Holberton School, in collaboration with the ALX Software Engineering Program, to provide practical, hands-on learning experiences in a professional and real-world context. It aims to equip learners with the skills and knowledge necessary to tackle complex challenges in software engineering.
