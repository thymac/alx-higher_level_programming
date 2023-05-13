#!/usr/bin/python3
"""
Script that prints all City objects from the database hbtn_0e_14_usa
"""
import sys
from model_state import Base, State
from model_city import City
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

    #Query the City objects
    cities = session.query(State, City).join(City).order_by(City.id).all()

    #Display the results
    for state, city in cities:
        print(f"{state.name}: ({city.id}) {city.name}")
