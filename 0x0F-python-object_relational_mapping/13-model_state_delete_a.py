#!/usr/bin/python3
"""
Script that deletes all State objects with a name containing the letter a
from the database hbtn_0e_6_usa
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    #Create the engine
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    engine = create_engine(f"mysql+mysqldb://{username}:{password}@localhost:3306/{database}")

    #Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    #Create a Session
    session = Session()

    #Query the State objects with names containing the letter "a"
    states = session.query(State).filter(State.name.like("%a%")).all()

    if states:
        #Delete the State objects
        for state in states:
            session.delete(state)

        #Commit the session to persist the changes
        session.commit()
