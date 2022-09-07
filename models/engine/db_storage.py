#!/usr/bin/python3
from models.base_model import Base
from models.user import User
from models.state import State
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.city import City
from sqlalchemy import (create_engine)
from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session

class DBStorage():
    """Class DBStorage"""
    __engine = None
    __session = None

    def __init__(self):
        """Public instance methods"""
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}"
                                      .format(getenv("HBNB_MYSQL_USER"),
                                              getenv("HBNB_MYSQL_PWD"),
                                              getenv("HBNB_MYSQL_HOST"),
                                              getenv("HBNB_MYSQL_DB")), 
                                      pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """The following values must be retrieved via environment variables"""
        classes = [User, State, Place, Amenity, Review, City]
        my_dict = {}

        if cls in classes:
            search = self.__session.query(cls)
            for object in search:
                key = (f"{object.__class__.__name__}.{object.id}")
                my_dict[key] = object
        
        elif cls is None:
            for class_ in classes:
                search = self.__session.query(class_)
                for object in search:
                    key = "{}.{}".format(type(object).__name__,
                               object.id)
                    my_dict[key] = object
        return my_dict

    def new(self, obj):
        """Add the object to the current database session"""
        self.__session.add(obj)
    
    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """
        Delete from the current database
        session obj if not None
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the databas"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                  expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
    
    def close(self):
        """Close the session"""
        self.__session.close()
