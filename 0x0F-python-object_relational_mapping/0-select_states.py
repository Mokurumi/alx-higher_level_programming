#!/usr/bin/python3
"""
Retrieves and lists all states from the specified MySQL database.
"""


import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(
            host="localhost",
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            port=3306
            )

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states")
    states = cursor.fetchall()
    for state in states:
        print(state)
    cursor.close()
    db.close()