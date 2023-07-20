from models import session, Game, User, User_Game
import random
import time

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
        # session.close()
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
    current_word = random_row.word.lower()

    # generate a blank space for each letter in the word
    word_blanks = "_" * len(current_word)

    # ---START TIME HERE---
    start_time = time.time()

    # ---GRAPHICS ON LOAD---
    print('')
    print('WELCOME TO HANGMAN')
    print("")
    start_man = [
        """
_______________
|/            |
|              
|            
|             
|            
|
|
        """
    ]

    print(start_man[0])
    print(word_blanks)


    # Keep track of the guesses + wrong guesses
    guessed = False
    wrong_guesses = 0
    guessed_letters = []
    guessed_words = []
    score = 7

    # ---GAMEPLAY---
    # while you have less than 7 wrong guesses, keep asking for a guess
    while not guessed and wrong_guesses < 7:
        guess = input('Letter Guess: ').lower()

        # if the guess is 1 letter long:
        if len(guess) == 1 and guess.isalpha():
            # if the guessed letter is already in the guessed_letters list, say that letter was already guessed.
            if guess in guessed_letters:
                    print(f'You already guessed {guess}. Try again.')
            # if the gussed letter has not already been guessed (is not in the guessed_letters list), and is not in the word, add 1 to the wrong guesses, subtract one from the score, and add the guess to the guessed_letters list.
            elif guess not in current_word:
                print(f'Sorry, {guess} is not in the word.')
                wrong_guesses += 1
                score -= 1
                guessed_letters.append(guess)
            # else (if the letter hasn't been guessed and it's in the word), add the letter to the guessed_letters list, turn the word blanks into a list, checking each letter in the word, match with word blanks. If the letter was guessed, it changes the corresponding word blank into that letter. 
            else:
                guessed_letters.append(guess)
                word_as_list = list(word_blanks)
                indices = [i for i, letter in enumerate(current_word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                    word_blanks = "".join(word_as_list)
                # if there are no more word blanks, that means the word was guessed and player wins
                if "_" not in word_blanks:
                    guessed = True
    
        # ---FOR GUESSING THE WHOLE WORD INSTEAD OF JUST A LETTER---
        # if the length of the guess is the length of the current word:
        elif len(guess) == len(current_word) and guess.isalpha():
            # if you already guessed that wrong word:
            if guess in guessed_words:
                print(f'You already guessed the word {guess}')
            # if you guess the word wrong
            elif guess != current_word:
                print(guess, "WRONG!")
                wrong_guesses += 1
                score -= 1
                guessed_words.append(guess)
            # if you guess the word right, guessed changes to true and the player wins
            else:
                guessed = True
                word_blanks = current_word
        # incase the guess is not a letter (.isalpha()).
        else:
            print("That isn't a LETTER")

        # ---WHAT THE USER SEES WHILE PLAYING---
        print(guessed_letters)
        print(hangman(wrong_guesses))
        print(word_blanks)
        print("\n")

    # if you win:
    if guessed:
        print("    \    |   /")
        print(" --- You Win! ---")
        print("    /    |   \\")
        print("")
        print("COME GET A SMOOCH")
        print("")
        print(f'Your score: {score}/7')

        # --END TIME HERE--
        end_time = time.time()

    # if you loose:
    else:
        if wrong_guesses == 7 or score <= 0:
            print("You Lose :'( ")
            print(f'The word was {random_row.word}')
            print(f'Your score: {score}/7')

            # --END TIME HERE--
            end_time = time.time()
            
    
    game_time = round((end_time - start_time), 1)
    
    if user:
        leaderboard = User_Game(user_id = user.id, game_id = random_row.id, time = game_time, score = score)
        session.add(leaderboard)

    else:
        leaderboard = User_Game(user_id = new_user.id, game_id = random_row.id, time = game_time, score = score)
        session.add(leaderboard)
        
    session.commit()
    session.close()

    print(f'User: {username}   Game: "{current_word}"   Time: {game_time}seconds   Score: {score}')
    


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

play()