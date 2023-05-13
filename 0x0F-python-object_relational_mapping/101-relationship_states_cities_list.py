#!/usr/bin/python3
"""
Script that lists all State objects and corresponding City objects from the database hbtn_0e_101_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import City


if __name__ == "__main__":
    #Create the engine
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    engine = create_engine(f"mysql+mysqldb://{username}:{password}@localhost:3306/{database}")

    #Create all tables defined in the models
    State.metadata.create_all(engine)

    #Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    #Create a Session
    session = Session()

    #Retrieve all State objects with their associated City objects
    states = session.query(State).order_by(State.id).all()

    #Print the results
    for state in states:
        print(f"{state.id}: {state.name}")
        for city in state.cities:
            print(f"    {city.id}: {city.name}")
