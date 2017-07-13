from turtle import *

file = open('dictionary.txt', 'r')
colours = {}
for line in file:
    x = line.split(",")
    a=x[0]
    b=x[1]
    c=len(b)-1
    b=b[0:c]
    colours[a]=b

screen  = Screen()
screen.setup(1000,1000)


screen.bgcolor(colours['green'])

dot(500)
def Colorpicker(colors, word):
    color(colours[colors])
    style = ('Arial', 40, 'bold')
    write(word, font=style, align='center')
    hideturtle()

def Moveturtle():
    penup()
    right(90)
    forward(60)
    left(90)
Colorpicker('orange', 'Hello')
Moveturtle()
Colorpicker('red', 'Good')
Moveturtle()
Colorpicker('green', 'This')
screen.exitonclick()
