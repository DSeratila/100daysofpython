import turtle
from turtle import Turtle
import random

t = Turtle()
# t.shape("turtle")
# t.color('red')
t.screen.colormode(255)


def get_ready():
    # t.pensize(7)
    t.speed(0)
    # t.penup()
    # t.left(90)
    # t.forward(300)
    # t.right(90)
    # t.pendown()


def change_color_to_random():
    g = random.randrange(0, 257, 10)
    b = random.randrange(0, 257, 10)
    r = random.randrange(0, 257, 10)
    t.pencolor(r, g, b)


def get_random_direction():
    directions = [270, 90, 0, 180]
    return random.choice(directions)


def draw_line():
    change_color_to_random()
    t.setheading(get_random_direction())
    t.forward(15)


def draw_circle(tilt: int):
    change_color_to_random()
    t.right(tilt)
    t.circle(100)

get_ready()

# for a in range(2000):
#     draw_line()

for _ in range(36):
    draw_circle(10)


screen = turtle.Screen()
screen.exitonclick()

