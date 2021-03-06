from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(150, 250)
        self.hideturtle()
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.goto(150, 250)
        self.update_scoreboard()

    def increase_score2(self):
        self.score += 1
        self.clear()
        self.goto(-150, 250)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score = {self.score} ", False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", False, align=ALIGNMENT, font=FONT)