from turtle import Turtle, Screen
import random
tim = Turtle()
tim.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r,g,b)
    return random_color

directions = [0,90,180,270]
tim.speed("fastest")

tim.pensize(15)

for _ in range(200):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))
