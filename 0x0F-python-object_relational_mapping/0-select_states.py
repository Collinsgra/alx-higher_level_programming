#!/usr/bin/python3
"""Script to retrieve and list all states from a database"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    # Retrieve database connection parameters from command line arguments
    username = argv[1]
    password = argv[2]
    database_name = argv[3]

    # Establish a connection to the database
    db = MySQLdb.connect(host="localhost", user=username, passwd=password, db=database_name, port=3306)

    # Create a cursor object for executing SQL queries
    cursor = db.cursor()

    # Execute an SQL query to select all states and order them by id
    cursor.execute("SELECT * FROM states ORDER BY id ASC;")

    # Fetch and print all records retrieved by the query
    for row in cursor.fetchall():
        print(row)

    # Close the cursor and the database connection
    cursor.close()
    db.close()

