#!/usr/bin/python3
"""Script that lists all State objects that contain the letter a"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == '__main__':
    #Set up database connection
    username = sys.argv[1]
    password = sys.argv[2]
    name = sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, name))

    #Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    #Create a session
    session = Session()

    #Query for all states containing 'a' and sort by ID
    states = session.query(State).filter(State.name.like('%a%')).order_by(State.id)

    #Print the results
    for state in states:
        print("{}: {}".format(state.id, state.name))
