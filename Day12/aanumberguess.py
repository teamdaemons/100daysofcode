from art import logo
import random
print(logo)
print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 to 100")
choice=input("Choose a difficulty. Type 'easy' or 'hard': ")

number = random.randint(1,100)
print(number)

def play(count):
  while count!=0:
    print(f"You have {count} attempts remaining to guess the number")
    guess=int(input("Make a guess: "))
    if guess > number:
      print("Too High")
      print("Guess Again")
      count-=1
    elif guess==number:
      print(f"You guess is right Yippie. The answer is {guess}")
      break
    else:
      print("Too Low")
      if count >1:
        print("Guess Again")
      count-=1
  if count==0:
      print("No attempts left, You Lose")

count=0
if choice=='easy':
  count+=10
else:
  count+=5

play(count)