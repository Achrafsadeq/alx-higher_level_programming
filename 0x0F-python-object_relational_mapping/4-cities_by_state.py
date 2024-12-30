#!/usr/bin/python3
"""
Lists all cities from the database hbtn_0e_4_usa.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Capture command-line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Connect to the database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name
    )

    # Create a cursor object to execute queries
    cursor = db.cursor()

    # SQL query to retrieve cities and their states
    query = """
    SELECT cities.id, cities.name, states.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    ORDER BY cities.id ASC;
    """

    # Execute the query
    cursor.execute(query)

    # Fetch all the results
    results = cursor.fetchall()

    # Print each row
    for row in results:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()
