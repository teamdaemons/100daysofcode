from art import auction
from replit import clear
#HINT: You can call clear() to clear the output in the console.
print(auction)
auctiondictionary = {}
name=input("What is your name?:")
bid=int(input("What is your bid?:"))
auctiondictionary[name]=bid
bidders =input("Are there any other bidders? Type 'yes' or 'no': ")

while bidders=="yes":
  clear()
  name=input("What is your name?:")
  bid=int(input("What is your bid?:"))
  auctiondictionary[name]=bid
  bidders =input("Are there any other bidders? Type 'yes' or 'no': ")
else:
  print(auctiondictionary)
  win_bid=0
  winner =""
  for key in auctiondictionary:
    if auctiondictionary[key] >win_bid:
      win_bid = auctiondictionary[key]
      winner = key
  print(f"Winner is {winner} and winning bid is $ {win_bid}")