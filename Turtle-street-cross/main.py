from turtle import Turtle, Screen
from player import Player
import time
from line import Line
from cars import CarsManager
from scoreboard import Scoreboard

ROAD_START_Y = -200
FINISH_LINE_Y = 250
TIME_MULTIPLIER = 0.98

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.tracer(0)
screen.mode("logo")
screen.colormode(255)

finish = Line()
finish.create(position=(0, FINISH_LINE_Y), color="green")
start = Line()
start.create(position=(0, ROAD_START_Y), color="red")
blood = Turtle(shape="circle")
blood.color("red")
blood.penup()
blood.hideturtle()
player = Player()
car_manager = CarsManager()
scoreboard = Scoreboard()


def key_activation():
    screen.onkeypress(player.move_up, "Up")
    screen.onkeypress(player.move_down, "Down")
    screen.onkeypress(player.move_left, "Left")
    screen.onkeypress(player.move_right, "Right")


def key_deactivation():
    screen.onkeypress(None, "Up")
    screen.onkeypress(None, "Down")
    screen.onkeypress(None, "Left")
    screen.onkeypress(None, "Right")


def level_up():
    global freeze_time, TIME_MULTIPLIER
    car_manager.level += 1
    scoreboard.level_up()
    freeze_time *= TIME_MULTIPLIER
    player.reset_all()

def reset():
    global accident_index, accident_count, freeze_time, accident, game_progress, finish, start, blood, player

    car_manager.reset()
    accident_index = 0
    accident_count = 0
    freeze_time = 0.1
    accident = False
    game_progress = True

    screen.clear()
    screen.setup(width=600, height=600)
    screen.bgcolor("white")
    screen.tracer(0)
    screen.mode("logo")
    screen.colormode(255)

    finish = Line()
    finish.create(position=(0, FINISH_LINE_Y), color="green")
    start = Line()
    start.create(position=(0, ROAD_START_Y), color="red")
    blood = Turtle(shape="circle")
    blood.color("red")
    blood.penup()
    blood.hideturtle()
    player = Player()

    scoreboard.refresh()
    key_activation()


key_activation()
game_on = True
game_progress = True
accident = False
accident_index = 0
accident_count = 0
freeze_time = 0.1
blood_color = "red"

while game_on:
    screen.listen()

    car_manager.start_generation()
    for car in car_manager.cars:
        if player.distance(car) < 20:
            accident = True
            car.pencolor(blood_color)
            car.pensize(5)
            car.pendown()
            accident_count += 1
            blood.teleport(player.xcor(), player.ycor())
            blood.showturtle()

    if accident:
        key_deactivation()
        game_progress = False
        if accident_count > 5:
            player.color("firebrick")
            blood_color = "firebrick"
        player.pencolor(blood_color)

        accident_index += 1
        if accident_index > 5:
            scoreboard.died()
            screen.onkeypress(reset, "space")

    if player.ycor() > FINISH_LINE_Y:
        level_up()

    time.sleep(freeze_time)
    screen.update()

screen.exitonclick()
