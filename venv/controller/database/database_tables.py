import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Weather(Base):
    __tablename__ = 'weather'
    id = Column(Integer, primary_key=True, autoincrement=True)
    temperature = Column(Integer, nullable=False)
    """status = Column(Integer, nullable=False)
    humidity = Column(Integer, nullable=False)
    wind = Column(Integer, nullable=False)
    date = Column(Date, nullable=False)"""
    location_id = Column(Integer, ForeignKey('location.id'))


class Clothes(Base):
    __tablename__ = 'clothes'
    id = Column(Integer, primary_key=True, autoincrement=True)
    """clothing_type_id = Column(Integer, nullable=False)
    color = Column(Integer, nullable=False)
    brand = Column(Integer, nullable=False)
    clothing_name = Column(Integer, nullable=True)
    picture = Column(String(8), nullable=False)"""

class User(Base):
	__tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(Integer, nullable=False)
    password = Column(String(20), nullable=False)
    gender = Column(Bit(2), nullable=False)
    location_id = Column(Integer, ForeignKey('location.id'))

class Location(Base):
	__tablename__ = 'location'
    id = Column(Integer, primary_key=True, autoincrement=True)
    location_name =  Column(String(20), nullable=False)

class User_Clothes_Joiner(Base):
	__tablename__ = 'user_clothes_joiner'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    clothing_id = Column(Integer, ForeignKey('clothing.id'))

class History(Base):
	__tablename__ = 'history'
	id = Column(Integer, primary_key=True, autoincrement=True)
	user_id = Column(Integer, ForeignKey(user.id)) #i feel like this is off; i already have a user_id in the class above
	preference = Column(Boolean, nullable=True)

	"""docstring for User"""
	def __init__(self, arg):
		super(User, self).__init__()
		self.arg = arg


# Create an engine that stores data in the local directory's
# sqlalchemy_example.db file.
engine = create_engine('sqlite:///sqlalchemy_example.db')

# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
Base.metadata.create_all(engine)