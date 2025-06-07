from turtle import Turtle

SPAWN = (0, -250)
MOVE_STEP = 15

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.reset_all()

    def move_up(self):
        self.setheading(0)
        self.forward(MOVE_STEP)

    def move_down(self):
        self.setheading(180)
        self.forward(MOVE_STEP)

    def move_right(self):
        self.setheading(90)
        self.forward(MOVE_STEP)

    def move_left(self):
        self.setheading(270)
        self.forward(MOVE_STEP)

    def reset_all(self):
        self.shape("turtle")
        self.color("blue")
        self.penup()
        self.setheading(0)
        self.goto(SPAWN)