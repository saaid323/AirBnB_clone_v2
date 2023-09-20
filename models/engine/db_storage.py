#!/usr/bin/python3
"""DBStorage class"""
from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class CustomDBStorage:
    """Create tables in the environment"""
    __custom_engine = None
    __custom_session = None

    def __init__(self):
        user = getenv("HBNB_MYSQL_USER")
        passwd = getenv("HBNB_MYSQL_PWD")
        db = getenv("HBNB_MYSQL_DB")
        host = getenv("HBNB_MYSQL_HOST")
        env = getenv("HBNB_ENV")

        self.__custom_engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                             .format(user, passwd, host, db),
                                             pool_pre_ping=True)

        if env == "test":
            Base.metadata.drop_all(self.__custom_engine)

    def all(self, cls=None):
        """query on the current database session"""
        custom_dict = {}
        if cls:
            if type(cls) is str:
                cls = eval(cls)
            query = self.__custom_session.query(cls)
            for elem in query:
                key = "{}.{}".format(type(elem).__name__, elem.id)
                custom_dict[key] = elem
        else:
            custom_list = [State, City, User, Place, Review, Amenity]
            for custom_cls in custom_list:
                query = self.__custom_session.query(custom_cls)
                for elem in query:
                    key = "{}.{}".format(type(elem).__name__, elem.id)
                    custom_dict[key] = elem
        return custom_dict

    def new(self, obj):
        """add the object to the current database session"""
        self.__custom_session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__custom_session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj:
            self.__custom_session.delete(obj)

    def reload(self):
        """create all tables in the database """
        Base.metadata.create_all(self.__custom_engine)
        custom_session_maker = sessionmaker(bind=self.__custom_engine,
                                            expire_on_commit=False)
        CustomSession = scoped_session(custom_session_maker)
        self.__custom_session = CustomSession()
