import turtle
from turtle import Turtle, Screen
import random


tur = Turtle()
scr = Screen()


def move_forwards():
    tur.forward(10)

def rotate_right():
    tur.right(10)

def rotate_left():
    tur.left(10)

def clear():
    tur.reset()

scr.listen()
scr.onkey(key="w", fun=move_forwards)
scr.onkey(key="d", fun=rotate_right)
scr.onkey(key="a", fun=rotate_left)
scr.onkey(key="c", fun=clear)



scr.exitonclick()


