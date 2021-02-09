def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum


print(add(1, 2, 3, 4, 5))

def calculate(n,**kwargs):
    print(type(kwargs)) # dictionary
    n +=kwargs["add"]
    n *=kwargs["multiply"]
    print(n)

calculate(2, add=2, multiply =5)


class Car:
    def __init__(self,**kw):
        self.make = kw.get("make") # kw["make"]
        self.model = kw.get("model") #kw["model"]

my_car = Car(make="Nissan", model ="GT-R" )
print(my_car.make)