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
    print('')
    user = session.query(User).filter_by(username=username).first()

    # If user already exists in the User model, say welcome back
    if user:
        print(f'Welcome back, {username}!')
        print('')

    # If user doesn't already exist, create a new user and add to the User model. Say hello to new user.
    else:
        new_user = User(username=username)
        session.add(new_user)
        session.commit()
        session.close()
        start_game = input(f'Hello, {username}, would you like to play a game?')
        print('')
    

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
    word_blanks = "_" * len(random_row.word)

    print(word_blanks)

    # Keep track of the guesses + wrong guesses
    guessed = False
    wrong_guesses = 0
    guessed_letters = []
    guessed_words = []
    score = 7


    print('')
    print('WELCOME TO HANGMAN')
    print("")
    # print(hangman(wrong_guesses[0]))
    # Print the hangman base to start
    print('_______________')
    print('|/            |')
    print('|')
    print('|')
    print('|')
    print('|')
    print('|')
    print('|')


    while not guessed and wrong_guesses < 7:
        guess = input('Letter Guess: ')

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                    print(f'You already guessed {guess}. Try again.')
            elif guess not in random_row.word:
                print(f'Sorry, {guess} is not in the word.')
                wrong_guesses += 1
                score -= 1
                guessed_letters.append(guess)
            else:
                guessed_letters.append(guess)
                word_as_list = list(word_blanks)
                indices = [i for i, letter in enumerate(random_row.word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                    word_blanks = "".join(word_as_list)
                if "_" not in word_blanks:
                    guessed = True
        elif len(guess) == len(random_row.word) and guess.isalpha():
            if guess in guessed_words:
                print(f'You already guessed the word {guess}')
            elif guess != random_row.word:
                print(guess, "WRONG!")
                wrong_guesses += 1
                score -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_blanks = random_row.word
        else:
            print("That isn't a LETTER")

        print(hangman(wrong_guesses))
        print(word_blanks)
        print("\n")

    if guessed:
        print("    \    |   /")
        print(" --- You Win! ---")
        print("    /    |   \\")
        print("")
        print("COME GET A SMOOCH")

    else:
        if wrong_guesses == 7 or score <= 0:
            print("You Lose :'( ")
            print(f'the word was {random_row.word}')
            

def hangman(wrong_guesses):
    filled_man = [  
        
    """
    _______________
    |/            |
    |              
    |            
    |             
    |            
    |
    |
    """,
    """
    _______________
    |/            |
    |             O 
    |            
    |             
    |            
    |
    |

    """,
    """
    _______________
    |/            |
    |             O 
    |             |
    |             
    |            
    |
    |
    """,
    """
    _______________
    |/            |
    |             O 
    |            /|
    |            
    |            
    |
    |
    """,
    """
    _______________
    |/            |
    |             O 
    |            /|\\
    |            
    |            
    |
    |
    """,
    """
    _______________
    |/            |
    |             O 
    |            /|\\
    |             |
    |            
    |
    |
    """,
    """
    _______________
    |/            |
    |             O 
    |            /|\\
    |             |
    |            /
    |
    |
    """,
    """
    _______________
    |/            |
    |             O 
    |            /|\\
    |             |
    |            / \\
    |
    |
    """
                

    ]
    return filled_man[wrong_guesses]

            
            

           


    # return random_row
    

ipdb.set_trace()