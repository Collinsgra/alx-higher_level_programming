#!/usr/bin/python3
"""
This script retrieves and lists states with names starting
with the letter 'N' from the 'hbtn_0e_0_usa' database.
"""

import MySQLdb as db
from sys import argv

"""
Establish a connection to the database and retrieve
states that meet the specified criteria.
"""

if __name__ == '__main__':
    db_connection = db.connect(host="localhost", port=3306,
                            user=argv[1], passwd=argv[2], db=argv[3])
    db_cursor = db_connection.cursor()

    db_cursor.execute(
        "SELECT * FROM states WHERE name LIKE BINARY 'N%' \
                ORDER BY states.id ASC")

    selected_rows = db_cursor.fetchall()

    for row in selected_rows:
        print(row)

