#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
import os


class State(BaseModel):
    """ State class
    name = ""
    """

    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship('City', cascade='all, delete', backref='state')
    else:
        @property
        def cities(self):
            """public getter method cities to
            return the list of City"""
            from models.city import City
            from models import storage

            my_list = []
            all_cities = storage.all(City)
            for city in all_cities.values():
                if city.state_id == self.id:
                    my_list.append(city)
            return my_list

