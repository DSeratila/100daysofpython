from turtle import Turtle

STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for i in STARTING_POS:
            self.add_segment(i)

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            # print(i)
            x = self.segments[i - 1].xcor()
            y = self.segments[i - 1].ycor()
            self.segments[i].goto(x, y)
            # snake[i].setx(x)
            # snake[i].sety(y)
        self.head.forward(MOVE_DISTANCE)

    def add_segment(self, position):
        t = Turtle()
        t.color("white")
        t.shape("square")
        t.penup()
        t.goto(position)
        self.segments.append(t)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
