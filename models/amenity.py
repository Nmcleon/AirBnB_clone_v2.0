#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Table, ForeignKey
from sqlalchemy.orm import relationship

class Amenity(BaseModel, Base):
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)

    __table_args__ = {'extend_existing': True}

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
        nullable=False),
    extend_existing=True
    )

place_amenity_rel = relationship('Place', secondary=place_amenity,
             viewonly=False)
