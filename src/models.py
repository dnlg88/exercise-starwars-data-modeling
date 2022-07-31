import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Float, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'User'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    username = Column(String, primary_key=True)
    password = Column(String(250), nullable=False)

class Planet(Base):
    __tablename__= 'Planet'
    uid = Column(Integer, primary_key=True)
    diameter = Column(Integer, nullable=False)
    rotation_period = Column(Integer, nullable=False)
    orbital_period = Column(Integer, nullable=False)
    gravity = Column(String, nullable=False)
    population = Column(Integer, nullable=False)
    climate = Column(String, nullable=False)
    terrain = Column(String, nullable=False)
    surface_water = Column(Integer, nullable=False)
    created = Column(Date, nullable=False)
    edited = Column(Date, nullable=False)
    name = Column(String, nullable=False)
    url = Column(String, nullable=False)

class Character(Base):
    __tablename__= 'Character'
    uid = Column(Integer, nullable=False, primary_key=True)
    height = Column(Float, nullable=False)
    mass = Column(Float, nullable=False)
    hair_color = Column(String, nullable=False)
    skin_color = Column(String, nullable=False)
    eye_color = Column(String, nullable=False)
    birth_year = Column(Integer, nullable=False)
    gender = Column(String, nullable=False)
    created = Column(Date, nullable=False)
    edited = Column(Date, nullable=False)
    name = Column(String, nullable=False)
    homeworld_id = Column(Integer, ForeignKey('Planet.uid'))
    url = Column(String, nullable=False)

class Vehicle(Base):
    __tablename__= 'Vehicle'
    uid = Column(Integer, nullable=False, primary_key=True)
    model = Column(String, nullable=False)
    vehicle_class = Column(String, nullable=False)
    manufacturer = Column(String, nullable=False)
    skin_color = Column(String, nullable=False)
    cost_in_credits = Column(Integer, nullable=False)
    length = Column(Float, nullable=False)
    crew = Column(Integer, nullable=False)
    passengers = Column(Integer, nullable=False)
    max_atmosephering_speed = Column(Integer, nullable=False)
    cargo_capacity = Column(Integer, nullable=False)
    consumables = Column(String, nullable=False)
    films = Column(String, nullable=False)
    pilots = Column(String, nullable=False)
    created = Column(Date, nullable=False)
    edited = Column(Date, nullable=False)
    name = Column(String, nullable=False)
    url =Column(String, nullable=False)

class CharacterFavorites(Base):
    __tablename__ = 'CharacterFavorites'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    username = Column(String, ForeignKey('User.username'), primary_key=True)
    character_uid = Column(Integer, ForeignKey('Character.uid'))
    name = Column(String, ForeignKey('Character.name'))

class PlanetFavorites(Base):
    __tablename__ = 'PlanetFavorites'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    username = Column(String, ForeignKey('User.username'), primary_key=True)
    planet_uid = Column(Integer, ForeignKey('Planet.uid'))
    name = Column(String, ForeignKey('Planet.name'))

class VehicleFavorites(Base):
    __tablename__ = 'VehicleFavorites'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    username = Column(String, ForeignKey('User.username'), primary_key=True)
    vehicle_uid = Column(Integer, ForeignKey('Vehicle.uid'))
    name = Column(String, ForeignKey('Vehicle.name'))    
    
    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')