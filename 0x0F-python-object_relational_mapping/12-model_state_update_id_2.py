#!/usr/bin/python3
"""
Script that changes the name of a State object from the database hbtn_0e_6_usa
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

    #Query the State object with id = 2
    state = session.query(State).filter(State.id == 2).first()

    if state:
        #Update the name of the State object
        state.name = "New Mexico"

        #Commit the session to persist the changes
        session.commit()
