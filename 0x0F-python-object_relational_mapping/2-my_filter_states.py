#!/usr/bin/python3
"""
Takes in an argument and displays all values in the states table
of `hbtn_0e_0_usa` where name matches the argument.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Parse command-line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=mysql_username,
            passwd=mysql_password,
            db=database_name
        )

        cursor = db.cursor()

        query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(state_name)
        cursor.execute(query)

        rows = cursor.fetchall()
        for row in rows:
            print(row)

    except Exception as e:
        print(f"Error: {e}")

    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'db' in locals():
            db.close()

