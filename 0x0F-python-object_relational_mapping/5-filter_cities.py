#!/usr/bin/python3
"""
lists all cities
"""


import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("""
            SELECT * FROM cities
            INNER JOIN states ON cities.state_id = states.id
            ORDER BY cities.id
            """)
    print(", ".join([city[2]
        for city in cursor.fetchall()
        if city[4] == sys.argv[4]]))
