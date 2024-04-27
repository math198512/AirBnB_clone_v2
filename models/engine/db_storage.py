#!/usr/bin/python3
"""This module defines a class to manage database storage for hbnb clone"""
import models
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from models.base_model import BaseModel, Base
from models import city, state
from models.base_model import BaseModel
from models.city import City
from models.review import Review
from models.state import State
from models.user import User
from models.place import Place
from models.amenity import Amenity


class DBStorage():
    """This class manages storage of hbnb models in database"""
    __engine = None
    __session = None

    def __init__(self):
        """"initializes db storage"""
        HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
        HBNB_ENV = getenv('HBNB_ENV')
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".format(
            HBNB_MYSQL_USER,
            HBNB_MYSQL_PWD,
            HBNB_MYSQL_HOST,
            HBNB_MYSQL_DB), pool_pre_ping=True)
        env = HBNB_ENV
        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session all objects"""
        objects_list = []
        if cls:
            if isinstance(cls, str):
                try:
                    cls = globals()[cls]
                except KeyError:
                    pass
            if issubclass(cls, Base):
                objects_list = self.__session.query(cls).all()
        else:
            for subclass in Base.__subclasses__():
                objects_list.extend(self.__session.query(subclass).all())
        objects_dict = {}
        for obj in objects_list:
            key = "{}.{}".format(ojb.__class__.__name__, obj.id)
            objects_dict[key] = obj
        return objects_dict

    def new(self, obj):
        """add object to current session
        """
        self.__session.add(obj)

    def save(self):
        """commit current done work
        """
        self.__session.commit()

    def reload(self):
        """reload the session
        """
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Scope = scoped_session(Session)
        self.__session = Scope()

    def delete(self, obj=None):
        """delete obj from session
        """
        if (obj is None):
            self.__session.delete(obj)
