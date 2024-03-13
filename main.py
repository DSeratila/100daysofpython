import turtle
from turtle import Turtle
import random

t = Turtle()
t.shape("turtle")
t.color('red')
t.screen.colormode(255)
t.penup()
t.left(90)
t.forward(300)
t.right(90)
t.pendown()

for i in range(3, 21):
    g = random.randrange(0, 257, 10)
    b = random.randrange(0, 257, 10)
    r = random.randrange(0, 257, 10)
    print(r, g, b)
    tup = (r, g, b)
    t.pencolor(tup)
    angle = 360/i
    # if angle != 90:
    t.right(angle)
    for r in range(0, i):
        if i % 2 == 0:
            for _ in range(0, 5):
                t.forward(10)
                t.penup()
                t.forward(4)
                t.pendown()
                t.forward(2)
                t.penup()
                t.forward(4)
                t.pendown()
        else:
            t.forward(100)
        if r != i-1:
            t.right(angle)

screen = turtle.Screen()
screen.exitonclick()

