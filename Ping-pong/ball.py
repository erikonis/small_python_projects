from turtle import Turtle
from random import randint as r

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.x_move = 10
        self.y_move = 10
        self.time_speed = 0.1


    def create(self, position):
        self.shape("circle")
        self.penup()
        self.color("white")
        self.goto(position)
        self.speed(2)

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def wall_bounce(self):
        self.y_move *= -1

    def paddle_bounce(self):
        self.x_move *= -1
        self.time_speed *= 0.9

    def reset_pos(self):
        self.teleport(0, 0)
        self.paddle_bounce()
        self.time_speed = 0.1

    def debug(self):
        self.color(r(0, 255), r(0, 255), r(0, 255))
        self.pendown()