from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String


Base = declarative_base()

engine = create_engine('sqlite:///words.db')

Session = sessionmaker(bind=engine)

session = Session()


class User(Base):

    __tablename__ = "user"
    id = Column(Integer(), primary_key=True)
    username = Column(String())



class Game(Base):

    __tablename__ = "game"
    id = Column(Integer(), primary_key=True)
    word = Column(String())


