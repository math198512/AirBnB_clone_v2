#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from models.state import State
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, ForeignKey
from os import environ

storage_engine = environ.get("HBNB_TYPE_STORAGE")


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    if (storage_engine == "db"):
        __tablename__ = "cities"
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    else:
        state_id = ""
        name = ""
