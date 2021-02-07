from turtle import Turtle
import random


class States():

    def create_state(self, name, x, y):
        new_state = Turtle()
        new_state.hideturtle()
        new_state.penup()
        new_state.goto(x, y)
        #new_state.pendown()
        new_state.write(name, move=True, font=("Arial", 10, "normal"))
        new_state.shapesize(stretch_wid=1, stretch_len=2)


