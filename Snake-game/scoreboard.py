from turtle import Turtle
FONT = ("Arial", 16, "bold")
class Scoreboard:
    def __init__(self):
        self.scoreboard = Turtle()
        self.scoreboard.hideturtle()
        self.scoreboard.penup()
        self.scoreboard.color("white")
        self.score = 0
        self.scoreboard.goto(0, 270)
        self.count(self.score)


    def count(self, score):
        self.scoreboard.clear()
        self.score += score
        self.scoreboard.write(arg=f"Score: {self.score}", move=False, align="center", font=FONT)

    def game_over(self):
        self.scoreboard.goto(0, 0)
        self.scoreboard.write(arg=f"Game over.", move=False, align="center", font=FONT)
