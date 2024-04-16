#!/usr/bin/python3
""" script that takes in the name of a state
    as an argument and lists all cities of that state,
    using the database hbtn_0e_4_usa
"""
import MySQLdb
import sys

if __name__ == "__main__":

    connection = MySQLdb.connect(user=sys.argv[1],
                                 passwd=sys.argv[2],
                                 db=sys.argv[3])

    cursor = connection.cursor()
    cursor.execute("""SELECT cities.name FROM cities WHERE\
                        cities.state_id=(SELECT id\
                        FROM states WHERE name=%s)""", (sys.argv[4], ))
    result = cursor.fetchall()
    print([r[0] for r in result])

    cursor.close()
    connection.close()
