#!/usr/bin/python3
"""script that takes in an argument and
    displays all values in the states table
    of hbtn_0e_0_usa where name matches the argument.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    connection = MySQLdb.connect(host="localhost",
                                 user=sys.argv[1],
                                 passwd=sys.argv[2],
                                 db=sys.argv[3])
    cur = connection.cursor()
    cur.execute("""SELECT * FROM states WHERE name LIKE BINARY  '{}'""".format(sys.argv[4]))
    result = cur.fetchall()
    for r in result:
        print(r)
    cur.close()
    connection.close()
