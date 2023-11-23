#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from os import getenv
from models import storage
from models.amenity import Amenity


place_amenity = Table(
    'place_amenity',
    Base.metadata,
    Column('place_id',
           String(60),
           ForeignKey('places.id'),
           primary_key=True,
           nullable=False),
    Column('amenity_id',
           String(60),
           ForeignKey('amenities.id'),
           primary_key=True,
           nullable=False)
    )

<<<<<<< HEAD
if storage_type == 'db'
    place_amenity = Table('place_amenity', Base.metadata,
                          Column('place_id', String(60),
                                 ForeignKey('places.id'),
                                 primary_key=True,
                                 nullable=False),
                          Column('amenity_id', String(60),
                                 ForeignKey('amenities.id'),
                                 primary_key=True,
                                 nullable=False)
                          )
=======
>>>>>>> 6754656dc1c1f96f3292a4c9d41e3a36d3a0ccba

class Place(BaseModel, Base):
    """This is a place class model """
    __tablename__ = 'places'
    if storage_tpye = 'db'
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        reviews = relationship('Review', backref='place',
                               cascade='all, delete, delete-orphan')
        amenities = relationship('Amenity', secondary=place_amenity,
                                 viewonly=False, backref='place_amenities')
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

<<<<<<< HEAD
        @property
        def reviews(self):
            ''' The review instances relate with class review
                FileStorage_relationship between_Place and_Review
            '''
            from models import storage
            all_rev = storage.all(Review)
            list_rev = []
            for rev in all_rev.values():
                if rev.place_id == self.id:
                    list_rev.append(rev)
            return list_rev

        @property
        def amenities(self):
            ''' The amenity instances represent al relatioship
            with class amenities.
                It contains all Amenity.id linked to Place
            '''
            from models import storage
            all_amty = storage.all(Amenity)
            list_amty = []
            for amt in all_amty.values():
                if amty.id in self.amenity_ids:
                    list_amty.append(amen)
            return list_amty

        @amenities.setter
        def amenities(self, obj):
            ''' This method set amenity objects '''
            if obj is not None:
                if isinstance(obj, Amenity):
                    if obj.id not in self.amenity_ids:
                        self.amenity_ids.append(obj.id)
