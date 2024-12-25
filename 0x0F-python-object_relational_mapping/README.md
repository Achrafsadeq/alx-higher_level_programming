# 0x0F. Python - Object Relational Mapping

## Description

This project introduces the concept of Object-Relational Mapping (ORM) in Python, utilizing libraries like MySQLdb and SQLAlchemy to interact with MySQL databases. You’ll learn how to bridge the gap between object-oriented programming and relational databases.

## Learning Objectives

At the end of this project, you should be able to explain:

- How to connect to a MySQL database from a Python script
- The differences between executing SQL queries directly and using an ORM
- How to map Python classes to MySQL tables using SQLAlchemy
- How to perform Create, Read, Update, and Delete (CRUD) operations using SQLAlchemy
- How to handle database transactions safely
- Best practices for using Python and SQL together

## Requirements

- **OS**: Ubuntu 20.04 LTS
- **Python**: Version 3.8.5
- **MySQLdb**: Version 2.0.x
- **SQLAlchemy**: Version 1.4.x
- **Code Style**: Pycodestyle (version 2.8.\*)
- All files should be executable and end with a new line
- The first line of all scripts should be exactly `#!/usr/bin/python3`
- All modules, classes, and functions must have proper documentation

## Setup

### Install and Activate Virtual Environment

```bash
$ sudo apt-get install python3.8-venv
$ python3 -m venv venv
$ source venv/bin/activate
```

### Install MySQLdb

```bash
$ sudo apt-get install python3-dev libmysqlclient-dev zlib1g-dev
$ pip3 install mysqlclient
$ python3 -c "import MySQLdb; print(MySQLdb.version_info)"
```

### Install SQLAlchemy

```bash
$ pip3 install SQLAlchemy
$ python3 -c "import sqlalchemy; print(sqlalchemy.__version__)"
```

## Project Tasks

| **Task**                         | **Description**                                                         | **File**                        |   
| -------------------------------- | ----------------------------------------------------------------------- | ------------------------------- |  
| **0. Get all states**            | Write a script that lists all states from the database `hbtn_0e_0_usa`. | `0-select_states.py`            |   
| **1. Filter states**             | Lists all states with names starting with `N` (upper case).             | `1-filter_states.py`            |    
| **2. Filter states by input**    | Displays states matching user input.                                    | `2-my_filter_states.py`         |    
| **3. SQL Injection**             | Securely handle SQL injection in user input.                            | `3-my_safe_filter_states.py`    |   
| **4. Cities by states**          | Lists all cities and their states.                                      | `4-cities_by_state.py`          |    
| **5. All cities by state**       | Lists all cities of a state given by user input.                        | `5-filter_cities.py`            | 
| **6. First state model**         | Define a `State` class using SQLAlchemy.                                | `model_state.py`                |   
| **7. All states via SQLAlchemy** | Use SQLAlchemy to list all `State` objects.                             | `7-model_state_fetch_all.py`    |
| **8. First state**               | Print first State object from database                                  | `8-model_state_fetch_first.py`  |
| **9. Contains a**                | List State objects containing letter 'a'                                | `9-model_state_filter_a.py`     |
| **10. Get a state**              | Print State object matching name argument                               | `10-model_state_my_get.py`      |
| **11. Add a new state**          | Add "Louisiana" State object to database                                | `11-model_state_insert.py `     |
| **12. Update a state**           | Change name of State with id=2 to "New Mexico"                          | `12-model_state_update_id_2.py` |
| **13. Delete states**            | Delete State objects containing letter 'a'                              | `13-model_state_delete_a.py `    |
| **14. Cities in state**          | Print all City objects from database                                    | `model_city.py, 14-model_city_fetch_by_state.py` |
| **15. City relationship**         | Improve state/city models with relationships                           | `relationship_city.py, relationship_state.py, 100-relationship_states_cities.py` |
| **16. List relationship**         | List States and corresponding Cities                                   | `101-relationship_states_cities_list.py` |
| **17. From city**                | List all City objects with linked State names                           | `102-relationship_cities_states_list.py` |
 
## General Guidelines

- Follow best practices for SQL and Python integration.
- Avoid hardcoding sensitive information like database credentials.
- Test your scripts with various input values, including edge cases.
- Use proper error handling for database operations.
- Always close database connections after use.

## Mission Director
This project is supervised by the ALX Software Engineering Program.

## Developer
**Codename**: Achraf Sadaeq

## Acknowledgments
Holberton School, in collaboration with the ALX Software Engineering Program, developed this project for educational purposes.
