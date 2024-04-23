#!/usr/bin/python3
"""
prints all City objects from the database hbtn_0e_14_usa
"""

from model_city import City
from model_state import State, Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import sys


if __name__ == "__main__":

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1],
                                   sys.argv[2],
                                   sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(engine)
    session = Session()

    for state_id, city_id, city_state_id in (
        session.query(State.id, City.id, City.state_id)
        .filter(State.id == City.state_id)
    ):
        print(
            f"State ID: {state_id}, City ID: {city_id},
            City State ID: {city_state_id}")
