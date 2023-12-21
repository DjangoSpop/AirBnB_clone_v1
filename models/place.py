#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from models.review import Review
from models import storage
from sqlalchemy import Table, Column, String, ForeignKey
from models.base_model import Base
from models.amenity import Amenity
class Place(BaseModel):
    __tablename__ = 'places'
    __tablename__ = 'place_amenity'
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
    reviews = relationship("Review", cascade="all, delete", backref="place")
    amenities = relationship("Amenity", secondary="place_amenity", viewonly=False)
    place_amenity = Table('place_amenity', Base.metadata,
                          Column('place_id', String(60), ForeignKey('places.id'), primary_key=True, nullable=False),
                          Column('amenity_id', String(60), ForeignKey('amenities.id'), primary_key=True, nullable=False)
                          )
    
    @property
    def reviews(self):
        review_list = []
        for review in storage.all(Review).values():
            if review.place_id == self.id:
                review_list.append(review)
        return review_list
    
    
    
