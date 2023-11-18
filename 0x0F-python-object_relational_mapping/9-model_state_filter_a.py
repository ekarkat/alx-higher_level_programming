#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Sess = sessionmaker(bind=engine)
    sess = Sess()

    res = sess.query(State).order_by(State.id).filter(State.name.like("%a%"))

    for x in res:
        print("{}: {}".format(x.id, x.name))
