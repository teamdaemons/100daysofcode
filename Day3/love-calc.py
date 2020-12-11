# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

lower_name = name1.lower()+name2.lower()
#lower_name2 = name2.lower()

true_count = lower_name.count("t")+lower_name.count("r")+lower_name.count("u")+lower_name.count("e")
love_count = lower_name.count("l")+lower_name.count("o")+lower_name.count("v")+lower_name.count("e")
score = int(str(true_count)+ str(love_count))
print(score)

if score <10 or score >90:
  print(f"Your love score is {score}, you go together like coke and mentos.")
elif score >=40 and score <=50:
  print(f"Your love score is {score}, you are alright together.")
else:
  print(f"Your love score is {score}")