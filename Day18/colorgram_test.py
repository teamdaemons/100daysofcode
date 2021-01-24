#import colorgram

# colors = colorgram.extract('hirst_painting.jpg', 30)
# print(colors)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

import turtle as t
import random

t.colormode(255)
tim = t.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [(199, 175, 117), (212, 222, 215), (125, 36, 24), (223, 224, 228), (167, 106, 56), (186, 159, 52),
              (6, 57, 83), (108, 68, 85), (112, 161, 175), (21, 122, 174), (63, 153, 138), (39, 36, 35), (76, 40, 48),
              (9, 68, 47), (90, 141, 52), (182, 96, 79), (131, 38, 41), (141, 171, 156), (210, 200, 149),
              (179, 201, 186), (173, 153, 159), (212, 183, 176), (151, 114, 119), (177, 198, 203), (206, 184, 190),
              (37, 73, 84), (45, 74, 63), (48, 66, 80)]
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = t.Screen()
screen.exitonclick()
