import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
# import random


scr = Screen()
scr.setup(600, 600)
scr.bgcolor("black")
scr.title("Snake game")
# disable refreshing the screen
scr.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()
scr.listen()

scr.onkey(snake.up, "Up")
scr.onkey(snake.down, "Down")
scr.onkey(snake.left, "Left")
scr.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    scr.update()
    time.sleep(0.1)
    snake.move()

    # food collision check
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    # wall collision
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.xcor() < -280:
        game_is_on = False
        score.game_over()

    for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()

scr.exitonclick()
