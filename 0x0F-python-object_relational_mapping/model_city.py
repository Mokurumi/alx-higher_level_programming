#!/usr/bin/python3
"""
Represents a City linked to the MySQL table 'cities'.
"""


from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """
    Attributes:
    id (int): Represents the unique identifier for the city.
    name (str): Represents the name of the city.
    state_id (int): Reps the identifier of the state associated with the city.
    """

    __tablename__ = 'cities'
    id = Column(
            Integer,
            primary_key=True,
            nullable=False,
            autoincrement=True
            )
    """int: Represents the unique identifier for the city."""

    name = Column(String(128), nullable=False)
    """str: Represents the name of the city."""

    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    """int: Represents the identifier of the state associated with the city."""
