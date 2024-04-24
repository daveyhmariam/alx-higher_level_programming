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
    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(State.name,
                           City.id,
                           City.name).filter(State.id == City.state_id)
    for inst in cities:
        print(f"{inst[0]}: ({inst[1]}) {inst[2]}")
