import turtle
from turtle import Turtle
import random
import colorgram


t = Turtle()
# t.shape("turtle")
# t.color('red')


def get_ready():
    t.pensize(20)
    t.screen.colormode(255)
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

def draw_dot(color: turtle):
    t.pendown()
    t.pencolor(color[0], color[1], color[2])
    t.forward(1)
    t.penup()

extracted_colors = []

get_ready()

for color in colorgram.extract("Hirst painting.jpeg", 100):
    extracted_colors.append((color.rgb.r, color.rgb.g, color.rgb.b))

starting_y = -260
starting_x = - 230
t.teleport(starting_x, starting_y)

for i in range(100):
    if i % 10 == 0:
        print("kek")
        starting_y += 50
        t.teleport(starting_x, starting_y)
    draw_dot(random.choice(extracted_colors))
    t.forward(50)


screen = turtle.Screen()
screen.exitonclick()

