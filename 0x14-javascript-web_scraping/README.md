# 0x14. JavaScript - Web Scraping

## Background Context

This project focuses on web scraping using JavaScript. You will learn how to interact with web pages, extract data, and manipulate it using JavaScript. By completing this project, you will gain hands-on experience with Node.js, the `request` module, and working with APIs.

## Requirements

| Category         | Details |
|------------------|---------|
| **Project Type** | Mandatory |
| **Review**       | Manually reviewed by peers or TAs |
| **Environment**  | Ubuntu 20.04 LTS |
| **README**       | A `README.md` file at the root of the project folder is mandatory |
| **File Extension** | All JavaScript files must end with `.js` |

## General Requirements

1. **Node.js Version**: All files will be interpreted on Ubuntu 20.04 LTS using Node.js (version 14.x).
2. **File Structure**: All files should end with a new line, and the first line of each JavaScript file must be `#!/usr/bin/node`.
3. **Code Style**: Your code should be semistandard compliant (rules of Standard + semicolons on top). Also, as a reference: AirBnB style.
4. **Execution**: All your files must be executable.
5. **Variables**: You are not allowed to use `var`.

## More Info

### Install Node 14
```bash
$ curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
$ sudo apt-get install -y nodejs
```

### Install semi-standard
```bash
$ sudo npm install semistandard --global
```

### Install request module and use it
```bash
$ sudo npm install request --global
$ export NODE_PATH=/usr/lib/node_modules
```

**Note**: The `request` module has been deprecated since February 2020 - the team is considering an alternative to replace this module - however, it’s a really simple and powerful module for practicing web-scraping in JavaScript (and still used a lot in the industry).

## Tasks

| Task                          | Description                                  | Files                         |
|-------------------------------|----------------------------------------------|-------------------------------|
| **0. Readme**                 | Write a script that reads and prints the content of a file | `0-readme.js` |
| **1. Write me**               | Write a script that writes a string to a file | `1-writeme.js` |
| **2. Status code**            | Write a script that displays the status code of a GET request | `2-statuscode.js` |
| **3. Star wars movie title**  | Write a script that prints the title of a Star Wars movie where the episode number matches a given integer | `3-starwars_title.js` |
| **4. Star wars Wedge Antilles** | Write a script that prints the number of movies where the character “Wedge Antilles” is present | `4-starwars_count.js` |
| **5. Loripsum**               | Write a script that gets the contents of a webpage and stores it in a file | `5-request_store.js` |
| **6. How many completed?**    | Write a script that computes the number of tasks completed by user id | `6-completed_tasks.js` |
| **7. Who was playing in this movie?** | Write a script that prints all characters of a Star Wars movie | `100-starwars_characters.js` |
| **8. Right order**            | Write a script that prints all characters of a Star Wars movie in the same order of the list “characters” in the /films/ response | `101-starwars_characters.js` |

## Submission

- **GitHub Repository**: [alx-higher_level_programming](https://github.com/Achrafsadeq/alx-higher_level_programming)
- **Directory**: `0x14-javascript-web_scraping`

---

### Mission Director

This project is part of the ALX Software Engineering Program.

### Developer

**Codename**: Achraf Sadeq

### Acknowledgments

This project was developed by Holberton School, in collaboration with the ALX Software Engineering Program, to provide practical, hands-on learning experiences in a professional and real-world context. It aims to equip learners with the skills and knowledge necessary to tackle complex challenges in software engineering.


