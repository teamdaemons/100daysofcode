#1. Create a greeting for your program.
print("Welcome to the tip calculator. $")
#2. Ask the user for the total bill.
total=float(input("What was the total bill"))
#3. Ask the user for number of people and percentage split of the tip.
people=int(input("How many people to split the bill? "))
percentage=int(input("What percentage tip would you like to give? 10, 12, or 15 "))
percentagetip = float((total*12)/(100*5));
bill = str((total/people)+percentagetip)
#4. Print the value each should pay
print(percentagetip)
print("Each person should pay: $"+bill)