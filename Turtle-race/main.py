from turtle import Turtle, Screen
import random


def start():
    screen = Screen()
    screen.colormode(255)
    screen.setup(width=500, height=400)

    game_on = False

    choice = screen.textinput(title="Top ESports Betting Platform (TES BP)",
                              prompt="What color turtle ar you choosing to bet on?")

    y_positions = [-150, -90, -30, 30, 90, 150]
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    turtles = []

    for turtle_num in range(0, 6):
        tim = Turtle(shape="turtle")
        tim.color(colors[turtle_num])
        tim.penup()
        tim.goto(-230, y_positions[turtle_num])
        turtles.append(tim)

    if choice:
        game_on = True

    while game_on:
        for turtle in turtles:
            turtle.pendown()
            turtle.forward(random.randint(0, 10))
            if turtle.pos()[0] > 225:
                winner = turtle
                game_on = False

    print(f"The winner is {winner.color()[0]} turtle and you chose {choice}.")
    if choice == winner.color()[0]:
        print("You WON the bet!")
    else:
        print("You LOST the bet!")


    screen.exitonclick()


start()
