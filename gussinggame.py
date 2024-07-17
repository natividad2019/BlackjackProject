# Allow the player to submit a guess for a number between 1 and 100
# Check users guess against actaul answer. Print "Too high" or "Too low" depending on the users answer.
# if they got the answer correct, show the actual answer to the player.
# track the number of turns remaining.
# if they run out of turns, provide feedback to the player.
#Include two different difficulty levels (e.g. 10 guesses in easy mode, only 5 guesses in hard mode).

from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5
turns = 0

# function to check users guess aganist actual answer:
def check_answer(guess, answer, turns):
  """ This function checks the users guess against the actual answer.
  It returns the number of remaining turns
  """
  if guess > answer:
    print("Too high") # if the guess is too high, inform the user


    return turns - 1
    # print(f"You have {turns} attempts remaining to guess the number.")
  elif guess < answer:
    print("Too low") # If the guess us too low, inform the user 
   
    return turns - 1
    # print(f"You have {turns} attempts remaining to guess the number.")
  else:
    print(f"You got it! The answer was {answer}") # if the guess is correct, congratulate the user. 
    return turns # No need to reduce turns since the game is won


# make a function to set difficulty
# function to set the diffictulty 
def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ") # Ask the user to choose a difficulty level.
  if level == "easy": 
    return EASY_LEVEL_TURNS # Return the number of turns for easy level
  else:
    return HARD_LEVEL_TURNS # Return the number if turns for hard level
 

def game():
   
# Choosing a random number between 1 and 100

  print("Welcome to the number guessing game!") # Welcome message

  print("I am thinking of a number between 1 and 100.") # inform the user about the game 


  answer = randint(1, 100) # generate a random number between 1 and 100
  print(f"Pssst, the correct answer is {answer}") # print the corrent answer for debuggging purposes (remove this is in the actaul game)

  turns = set_difficulty() # set the difficulty level and get the number of turns 
  # print(f"You have {turns} attempts remaining to guess the number.")

  guess = 0 # initialize the guess variable
  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number.") # Inform the user about the remaining attempts

# let the user guses the number 
    guess = int(input("Make a guess: ")) # Ask the user to make a guess and update the number of turns

    turns = check_answer(guess, answer, turns) # check the guess game and update the number of turns
    if turns == 0:
      print("You've run out of guesses, you lose.") # if the user runs out of turns, they lose the game 
      return # End the game
    elif guess != answer:

      print("Guess again.") # if the guess is incorrect , prompt the user to guess again

game() # start the game by calling the game function



