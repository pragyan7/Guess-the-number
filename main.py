import random
import sys
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
def check_guess(user_guess, the_number, turns):
  '''Checks the answer against the guess. Returns the no. of turns remaining'''
  if user_guess > the_number:
    print("Too high ⏫")
    # Track the number of turns remaining.
    return turns - 1
  elif user_guess < the_number:
    print("Too low ⏬")
    return turns - 1
  else:
    # If they got the answer correct, show the actual answer to the player.
    print(f".................................\n  You got it! The answer is {the_number}!\n  You win! 🤩\n.................................")

def set_difficulty():
  '''Sets the difficulty level of the game'''
  game_level = input("Choose a difficulty level: Type 'easy' or 'hard': ")
  if game_level == "easy":
    return EASY_LEVEL_TURNS
  elif game_level == "hard":
    return HARD_LEVEL_TURNS
  else:
    print("Please provide a valid input")
    sys.exit()

def guessing_game():
  print(logo)
  print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 to 100.")
  # Choosing a random number between 1 and 100.
  the_number = random.randint(1, 100)
  turns = set_difficulty()
  # Repeat the guessing functionality if the user gets it wrong.
  user_guess = 0
  while user_guess != the_number:
    print(f"You have {turns} attempts to guess the number 💭")
    # Let the user guess a number
    user_guess = int(input("Make a guess: "))
    # Track the number of turns and reduce by 1 if they get it wrong.
    turns = check_guess(user_guess, the_number, turns)
    if turns == 0:
      print(f"........................................\n  You've run out of guesses, you lose.  \n  The answer was {the_number}! 😭                \n........................................")
      return
    elif user_guess != the_number:
      print("Guess again 🙄\n------------------------------------------")  
     
guessing_game()
