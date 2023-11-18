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

    sql_cm.execute("SELECT cities.name\
                    FROM cities\
                    inner JOIN states ON cities.state_id = states.id\
                    where states.name = %s\
                    order by cities.id ASC", (argv[4],))

    row = sql_cm.fetchall()

    if not row:
        print("")

    for i in range(len(row)):
        if i == len(row) - 1:
            print(row[i][0])
        else:
            print(row[i][0], end=", ")

    sql_cm.close()
    db.close()
