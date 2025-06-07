from turtle import Turtle
from random import randint as r

class Food(Turtle):
    def __init__(self):
        super().__init__()

        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color(r(0, 255), r(0, 255), r(0, 255))
        self.speed("fastest")

        self.refresh()

    def refresh(self):
        import random
        self.color(r(0, 255), r(0, 255), r(0, 255))
        x_coord = random.randint(-290, 290)
        y_coord = random.randint(-290, 290)
        self.goto(x_coord, y_coord)
