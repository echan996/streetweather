#from database_tables as db import Base, Weather, Clothes, User, Location, User_Clothes_Joiner, History
import database_tables as db
import requests
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, create_session
Session  = sessionmaker(bind = db.engine, autoflush=False)
session = Session()
weather_key = "b1b15e88fa797225412429c1c50c122a1"
update_weather()
print len(session.query(db.Location).all())

def sample_get_location():
	return session.query(db.Location).first().location_name
	
def update_weather():
	tuple_query = session.query(db.Location).all()
	for tuple in tuple_query:
		kv_params = {'appid': weather_key, 'q': tuple.location_name}
		r = request.get("http://api.openweathermap.org/data/2.5/weather", params=kv_params)
		print r.url
		print r.text