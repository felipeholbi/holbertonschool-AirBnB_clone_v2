#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City

class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable = False)
    cities = relationship("City", 
                          backref="State",
                          cascade="all, delete-orphan")

    @property
    def cities(self):
        """ returns the list of City instances with 
        state_id equals to the current State.id"""
        from models import storage
        new_list = []
        cities = storage.all(City)

        for city in cities.values():
            if city.state_id == self.id:
                new_list.append(city)
        return new_list
