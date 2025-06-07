from turtle import Turtle, Screen

t = Turtle()
screen = Screen()
t.color("red")

def move_forward():
    t.forward(30)
def move_backward():
    t.forward(-30)

def turn_left():
    t.left(30)

def turn_right():
    t.right(30)

def reset():
    screen.reset()
    t.color("red")

screen.listen()
screen.onkey(move_forward, "Up")
screen.onkey(move_backward, "Down")
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")
screen.onkey(reset, "c")


screen.exitonclick()

