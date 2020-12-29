#passwordlist Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Pypasswordlist Generator!")
nr_letters= int(input("How many letters would you like in your passwordlist?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomise d:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

passwordlist = random.choices(letters,k=nr_letters) + random.choices(numbers,k=nr_numbers) + random.choices(symbols,k=nr_symbols)
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P 
print(passwordlist)
random.shuffle(passwordlist)
#list2 = passwordlist
#print(type(list2))
#print(passwordlist)
pass1=""
for n in passwordlist:
  pass1+=n
print(pass1)

#Solution https://repl.it/@appbrewery/password-generator-end#main.py