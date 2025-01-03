#!/usr/bin/python3
"""
Defines the City class linked to the State class
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from relationship_state import Base
from sqlalchemy.orm import relationship


class City(Base):
    """
    Represents a city in the database.
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    state = relationship("State", back_populates="cities")
