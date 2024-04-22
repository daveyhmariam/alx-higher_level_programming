#!/usr/bin/python3
"""
lists all State objects that contain the letter a from the database hbtn_0e_6_usa
"""
from model_state import Base, State
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
    for inst in session.query(State).filter(State.name.like(f'%a%')).all():
        print(inst.id, inst.name, sep=": ")
