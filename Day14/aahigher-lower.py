from art import logo,vs
from game_data import data
import random
from replit import clear


count=0
f=random.sample(data,2)
option1 = f[0]
option2 = f[1]
answer=1
score=0

def get_next_choice():
    x=random.sample(data,1)
    option2 = x[0]
    return option2
print(logo)
while answer!=0:
  print(f"Compare A: {option1['name']}, {option1['description']},{option1['country']}")
  print(vs)
  print(f"Compare B: {option2['name']}, {option2['description']},{option2['country']}")
  choice = input("Who has more followers? Type 'A' or 'B': ").upper
  if choice=="A":
    if option1['follower_count']>option2['follower_count']:
      score+=1
      clear()
      print(logo)
      print(f"You are right! Current Score {score}")
      option1.clear()
      option1=option2.copy()
      while option2==option1:
        #option2.clear()
        option2=get_next_choice()
    else:
      print(f"Sorry thats wrong! Final Score{score}")
      answer=0 
  else:
    if option2['follower_count']>option1['follower_count']:
      score+=1
      clear()
      print(f"You are right! Current Score {score}")
      option1.clear()
      option1=option2.copy()
      while option2==option1:
        #option2.clear()
        option2=get_next_choice()
    else:
      print(f"Sorry thats wrong! Final Score{score}")
      answer=0 
#print(f)

