#!/usr/bin/python3
"""
Script that adds the State object "Louisiana" to the database hbtn_0e_6_usa
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    # Create the engine
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    engine = create_engine(f"mysql+mysqldb://{username}:{password}@localhost:3306/{database}")

    #Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    #Create a Session
    session = Session()

    #Create a new State object
    new_state = State(name="Louisiana")

    #Add the new State object to the session
    session.add(new_state)

    # Commit the session to persist the changes
    session.commit()

    #Print the new state's ID
    print(new_state.id)
