#!/usr/bin/python3
"""
takes in an argument and displays all values in the states table
"""


import sys
import MySQLdb


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("
        Usage: python script.py <username> <password> <database> <state_name>
        ")
    else:
        db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                db=sys.argv[3])
        cursor = db.cursor()
        cursor.execute("""
                SELECT * FROM states
                WHERE name LIKE BINARY '{}'
                ORDER BY states.id ASC
                """.format(sys.argv[4]).strip("'"))
        [print(state) for state in cursor.fetchall()]
