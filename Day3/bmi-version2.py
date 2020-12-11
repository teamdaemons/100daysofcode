# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

weight_as_int = float(weight)
height_as_float = float(height)

# Using the exponent operator **
bmi = weight_as_int / height_as_float ** 2

print(round(bmi))

if bmi < 18.5:
  print(f"Your bmi is {bmi}, You are underweight")
elif bmi <25:
  print(f"Your bmi is {bmi}, Your are normal weight")
elif bmi <30:
  print(f"Your bmi is {bmi}, Your are overweight")
elif bmi <30:
  print(f"Your bmi is {bmi}, Your are obese weight")
else:
  print(f"Your bmi is {bmi}, You are clinically obese")