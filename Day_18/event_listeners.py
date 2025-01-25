from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.fd(10)

def move_backwards():
    tim.back(10)

def move_CW():
    tim.right(10)

def move_CCW():
    tim.left(10)

def clear():
    tim.penup()
    tim.clear()
    tim.home()
    tim.pendown()

# screen.listen()
# screen.onkey(key = "space", fun = move_forward)
# screen.exitonclick()

#Higher order function
#Functions that can take inputs as function and working with it inside this (onkey is an example of this)

#Etch A Sketech Program

screen.listen()
screen.onkey(key = "w", fun = move_forward)
screen.onkey(key = "s", fun = move_backwards)
screen.onkey(key = "d", fun = move_CW)
screen.onkey(key = "a", fun = move_CCW)
screen.onkey(key = "c", fun = clear)


screen.exitonclick()