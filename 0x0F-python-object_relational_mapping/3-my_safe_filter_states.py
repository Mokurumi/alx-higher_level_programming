#!/usr/bin/python3
"""
takes in an argument and displays all values in the states table
"""


import sys
import MySQLdb


if __name__ == "__main__":
    """main function"""
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name=%s ORDER BY id ASC",
                (sys.argv[4],))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
