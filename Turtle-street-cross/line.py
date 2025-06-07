from turtle import Turtle


class Line(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.hideturtle()
        self.width_multiplier = 30
        self.length_multiplier = 0.05
        self.shapesize(stretch_wid=self.width_multiplier, stretch_len=self.length_multiplier)

    def create(self, position, color):
        self.goto(position)
        self.color(color)
        self.shapesize(stretch_wid=self.width_multiplier, stretch_len=self.length_multiplier)
        self.showturtle()
