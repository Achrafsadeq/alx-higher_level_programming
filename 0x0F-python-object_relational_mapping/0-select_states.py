#!/usr/bin/python3
"""
Fetches and lists all states from the MySQL database `hbtn_0e_0_usa`.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Parse command-line arguments for database credentials
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Establish a connection to the MySQL database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name
    )

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Execute the SQL query to retrieve all states ordered by ID
    cursor.execute("SELECT * FROM states ORDER BY id ASC;")

    # Fetch all rows from the query result and print them
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close the cursor and database connection to release resources
    cursor.close()
    db.close()
