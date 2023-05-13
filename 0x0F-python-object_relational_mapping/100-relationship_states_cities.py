#!/usr/bin/python3
"""
Script that creates the State "California" with the City "San Francisco"
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

    #Create the State "California" with the City "San Francisco"
    california = State(name="California")
    san_francisco = City(name="San Francisco", state=california)
    session.add(california)
    session.add(san_francisco)
    session.commit()
