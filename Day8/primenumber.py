#Write your code below this line 👇

def prime_checker(number):
  # prime number is divisible by 1 and itself
  prime=True
  for n in range(2,number):
    count = number%n
    if count==0:
      prime=False
  if prime==False:
    print(f"The number {number} is Not Prime")
  else:
    print(f"The number {number} is Prime")



#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)



