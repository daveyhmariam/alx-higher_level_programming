#!/usr/bin/python3
"""
lists all City objects from the database hbtn_0e_101_usa
"""
from relationship_city import City
from relationship_state import State, Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import sys


if __name__ == "__main__":

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1],
                                   sys.argv[2],
                                   sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    session = Session()

    result = session.query(City, State.name).order_by(City.id)
    for city, state_name in result:
        print(f"{city.id}: {city.name} -> {state_name}")
