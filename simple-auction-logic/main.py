from replit import clear
from art import logo

print(logo)
auc = {}
_continue_ = True

def find_highest(bidding_record):

  highest= 0
  winner= ""

  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest:
      highest = bid_amount
      winner = bidder
  print(f"The highest bidder is {winner} and highest bid is $ {highest}")

while _continue_:
  name = input("What's your name? \n")
  bid = int(input("What is your bid? \n"))
  auc[name] = bid

  result = input("Enter Yes to clear or No to continue \n").lower()
  if result == "Yes" or result == "yes":
    _continue_
    clear()
  elif result == "no" or result == "No":
    _continue_ = False
    find_highest(auc)  
  
