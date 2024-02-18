#!/usr/bin/python3

import MySQLdb
import sys
"""Lists all states from the database hbtn_0e_0_usa
"""
db = MySQLdb.connect(db=sys.argv[3], host="localhost",
                     port=3306, user=sys.argv[1], passwd=sys.argv[2])
cur = db.cursor()
cur.execute("SELECT * from states ORDER BY id")

rows = cur.fetchall()
for row in rows:
    print(row)
