from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)


snake = Snake("cyan")
snake2 = Snake("red")
food = Food()
scoreboard = Scoreboard()
scoreboard2 = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

screen.onkey(snake2.up, "w")
screen.onkey(snake2.down, "s")
screen.onkey(snake2.left, "a")
screen.onkey(snake2.right, "d")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    snake2.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
    if snake2.head.distance(food) < 15:
        food.refresh()
        scoreboard2.increase_score2()

    # Detect collision with wall player 1
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        x = snake.head.xcor()
        y = snake.head.ycor()
        if x > 280:
            snake.segments[0].goto(-280, y)
        elif x < -280:
            snake.segments[0].goto(280, y)
        elif y > 280:
            snake.segments[0].goto(x, -280)
        elif y < -280:
            snake.segments[0].goto(x, 280)
    # Detect collision with wall player 2
    if snake2.head.xcor() > 280 or snake2.head.xcor() < -280 or snake2.head.ycor() > 280 or snake2.head.ycor() < -280:
        # x2 = snake2.head.xcor()
        # y2 = snake2.head.ycor()
        # if x2 > 280:
        #     snake2.segments[0].goto(-280, y2)
        # elif x2 < -280:
        #     snake2.segments[0].goto(280, y2)
        # elif y2 > 280:
        #     snake2.segments[0].goto(x2, -280)
        # elif y2 < -280:
        #     snake2.segments[0].goto(x2, 280)
        game_is_on = False
        scoreboard.game_over()

screen.exitonclick()
