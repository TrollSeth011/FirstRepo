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
screen.setup(400,400)


screen.bgcolor(colours['green'])

circle(50)
dot(300)

color(colours['red'])
style = ('Arial', 40, 'bold')
write('Hello', font=style, align='center')
hideturtle()
screen.exitonclick()
