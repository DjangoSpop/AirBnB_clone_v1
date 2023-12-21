#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class State(BaseModel, Base):
    """ State class """
    name = ""
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete", backref="state")
    @property
    def cities(self):
        """Getter attribute in case of file storage"""
        from models import storage
        from models.city import City
        city_list = []
        for key, value in storage.all(City).items():
            if value.state_id == self.id:
                city_list.append(value)
        return city_list
        
