from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.user_score = 0
        self.ai_score = 0

        self.goto(-100, 200)
        self.write(self.user_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.ai_score, align="center", font=("Courier", 80, "normal"))

    def refresh(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.user_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.ai_score, align="center", font=("Courier", 80, "normal"))
