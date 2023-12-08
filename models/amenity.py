#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Table, ForeignKey, relationship
from models.amenity_place import place_amenity

class Amenity(BaseModel, Base):
    __tablename__ = 'amenities'
    name = Columnn(String(128), nullable=False)

""" Define the association table for the many-to-many
relationship between Place and Amenity"""

place_amenity = Table(
    'place_amenity',
    Base.metadata,
    Column(
        'place_id',
        String(60),
        ForeignKey('places.id'),
        primary_key=True,
        nullable=False),
    Column(
        'amenity_id',
        String(60),
        ForeignKey('amenities.id'),
        primary_key=True,
        nullable=False))

place_amenity_rel = relationship('Place', secondary=place_amenity,
             viewonly=False)


class Amenity(BaseModel, Base):
    """inherits from BaseModel and Base
    name = ""
    """
    __tablename__ = 'amenities'

    name = Column(String(128), nullable=False)
    place_amenity = relationship(
        'Place',
        secondary=place_amenity,
        viewonly=False)
