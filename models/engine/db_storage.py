#!/usr/bin/python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv as env
from models.base_model import Base
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class DBStorage:
    """ Database Storage class """
    __engine = None
    __session = None

    def __init__(self):
        """ To Initialize another Storage Instance """
        user = env('HBNB_MYSQL_USER')
        passwd = env('HBNB_MYSQL_PWD')
        host = env('HBNB_MYSQL_HOST')
        db = env('HBNB_MYSQL_DB')
        data = 'mysql+mysqldb://{}:{}@{}:i/{}'\
        .format(user, passwd, host, db)
        self.__engine = create_engine(data, pool_pre_ping=True)

        if env('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = Session()

    def all(self, cls=None):
        """show all databases objects """
        dct = {}
        if cls is None:
            for c in classes.values():
                objs = self.__session.query(c).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    dct[key] = obj
        else:
            objs = self.__session.query(cls).all()
            for obj in objs:
                key = obj.__class__.__name__ + '.' + obj.id
                dct[key] = obj
        return dct

    def new(self, obj):
        """Create new object """
        self.__session.add(obj)

    def save(self):
        """To save a new object """
        self.__session.commit()

    def delete(self, obj=None):
        """To delete object"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """ To create all tables in the database """
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(bind=self.__engine, expire_on_commit=False))

    def close(self):
        """To close all the working session """
        self.session.close()

