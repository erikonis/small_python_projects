from turtle import Turtle
class Snake:
    def __init__(self):
        self.squares = []
        self.starting_position = (0, 0)
        self.speed = 20 #default - 20

        self.create()
        self.head = self.squares[0]

    def create(self):
        for number in range(3):
            square = Turtle(shape="square")
            square.color("white")

            square.penup()
            square.goto(self.starting_position)

            self.starting_position = (
            square.pos()[0] - 20, square.pos()[1])  # The X coordinate is changed by -20, the Y remains the same
            self.squares.append(square)

    def move(self):
        for num in range(len(self.squares) - 1, 0, -1):
            new_x = self.squares[num - 1].xcor()
            new_y = self.squares[num - 1].ycor()
            self.squares[num].goto(new_x, new_y)
        self.squares[0].forward(self.speed)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)


    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def grow(self):
        square = Turtle(shape="square")
        square.color("white")

        square.penup()
        square.goto(self.head.pos())
        self.squares.append(square)

    def teleport(self):
        if self.head.pos()[0] < -285:  # X coord
            self.head.teleport(285, self.head.pos()[1])
        elif self.head.pos()[0] > 285:
            self.head.teleport(-285, self.head.pos()[1])
        elif self.head.pos()[1] < -285:  # Y coord
            self.head.teleport(self.head.pos()[0], 285)
        elif self.head.pos()[1] > 285:
            self.head.teleport(self.head.pos()[0], -285)
    def space(self): #Developer mode
        import random
        self.head.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), )
        self.head.pendown()