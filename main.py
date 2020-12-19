import random
from replit import clear

print("Hello to Casino Cards Game Simplifer \n")

def card_deal():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def scores(card_score):
  if 11 in card_score and sum(card_score):
    card_score.remove(11)
    card_score.append(1)
  return sum(card_score)


def play_game():
  is_gameover = False
  should_continue = False
  user_cards = []
  computer_cards = []
  for _ in range(2):
    user_cards.append(card_deal())
    computer_cards.append(card_deal())

