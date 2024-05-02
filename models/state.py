#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models import storage_type
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """ State class """
    if storage_type == 'db':
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship("City",  backref="state", cascade="delete")

    else:
        name = ""

        @property
        def cities(self):
            """Get a list of all related City objects."""
            from models import storage
            city_list = []
            for j, city in models.storage.all(City).items():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
