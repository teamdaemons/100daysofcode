from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def turn_left():
    # tim.left(10)
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)


def turn_right():
    # tim.right(10)
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear, "c")
screen.onkey(move_backwards, "s")
screen.onkey(move_forwards, "w")
screen.exitonclick()
