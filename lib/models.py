from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String


Base = declarative_base()

engine = create_engine('sqlite:///words.db')

Session = sessionmaker(bind=engine)

session = Session()