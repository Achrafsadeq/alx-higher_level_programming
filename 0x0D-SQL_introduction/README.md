# 0x0D. SQL - Introduction

## Description

This project introduces the basics of SQL, including database management, table creation, data manipulation, and query execution. It focuses on understanding SQL commands and their applications in managing relational databases.

---

## Requirements

| Category          | Details                                                                 |
|-------------------|-------------------------------------------------------------------------|
| Editors           | vi, vim, emacs                                                         |
| Execution         | Ubuntu 20.04 LTS using MySQL 8.0 (version 8.0.25)                      |
| File Endings      | All files should end with a new line                                   |
| Comments          | Each SQL file should have a comment describing the task               |
| SQL Syntax        | All SQL keywords should be in uppercase (e.g., SELECT, WHERE)         |
| README            | A README.md file at the root of the project folder is mandatory       |
| File Length       | File length will be tested using `wc`                                 |
| Plagiarism        | Any form of plagiarism is strictly forbidden and will result in removal from the program |

---

## Project Structure

| Task | Description | File |
|------|-------------|------|
| 0    | Write a script that lists all databases of your MySQL server. | `0-list_databases.sql` |
| 1    | Create the database `hbtn_0c_0` if it does not already exist. | `1-create_database_if_missing.sql` |
| 2    | Delete the database `hbtn_0c_0` if it exists.                 | `2-remove_database.sql` |
| 3    | List all tables in a specific database.                      | `3-list_tables.sql` |
| 4    | Create a table `first_table` in a database with specific fields. | `4-first_table.sql` |
| 5    | Display the full description of `first_table`.               | `5-full_table.sql` |
| 6    | List all rows in `first_table`.                               | `6-list_values.sql` |
| 7    | Insert a row into `first_table`.                              | `7-insert_value.sql` |
| 8    | Count the number of records with `id = 89` in `first_table`.  | `8-count_89.sql` |
| 9    | Create `second_table` with predefined rows.                   | `9-full_creation.sql` |
| 10   | List records in `second_table` ordered by score (descending). | `10-top_score.sql` |
| 11   | Select records from `second_table` with scores >= 10.         | `11-best_score.sql` |
| 12   | Update Bob’s score to 10 using only the `name` field.          | `12-no_cheating.sql` |
| 13   | Remove records in `second_table` with score <= 5.             | `13-change_class.sql` |
| 14   | Compute the average score of all records in `second_table`.   | `14-average.sql` |
| 15   | List the number of records per score, sorted by count.        | `15-groups.sql` |
| 16   | List all records in `second_table` excluding rows without `name`. | `16-no_link.sql` |
| 17   | Convert `hbtn_0c_0` database and its tables to UTF8 (utf8mb4). | `100-move_to_utf8.sql` |
| 18   | Display the average temperature (Fahrenheit) by city, ordered by temperature. | `101-avg_temperatures.sql` |
| 19   | Display the top 3 cities' temperatures during July and August, ordered by temperature. | `102-top_city.sql` |
| 20   | Display the max temperature of each state, ordered by state name. | `103-max_state.sql` | 

---

## General Learning Objectives

- What is a database
- What is a relational database
- What does SQL stand for and its uses
- Basic SQL commands: `CREATE`, `SELECT`, `INSERT`, `UPDATE`, `DELETE`
- How to create and manage databases and tables
- How to insert, retrieve, and manipulate data in a table
- How to use `WHERE`, `ORDER BY`, and `LIMIT` clauses
- How to join tables and use relationships between them
- Understanding primary keys and constraints

---

## SQL Test Cases

- **Allowed Editors**: vi, vim, emacs  
- **All files** should end with a new line.  
- **Execution**:  
  ```bash
  $ mysql -hlocalhost -uroot -p < script.sql
  ```
- **Documentation**:  
  Each SQL file must have comments describing the task.  

---

### How Usage

**Listing Databases:**
```bash
$ cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
Enter password:
Database
information_schema
mysql
performance_schema
sys
```

**Creating a Table:**
```bash
$ cat 4-first_table.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password:
```

---

## Mission Director
This project is supervised by the ALX Software Engineering Program.

## Developer
**Codename**: Achraf Sadaeq

## Acknowledgments
Holberton School, in collaboration with the ALX Software Engineering Program, developed this project for educational purposes.

