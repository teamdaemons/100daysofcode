print("Welcome to Pizza Deliveries")
size = input("What size of pizza do you want S, M or L ")
add_pepperoni = input("Do you want to add pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

price = 0;
if size == "S":
  price =15
  if add_pepperoni == "Y":
    price+=2
  if extra_cheese == "Y":
    price+=1
elif size=="M":
  price =20
  if add_pepperoni == "Y":
    price+=3
  if extra_cheese == "Y":
    price+=1
elif size=="L":
  price=25
  if add_pepperoni == "Y":
    price+=3
  if extra_cheese == "Y":
    price+=1
  print(f"Your total bill is {price}")
else:
  print("Not valid")