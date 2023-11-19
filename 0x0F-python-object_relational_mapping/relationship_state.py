#!/usr/bin/python3
"""
Defines a state model
"""
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """Represents a State linked to the MySQL table 'states'."""

    __tablename__ = 'states'

    id = Column(
            Integer,
            primary_key=True,
            nullable=False,
            autoincrement=True
            )
    """int: Represents the unique identifier for the state."""

    name = Column(String(128), nullable=False)

    cities = relationship("City", cascade="all, delete", backref="state")
    """
    relationship: Represents the relationship with City objects.
    If State object is deleted, all linked City objects are automatically deleted.
    Reference from a City object to its State is named 'state'.
    """
