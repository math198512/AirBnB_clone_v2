#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models import storage_type
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """ State class: class to represent states of cities"""
    __tablename__ = "states"
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship(
            'City', back_populates='state',
            cascade='all, delete, delete-orphan')
    else:
        name = ""

        @property
        def cities(self):
            """cities list
            """
            result = []
            cities_dict = models.storage.all(City)
            for key, value cities_dict.items():
                if (value.state_id == self.id):
                    result.append(value)
            return result
