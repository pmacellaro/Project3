import ipdb
from models import session, Game, User, User_Game
import random

def insert_words(file_path):    
    with open(file_path, 'r') as file:
        text = file.read()

    words = text.split()
    for word in words:
        new_word = Game(word=word)
        session.add(new_word)
    session.commit()
    session.close()



# def insert_username():
    # username = input('Enter Username Here!')

    # new_user = User(username=username)
    # session.add(new_user)
    # session.commit()
    # session.close()

def play():
    username = input('Enter Username Here!')

    new_user = User(username=username)
    session.add(new_user)
    session.commit()
    session.close()
    print(f'Hello, {username}, would you like to play a game?')
    
    query = session.query(Game)
    count = query.count()

    if count == 0:
         return None  # Handle the case where the table is empty

    random_offset = random.randint(0, count - 1)
    random_row = query.offset(random_offset).first()
    word_blanks = " _ " * len(random_row.word)

    print(f"Random Row ID: {random_row.id}, Name: {random_row.word}")
    print(word_blanks)


    # return random_row
    

ipdb.set_trace()