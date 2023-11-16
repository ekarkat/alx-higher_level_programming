# 0x0F. Python - Object-relational mapping

## Synopsis
Project for Holberton School, within the "Python" and "Object-oriented programming" tracks, focusing on SQL, MySQL, and Object-Relational Mapping (ORM) using SQLAlchemy.

## Prerequisites
Ensure your MySQL server is in version 8.0. [How to install MySQL 8.0 in Ubuntu 20.04](link_to_mysql_installation_guide)

## Background Context
In this project, the goal is to connect two worlds: Databases and Python! The project has two parts:
1. Using the MySQLdb module to connect to a MySQL database and execute SQL queries.
2. Using the SQLAlchemy module (an Object-Relational Mapper - ORM).

The biggest difference with an ORM is that there are no more direct SQL queries. The ORM abstracts the storage to the usage, making your primary concern "What can I do with my objects?" rather than "How is this object stored? where? when?". The code becomes storage-type independent and allows easy switching between storage systems without rewriting the entire project.

Example without ORM:

```py
import MySQLdb

conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="my_db", charset="utf8")
cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC")
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()
```
With an ORM:

```py
engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format("root", "root", "my_db"), pool_pre_ping=True)
Base.metadata.create_all(engine)

session = Session(engine)
for state in session.query(State).order_by(State.id).all(): # HERE: no SQL query, only objects!
    print("{}: {}".format(state.id, state.name))
session.close()
```

Do you see the difference? Cool, right?

The biggest difficulty with ORM is: The syntax!

Indeed, all of them have the same type of syntax, but not always. Please read tutorials and don’t read the entire documentation before starting, just jump on it if you don’t get something.

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General
- Why Python programming is awesome
- How to connect to a MySQL database from a Python script
- How to SELECT rows in a MySQL table from a Python script
- How to INSERT rows in a MySQL table from a Python script
- What ORM means
- How to map a Python Class to a MySQL table
- How to create a Python Virtual Environment