import random
from replit import clear
from art import logo

print("Hello to Cards Game Simplifer \n")

def card_deal():
  """ Returns a random card from the deck """
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def scores(card_score):
  """ Calculates the scores of both players"""
  if 11 in card_score and sum(card_score):
    card_score.remove(11)
    card_score.append(1)
  return sum(card_score)

def compare_cards(user_scores, computer_scores):
  """ Compares the user's and computer's scores to determine the winner"""
  if user_scores == computer_scores:
    return "Draw 🙃"
  elif computer_scores == 0:
    return "Lose, opponent has Blackjack 😱"
  elif user_scores == 0:
    return "Win with a Blackjack 😎"
  elif user_scores > 21:
    return "You went over. You lose 😭"
  elif computer_scores > 21:
    return "Opponent went over. You win 😁"
  elif user_scores > computer_scores :
    return "You win 😃"  
  elif computer_scores > 21 and user_scores > 21:
    return "You went over. You lose 😤"
  else:
    return "You lose 😤"    

def play_game():
  """ Encompasses all the game functions in one simple place"""

  print(logo)

  is_gameover = False
  
  user_cards = []
  computer_cards = []

  for _ in range(2):
    user_cards.append(card_deal())
    computer_cards.append(card_deal())

  while not is_gameover:
    user_score = scores(user_cards)
    computer_score = scores(computer_cards)
    print(f"Your cards are {user_cards} and score {user_score}")
    print(f"Computer's first card is {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score >21:
      is_gameover = True
    else:
      user_answer = input("If you want to draw another card press 'y' or 'n' to pass \n").lower()
      if user_answer == "y":
        user_cards.append(card_deal())
      else: 
        is_gameover = True

  while computer_score != 0 and computer_score <17:
    computer_cards.append(card_deal())
    computer_score = scores(computer_cards)

  print(f"\nYour final cards are{user_cards} and your score is {user_score} \n")
  print(f"\nComputer final cards are{computer_cards}, and final score is {computer_score}\n")
  print(compare_cards(user_score, computer_score))

while input("\nWould you like to start? 'yes' to play \n").lower() == "yes":
  clear()
  play_game()

