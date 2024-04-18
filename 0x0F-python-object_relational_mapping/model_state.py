#!/usr/bin/python3
"""class definition of a State and an instance Base = declarative_base
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, String, MetaData, Column

Base = declarative_base()


class State(Base):
    __table__ = "states"

    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String, nullable=False)
