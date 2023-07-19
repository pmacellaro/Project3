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



def play():
    # ---START OF GAME: GET USERNAME---
    username = input('Enter Username Here: ')
    user = session.query(User).filter_by(username=username).first()

    # If user already exists in the User model, say welcome back
    if user:
        print(f'Welcome back, {username}!')

    # If user doesn't already exist, create a new user and add to the User model. Say hello to new user.
    else:
        new_user = User(username=username)
        session.add(new_user)
        session.commit()
        session.close()
        print(f'Hello, {username}, would you like to play a game?')
    
    # ---GETTING A RANDOM WORD FROM THE GAME MODEL---
    query = session.query(Game)
    count = query.count()

    # Handle the case where the table is empty
    if count == 0:
         return None  

    # pick a random row between the first and last indices, inclusive
    random_offset = random.randint(0, count - 1)
    random_row = query.offset(random_offset).first()

    # generate a blank space for each letter in the word
    word_blanks = " _ " * len(random_row.word)

    print(f"Random Row ID: {random_row.id}, Name: {random_row.word}")
    print(word_blanks)


    # return random_row
    

ipdb.set_trace()