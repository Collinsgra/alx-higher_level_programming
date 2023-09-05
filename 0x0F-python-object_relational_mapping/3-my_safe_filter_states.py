#!/usr/bin/python3
"""list of state protected by sql injection"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    u = argv[1]
    p = argv[2]
    d = argv[3]
    n = argv[4]
    # connect to db
    db = MySQLdb.connect(host="localhost", user=u, passwd=p, db=d, port=3306)

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name=%s ORDER BY id ASC", (n,))

    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()
