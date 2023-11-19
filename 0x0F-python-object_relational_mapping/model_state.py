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
