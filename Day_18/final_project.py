import colorgram

import turtle
from turtle import Turtle, Screen

import random

# # Extract 6 colors from an image.
# colors = colorgram.extract('image.jpg', 30)
#
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

tim = Turtle()
screen = Screen()
color_list = [(220, 173, 4), (2, 134, 196), (7, 149, 99), (241, 123, 42), (229, 116, 154), (243, 236, 241), (128, 160, 203), (29, 18, 65), (240, 161, 190), (232, 84, 113), (216, 233, 244), (236, 244, 240), (235, 201, 45), (195, 18, 40), (201, 29, 49), (2, 173, 119), (83, 30, 21), (189, 69, 41), (69, 12, 64), (3, 68, 162), (232, 53, 32), (141, 208, 237), (118, 107, 170), (0, 124, 76), (19, 158, 205), (120, 184, 157), (104, 44, 37), (241, 198, 6), (156, 212, 190)]

#size 20, spaced apart by 50
#10 by to dots using planned color pallet

screen.colormode(255)

tim.speed("fastest")

tim.setheading(225)
tim.penup()
tim.fd(300)
tim.setheading(0)

num_dots = 100

for dots in range(1,num_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.penup()
    tim.fd(50)
    if dots % 10 == 0:
        tim.hideturtle()
        tim.setheading(90)
        tim.fd(50)
        tim.setheading(180)
        tim.fd(500)
        tim.setheading(0)

screen = Screen()
screen.exitonclick()