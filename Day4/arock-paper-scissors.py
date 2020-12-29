import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
library = [rock,paper,scissors]
#print(library[0])

user_choice= int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
computer_choice=random.randint(0,2)
print(computer_choice)
print(f"Your choice is: {library[user_choice]}  Computer Choice is: {library[computer_choice]} \n")
if (user_choice==0 and computer_choice ==1) or (user_choice==1 and computer_choice ==2) or (user_choice==2 and computer_choice ==0):
  print("You lose")
elif (user_choice==computer_choice):
  print("Its a Draw")
else:
  print("You Win")


