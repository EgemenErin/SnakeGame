from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0,270)
        self.score = 0
        self.write(f"Score : {self.score}", align="center", font=("Comic Sans MS", 19, "normal"))

    def scoreUp(self):
        self.score += 1
        self.clear()
        self.write(f"Score : {self.score}", align="center", font=("Comic Sans MS", 19, "normal"))

    def GameOver(self):
        self.goto(0,0)
        self.write(f"Game Over", align="center", font=("Comic Sans MS", 19, "normal"))
        self.goto(0, -20)
        self.write(f"your score was {self.score}", align="center", font=("Comic Sans MS", 19, "normal"))

    def refresh(self):
        self.score = 0
        self.clear()
        self.write(f"Score : {self.score}", align="center", font=("Comic Sans MS", 19, "normal"))
