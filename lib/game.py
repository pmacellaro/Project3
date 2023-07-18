# word_list = ["Amount","Argument","Art","Be","Beautiful","Belief","Cause","Certain","Chance","Change","Clear","Common","Comparison","Condition","Connection","Copy","Decision","Degree","Desire","Development","Different","Do","Education","End","Event","Examples","Existence","Experience","Fact","Fear","Feeling","Fiction","Force","Form","Free","General","Get","Give","Good","Government","Happy","Have","History","Idea","Important","Interest","Knowledge","Law","Let","Level","Living","Love","Make","Material","Measure","Mind","Motion","Name","Nation","Natural","Necessary","Normal","Number","Observation","Opposite","Order","Organization","Part","Place","Pleasure","Possible","Power","Probable","Property","Purpose","Quality","Question","Reason","Relation","Representative","Respect","Responsible","Right","Same","Say","Science","See","Seem","Sense","Sign","Simple","Society","Sort","Special","Substance","Thing","Thought","True","Use","Way","Wise","Word","Work"]

from sqlalchemy import Column, Integer, String
if 'lib' in __name__ :
    from lib.models import Base, session
else:
    from models import Base, session
from sqlalchemy.orm import relationship


class Game(Base):
    __tablename__ = "game"
    id = Column(Integer(), primary_key=True)
    word = Column(String())


def insert_words(file_path):
    with open('words.txt', 'r') as file:
        text = file.read

    words = text.split()
    for word in words:
        new_word = Game(word=word)
        session.add(new_word)
    session.commit()

    session.close()
