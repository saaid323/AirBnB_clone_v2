#!/usr/bin/python3
"""This module defines a class to manage database storage for hbnb clone"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import urllib.parse
from models.base_model import BaseModel, Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models import st_type


class DBStorage:
    """manages storage of hbnb models in a SQL database"""
    __engine = None
    __session = None

    def __init__(self):
        """Initializes the SQL database storage"""
        user = os.getenv('HBNB_MYSQL_USER')
        pwd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db_name = os.getenv('HBNB_MYSQL_DB')
        env = os.getenv('HBNB_ENV')
        DB_URL = "mysql+mysqldb://{}:{}@{}:3306/{}".format(
            user, pwd, host, db_name)
        self.__engine = create_engine(DB_URL, pool_pre_ping=True)
        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        objects = dict()
        all_classes = (User, State, City, Amenity, Place, Review)
        if cls is None:
            for class_type in all_classes:
                query = self.__session.query(class_type)
                for obj in query.all():
                    obj_key = '{}.{}'.format(obj.__class__.__name__, obj.id)
                    objects[obj_key] = obj
        else:
            query = self.__session.query(cls)
            for obj in query.all():
                obj_key = '{}.{}'.format(obj.__class__.__name__, obj.id)
                objects[obj_key] = obj
        return objects

    def delete(self, obj=None):
        """Removes an object from the storage database"""
        if obj:
            self.__session.delete(obj)

    def new(self, obj):
        """Adds new object to storage database"""
        if obj is not None:
            try:
                self.__session.add(obj)
                self.__session.flush()
                self.__session.refresh(obj)
            except Exception as ex:
                self.__session.rollback()
                raise ex

    def save(self):
        """Commits the session changes to database"""
        self.__session.commit()

    def reload(self):
        """Loads storage database"""
        Base.metadata.create_all(self.__engine)
        SessionFactory = sessionmaker(
            bind=self.__engine,
            expire_on_commit=False
        )
        self.__session = scoped_session(SessionFactory)()

    def close(self):
        """calls close() method"""
        self.__session.close()
