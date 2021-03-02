import turtle
import random


wn = turtle.Screen()
xd = turtle.Turtle()
xd.shape("turtle")
turtle.bgcolor("black")


xd.speed(0)
x = 1 
while x<400:
    redA = random.randint(0,255)
    greenA = random.randint(0,255)
    blueA = random.randint(0,255)

    turtle.colormode(255)
    xd.pencolor(redA,greenA,blueA)

    xd.forward(5+x)
    xd.right(90.99)
    x=x+1
    
    

