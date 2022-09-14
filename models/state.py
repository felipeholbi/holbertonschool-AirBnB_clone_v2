#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
from os import getenv


class State(BaseModel, Base if(
        getenv("HBNB_TYPE_STORAGE") == "db") else object):
    """ State class """
    if getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", cascade="delete")
    else:
        name = ""

    @property
    def cities(self):
        """
        returns the list of City instances with
        state_id equals to the current State.id
        """
        from models import storage
        new_list = []
        cities = storage.all(City).values()
        for city in cities:
            if self.id == city.state_id:
                new_list.append(city)
        return(new_list)
