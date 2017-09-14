#from database_tables as db import Base, Weather, Clothes, User, Location, User_Clothes_Joiner, History
import database_tables as db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, create_session
Session  = sessionmaker(bind = db.engine, autoflush=False)
session = Session()

session.add(db.Location(location_name="Londelbomble"))
session.commit()
print session.query(db.Location).first()