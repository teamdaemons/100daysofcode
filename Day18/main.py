from turtle import Turtle, Screen
import random
tim = Turtle()

screen = Screen()
tim.shape("turtle")
tim.color("red")


def square():
    # Draw a square
    for _ in range(4):
        tim.forward(100)
        tim.right(90)


# square()


def dotted_line():
    # tim.right(90)
    for _ in range(50):
        tim.forward(2)
        tim.penup()
        tim.forward(2)
        tim.pendown()


colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
           "SeaGreen"]


def draw_shape(side):
    angle = 360 / side
    for _ in range(side):
        tim.right(angle)
        tim.forward(100)

side = 3
for i in range(8):
    draw_shape(side)
    side += 1
    tim.color(random.choice(colours))

# dotted_line()

# tim.right(90)

screen.exitonclick()
