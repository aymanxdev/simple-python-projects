from art import logo 
import random
from replit import clear
print("Welcome to Number Guessing Game!")

hard_level = 5
easy_level = 10

def set_difficulty():
  """This function returns the number of attempts """
  level = input("Choose your difficulty level 'easy or hard? ")
  if level == "easy":
   return easy_level
  else: 
    return hard_level

def check_answer(guess, answer, turns):
  """This function takes the generated answer, user's guess and reduce the number of turns """
  if guess > answer:
    print("Too high")
    return turns -1 
  elif guess < answer:
    print("Too low")
    return turns -1
  else:
    print(f"Wow, you got it! The answer is indeed {answer} and your remaining attempts are {turns}")


def game():
  auto_answer = random.randint(1, 100)

  print(logo)
  print(auto_answer)
  turns = set_difficulty()

#Repeat the guessing functionality if they get it wrong.
  user_guess = 0
  while user_guess != auto_answer:
    print(f"You have {turns} attempts remaining to guess the number.")

    user_guess = int(input("Make a guess?"))
    #Track the number of turns and reduce by 1 if they get it wrong.
    turns = check_answer(user_guess,auto_answer,turns)
    if turns == 0:
      print("You have ran out of Guesses, play again!")
      return
    elif user_guess != auto_answer:
      print("Guess again")


  


while input("\n Would you like to play a Guessing Game? 'Yes' or 'No' to exit.\n").lower() == "yes":
  clear()
  game()