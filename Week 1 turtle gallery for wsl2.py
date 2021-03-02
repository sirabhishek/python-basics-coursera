import turtle
import random
#remove from here...... 
import tkinter
import _tkinter

HEIGHT = 700
WIDTH = 800

root = tkinter.Tk()
root.title("Turtle Screen")

canvas = tkinter.Canvas(root, height = HEIGHT, width=WIDTH)
canvas.pack()

root.mainloop()
# .....till here for windows and then run

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

turtle.Screen().exitonclick()
    
    

