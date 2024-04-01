import time
import turtle
from turtle import Turtle, Screen
import random


scr = Screen()
scr.setup(600, 600)
scr.bgcolor("black")
scr.title("Snake game")
#disable refreshing the screen
scr.tracer(0)

snake = []
starting_pos = [(0, 0), (-20, 0), (-40, 0)]

for i in range(0, 3):
    t = Turtle()
    t.color("white")
    t.shape("square")
    t.penup()
    t.teleport(starting_pos[i][0], starting_pos[i][1])
    snake.append(t)

game_is_on = True

while game_is_on:
    scr.update()
    time.sleep(0.1)

    for i in range(len(snake) - 1, 0, -1):
        # print(i)
        x = snake[i - 1].xcor()
        y = snake[i - 1].ycor()
        snake[i].goto(x, y)
        # snake[i].setx(x)
        # snake[i].sety(y)
    snake[0].forward(20)
    
scr.exitonclick()


