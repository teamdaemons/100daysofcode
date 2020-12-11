height = int(input("Enter your height in cm "))
bill=0
if height>120:
  age = int(input("Enter your age in years"))
  if age <12:
    print("You will need to pay $5")
  elif age <=18:
    bill=7
    print(f"please pay {bill}.")
  elif age >= 45 and age <=55:
    bill=0
    print("Everything is going to be ok. Have a free ride on us!")
  else:
    bill=12
    print(f"please pay {bill}.")
  
  wants_photo= input("Do you want photo? ")
  if wants_photo== "Y":
    bill+=3
  
  print(bill)
else:
  print("Sorry you are not eligible.")