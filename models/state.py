#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from models.city import City
import os


class State(BaseModel):
    """ State class
    name = ""
    """

    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    
    if getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship('City', cascade='all, delete', backref='state')
    else:
        @property
        def cities(self):
            """public getter method cities to
            return the list of City"""
            my_list = []
            for city in models.storage.all(City).values():
                if city.state_id == self.id:
                    city_list.append(city)
            return my_list       
