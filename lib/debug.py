import ipdb
from models import session, Game, User

def insert_words(file_path):    
    with open(file_path, 'r') as file:
        text = file.read()

    words = text.split()
    for word in words:
        new_word = Game(word=word)
        session.add(new_word)
    session.commit()
    session.close()



def insert_username():
    username = input('Enter Username Here!')

    new_user = User(username=username)
    session.add(new_user)
    session.commit()
    session.close()
   


ipdb.set_trace()