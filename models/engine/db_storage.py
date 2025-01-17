#!/usr/bin/Python3
"""Module that defines the engine for the MySQL database"""
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
import os 
from os import getenv
from models.base_model import Base
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class DBStorage:
    """Database Storage Engine"""
    __engine = None
    __session = None

    def __init__(self):
        """Initialize DBStorage instance"""
        env = getenv("HBNB_ENV")
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(os.getenv('HBNB_MYSQL_USER'),
                                             os.getenv('HBNB_MYSQL_PWD'),
                                             os.getenv('HBNB_MYSQL_HOST'),
                                             os.getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)
        if env == "test":
            Base.metadata.drop_all(self._engine)
        self.reload()

    def all(self, cls=None):
        """implementation for query to return a dictionary of objects"""
        dic = {}
        if cls:
            if type(cls) is str:
                cls = eval(cls)
            query = self.__session.query(cls)
            for elem in query:
                key = "{}.{}".format(type(elem).__name__, elem.id)
                dic[key] = elem
        else:
            lista = [State, City, User, Place, Review, Amenity]
            for clase in lista:
                query = self.__session.query(clase)
                for elem in query:
                    key = "{}.{}".format(type(elem).__name__, elem.id)
                    dic[key] = elem
        return (dic)

    def new(self, obj):
        """Add new obj to a DB"""
        self.__session.add(obj)

    def save(self):
        """Save object to current DB"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete/remove obj from DB"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Reload current DB"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """Close SQLAchemy session"""
        self.__session.close()
