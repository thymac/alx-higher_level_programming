#!/usr/bin/python3
"""
Script that prints the first State object from the database hbtn_0e_6_usa
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

    #Query the first State object
    first_state = session.query(State).order_by(State.id).first()

    #Print the result or "Nothing" if it doesn't exist
    if first_state:
        print(f"{first_state.id}: {first_state.name}")
    else:
        print("Nothing")
