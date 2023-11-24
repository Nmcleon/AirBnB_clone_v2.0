#!/usr/bin/python3
""" File defining the place_amenity table"""
from models.base_model import BaseModel, Base
from sqlalchemy import Table, Column, String, ForeignKey
from models.base_model import Base

"""Define the association table for the many-to-many relationship between Place and Amenity"""
place_amenity = Table(
    'place_amenity',
    Base.metadata,
    Column(
        'place_id',
        String(60),
        ForeignKey('place.id'),
        primary_key=True,
        nullable=False),
    Column(
        'amenity_id',
        String(60),
        ForeignKey('amenities.id'),
        primary_key=True,
        nullable=False)
)
