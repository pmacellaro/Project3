from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String


Base = declarative_base()

engine = create_engine('sqlite:///words.db')

Session = sessionmaker(bind=engine)

session = Session()

class Word(Base):

    __tablename__ = "words"
    id = Column(Integer(), primary_key=True)
    text = Column(String())
    