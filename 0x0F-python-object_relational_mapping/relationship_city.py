#!/usr/bin/python3
"""
Represents a City linked to the MySQL table 'cities'.
"""


from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """
    Attributes:
    id (int): Represents the unique identifier for the city.
    name (str): Represents the name of the city.
    state_id (int): Reps the identifier of the state associated with the city.
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
