from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import Column, Integer, String, MetaData, ForeignKey


convention = {
	'fk': 'fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s'
	}


md = MetaData( naming_convention = convention)


Base = declarative_base(metadata = md)

engine = create_engine('sqlite:///words.db')

Session = sessionmaker(bind=engine)

session = Session()


class User(Base):

    __tablename__ = "user"
    id = Column(Integer(), primary_key=True)
    username = Column(String())

    user_games = relationship('User_Game', back_populates= "user")



class Game(Base):

    __tablename__ = "game"
    id = Column(Integer(), primary_key=True)
    word = Column(String())

    user_games = relationship('User_Game', back_populates= "game")
    def __repr__(self):
        return f'<Game {self.word} >'



class User_Game(Base):
    __tablename__ = "user_games"
    id = Column(Integer(), primary_key=True)
    user_id = Column(Integer(), ForeignKey('user.id'))
    game_id = Column(Integer(), ForeignKey('game.id'))
    start_time = Column(Integer())
    end_time = Column(Integer())
    score = Column(Integer())

    user = relationship('User', back_populates = "user_games")
    game = relationship('Game', back_populates = "user_games")


