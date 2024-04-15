from turtle import Turtle
ALIGNMENT = "center"
FONT  = ("Arial", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        with open("highscore.txt") as file:
            self.high_score = int(file.read())
        self.goto(0, 270)
        self.color("white")
        self.hideturtle()
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score = {self.score} High Score = {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()
        self.save_high_score()

    def save_high_score(self):
        with open("highscore.txt", "w") as file:
            file.write(str(self.high_score))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", align=ALIGNMENT, font=FONT)