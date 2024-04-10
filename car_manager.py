from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.car_speed = MOVE_INCREMENT

    def add_car(self):
        car = Turtle()
        car.penup()
        car.shape("square")
        car.shapesize(1, 2)
        # car.setheading(90)
        car.color(random.choices(COLORS))
        random_y = random.randint(-250, 250)
        car.goto(300, random_y)
        self.all_cars.append(car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)
            if car.xcor() < -320:
                self.all_cars.remove(car)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT