#!/usr/bin/python3
""" State Module for HBNB project """
import os
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.city import City
from models import st_type


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(
        String(128), nullable=False
    ) if st_type == 'db' else ''
    if st_type == 'db':
        cities = relationship(
            'City',
            cascade='all, delete, delete-orphan',
            back_populates='state'
        )

    else:
        @property
        def cities(self):
            """Returns the cities in this State"""
            from models import storage
            cities_in_state = []
            for value in storage.all(City).values():
                if value.state_id == self.id:
                    cities_in_state.append(value)
            return cities_in_state
