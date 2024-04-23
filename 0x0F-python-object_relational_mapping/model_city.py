#!/usr/bin/python3
"""
ORM definition of the cities table
"""
from model_state import Base
from sqlalchemy import Column, String, MetaData, Integer, ForeignKey

class City(Base):
    """
    Class with attributes of City

    """

    __tablename__ = 'Cities'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
