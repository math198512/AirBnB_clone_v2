#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
import models
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """ State class """
    if getenv("HBNB_TYPE_STORAGE") == 'db':
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship("City",  backref="state", cascade="delete")

    else:
        name = ""

        @property
        def cities(self):
            """Get a list of all related City objects."""
            city_list = []
            for city in models.storage.all(models.city.City).values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
