import turtle
from turtle import Turtle, Screen
import random



scr = Screen()
scr.setup(500, 400)
user_bet = scr.textinput(title="Make your bet", prompt="Which turtle is going to win? Enter the color:")
colors = ["red", "orange", "teal", "green", "blue", "purple"]
is_race_on = False
all_turtles = []

for i in range(0, 6):
    t = Turtle(shape='turtle')
    t.color(colors[i])
    all_turtles.append(t)


starting_x_pos = -240
starting_y_pos = 90

for t in all_turtles:
    t.teleport(starting_x_pos, starting_y_pos)
    starting_y_pos -= 25
    t.penup()


if user_bet:
    is_race_on = True

while is_race_on:
    if t.xcor() > 230:
        is_race_on = False
        print(t.pencolor())
        if t.pencolor() == user_bet:
            print("You've won")
    for t in all_turtles:
        t.forward(random.randint(0, 10))




scr.exitonclick()


