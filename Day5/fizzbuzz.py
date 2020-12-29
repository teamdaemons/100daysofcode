#if number is divisible by 3 fizz
#if its divisible by 5 then buzz  and so on

for number in range(1,101):
  if number % 3==0 and number % 5 ==0:
    print("FizzBuzz")
  elif number % 3==0:
    print("Fizz")
  elif number % 5==0:
    print("Buzz")
  else:
    print(number)