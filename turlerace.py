from turtle import *
from random import randint
#Create the screen
turtle1 = 0
turtle2 = 0
turtle3 = 0

window = Screen()
"""
for i in range(5):
    write(i)
    speed(1)
    forward(20)
"""
def CreateCourse():
    penup()
    goto(-140, 140)
    for step in range(16):
        speed(10)
        write(step, align='center')
        right(90)
        forward(10)
        pendown()
        forward(150)
        penup()
        backward(160)
        left(90)
        forward(20)

def CreateTurtles():
    #turtle 1
    t1 = Turtle()
    t1.shape('turtle')
    t1.color('orange')
    t1.penup()
    t1.goto(-160, 100)
    t1.pendown()


    #turtle 2
    t2 = Turtle()
    t2.shape('turtle')
    t2.color('red')
    t2.penup()
    t2.goto(-160, 70)
    t2.pendown()


    #turtle 3
    t3 = Turtle()
    t3.shape('turtle')
    t3.color('blue')
    t3.penup()
    t3.goto(-160, 40)
    t3.pendown()

    #race
    for turn in range(100):
        global turtle1
        global turtle2
        global turtle3
        num1 = randint(1, 5)
        turtle1 += num1
        num2 = randint(1, 5)
        turtle2 += num2
        num3 = randint(1, 5)
        turtle3 += num3


        t1.forward(num1)
        t2.forward(num2)
        t3.forward(num3)
    print("t1 " + str(turtle1))
    print("t2 " + str(turtle2))
    print("t3 " + str(turtle3))

    #declare winner
    penup()
    goto(-50, 250)
    if turtle1 > turtle2 and turtle1 > turtle3:
        write('Turtle1 is the winner',move=Flase, align="center", font=("Arial",50,"normal"))
    elif turtle2 > turtle1 and turtle2 > turtle3:
        write('Turtle2 is the winner')
    else:
        write('Turtle3 is the winner')
CreateCourse()
CreateTurtles()
window.exitonclick()
