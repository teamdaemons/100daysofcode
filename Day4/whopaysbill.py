import random

test_seed = int(input("Enter the seed number"))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#print(names)
#print(names[0])
length = len(names)
member_to_pay = random.randint(0,length)
print(names[member_to_pay-1] + " is going to pay the bill today") #starts from 0 to max len -1 is the max

