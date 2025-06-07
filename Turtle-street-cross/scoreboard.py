from turtle import Turtle
import time

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0

        self.penup()
        self.color("black")
        self.hideturtle()
        self.goto(0, 270)
        self.write(f"Level: {self.level}", move=False, align="center", font=("Courier", 20, "normal"))
        self.goto(0, 235)
        self.write("FINISH", move=False, align="center", font=("Courier", 10, "normal"))

    def level_up(self):

        self.level += 1
        self.clear()
        self.goto(0, 270)
        self.write(f"Level: {self.level}", move=False, align="center", font=("Courier", 20, "normal"))
        self.goto(0, 235)
        self.write("FINISH", move=False, align="center", font=("Courier", 10, "normal"))

    def died(self):
        self.goto(0, 0)
        self.write(f"You died. Press `SPACE` to reset.", move=False, align="center", font=("Courier", 20, "normal"))
        self.level = 0

    def refresh(self):
        self.clear()
        self.goto(0, 270)
        self.write(f"Level: {self.level}", move=False, align="center", font=("Courier", 20, "normal"))
        self.goto(0, 235)
        self.write("FINISH", move=False, align="center", font=("Courier", 10, "normal"))