import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
screen.listen()
screen.onkey(player.move_up, "Up")
score = Scoreboard()
car_manager = CarManager()

# player.goto(0, 260)

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    if player.is_at_finishline():
        score.level_up()
        player.level_up()
        car_manager.level_up()

    if random.randint(1, 6) == 6:
        car_manager.add_car()

    car_manager.move_cars()

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            score.game_is_over()

screen.exitonclick()