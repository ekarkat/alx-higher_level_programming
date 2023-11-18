#!/usr/bin/python3
"""
Lists all states with a name starting with N (upper N) from the
"""

from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=argv[1],
            passwd=argv[2],
            database=argv[3])

    sql_cm = db.cursor()

    sql_cm.execute("SELECT * FROM states WHERE name LIKE 'N%'")

    for x in sql_cm:
        print(x)

    sql_cm.close()
    db.close()
