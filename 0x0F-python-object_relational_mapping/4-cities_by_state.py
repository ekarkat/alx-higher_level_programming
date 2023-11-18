#!/usr/bin/python3
"""
lists all cities from the database hbtn_0e_4_usa
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

    sql_cm.execute("SELECT cities.id, cities.name, states.name\
                    FROM cities\
                    inner JOIN states ON cities.state_id = states.id\
                    order by cities.id ASC")

    for x in sql_cm:
        print(x)

    sql_cm.close()
    db.close()
