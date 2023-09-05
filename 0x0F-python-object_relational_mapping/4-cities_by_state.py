#!/usr/bin/python3
"""Lists all cities"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    u = argv[1]
    p = argv[2]
    d = argv[3]
    # connect to db
    db = MySQLdb.connect(host="localhost", user=u, passwd=p, db=d, port=3306)

    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM\
    states, cities WHERE states.id=cities.state_id ORDER BY cities.id ASC")

    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()
