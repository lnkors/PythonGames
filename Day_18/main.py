#From turtle module, import the Turtle Class (blueprint)
#Packaged with the preset python library
import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color_tuple = (r, g, b)
    return color_tuple

#Import Everything from the module (can get confusing though)
#from turtle import *

#Import the module with a different name (best used when modules have long names so it can be modified)
#import turtle as t

#Some modules cannot be imported, it needs to be installed
#want to access different modules/packages
#Install first, then you can import it

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
#timmy_the_turtle.color("blue")

#Draw a square (Challenge 1)
# for i in range(0,4):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.left(90)

#Draw a dashed line (Challenge 2)
# for j in range(0,15):
#     timmy_the_turtle.pendown()
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.penup()
#     timmy_the_turtle.forward(10)

#Draw Different Shapes (Challenge 3)
# def draw_shape(num_sides):
#     angle = 360/ num_sides
#     for i in range(num_sides):
#         timmy_the_turtle.forward(100)
#         timmy_the_turtle.right(angle)
#
# for shape_side in range(3,10):
#     draw_shape(shape_side)

#Generate a Random Walk (Challenge 4)
colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
# options = [0, 90, 180, 270]
#
# for i in range(0,200):
#     angle = random.choice(options)
#     timmy_the_turtle.color(random_color())
#     timmy_the_turtle.pensize(10)
#     timmy_the_turtle.speed("fastest")
#     timmy_the_turtle.setheading(angle)
#     timmy_the_turtle.forward(20)
#
# #Python Tuple
# #Cannot edit it. Cannot be changed in any way
# my_tuple = (1, 3, 4)

#Generate a Random Spirograph (Challenge 5)

timmy_the_turtle.speed("fastest")

def draw_spiro(size):
    for i in range(int(360/ size)):
        timmy_the_turtle.color(random_color())
        timmy_the_turtle.circle(100)
        timmy_the_turtle.setheading(timmy_the_turtle.heading()+ size)

draw_spiro(5)

screen = Screen()
screen.exitonclick()