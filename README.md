# Hangman

## Description

This cli program was designed for users to play hangman! The game starts by asking the player to enter a name. If the name is not already in our database, we send a hello message asking if the new player would like to play a game. If the player is already in our database, we send a welcome back message to the player. Once the game starts, the player will see the empty hangman stand along with a number of empty dashes that correspond to the number of letters in the word. The player is allowed 7 wrong guesses before they lose the game and with each wrong guess, a piece of the man is added to the hangman stand. Our program keeps track of the player, the game, the time it took the player to complete the game, as well as their score. The score is determined by how many wrong guesses the player makes. The score starts at 7 and one point is subtracted with each incorrect guess. If the player guesses the word without guessing any wrong letters, they'll recieve a 7 out of 7. Once the game is complete, the command line will display one of two things, depending on if the player won or lost. If the player won, the command line will display a fun little "you win" message along with their leaderboard score for that game including their name, the word, the time in seconds it took them to complete the game, and their score. If the player looses, the command line will display a "you lose" message along with the correct word, followed by their leaderboard score for that game.

We hope you enjoy!

## Instructions

To run this program, you'll first have to fork and clone this repository onto your own computer. Once this is done, you'll need to enter <code>pipenv install</code> followed by <code>pipenv shell</code>. Once this is done, you'll need to 'cd' into the lib folder, then run the cli.py file. To do this you'll enter <code>cd lib</code>, followed by <code>python cli.py</code>. This should get the game up and running! Once it's up and running the game will ask you to enter a name before proceeding to the gameplay. To play the game again, you just have to enter <code>python cli.py</code>.

## Accompishments

* Getting the empty dashes to turn into correctly guessed letters
* Having the hangman change upon wrong guesses

## Challenges

* Setting up the sqlalchemy databases and connecting them

## Authors
* Alexis Boucouvalas
* Paul Macellaro
