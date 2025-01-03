#!/usr/bin/python3
"""Script to display all values in states table where name matches argument."""
import MySQLdb
import sys


if __name__ == "__main__":
    # Connect to the database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    # Create a cursor object
    cursor = db.cursor()

    # Construct the SQL query to enforce case sensitivity
    query = ("SELECT * FROM states WHERE BINARY name = '{}' "
             "ORDER BY id ASC".format(sys.argv[4]))
    cursor.execute(query)

    # Fetch and display results
    states = cursor.fetchall()
    for state in states:
        print(state)

    # Close the cursor and the connection
    cursor.close()
    db.close()
