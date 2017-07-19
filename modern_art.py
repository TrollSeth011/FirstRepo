from turtle import *
from random import *

screen = Screen()

def randomcolor():
    red = 1
    green = 2
    blue = 3
    choice = randint(1, 3)
    if choice == 1:
        return color('red')
    elif choice == 2:
        return color('green')
    else:
        return color('blue')
def randomplace():
    x = randint(-100, 100)
    y = randint(-100, 100)
    penup()
    goto(x,y)
    pendown()
def drawrec():
    hideturtle()
    length = randint(10, 50)
    height = randint(10, 50)
    begin_fill()
    forward(length)
    right(90)
    forward(height)
    right(90)
    forward(length)
    right(90)
    forward(height)
    right(90)
    end_fill()

shape("turtle")
for i in range(0, 19):
    randomcolor()
    randomplace()
    drawrec()
    #stamp()
screen.exitonclick()
