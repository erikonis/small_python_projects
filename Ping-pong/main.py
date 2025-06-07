from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from random import randint as r
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.colormode(255)
screen.bgcolor("black")
screen.title("Ping Pong Game")
screen.tracer(0)

user_paddle = Paddle()
user_paddle.create((-350, 0))
ai_paddle = Paddle()
ai_paddle.create((350, 0))
ball = Ball()
ball.create((0, 0))
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(user_paddle.move_up, "w")  #stopped here. Have to continue in file paddle.py
screen.onkeypress(user_paddle.move_down, "s")
screen.onkeypress(ai_paddle.move_up, "Up")  # stopped here. Have to continue in file paddle.py
screen.onkeypress(ai_paddle.move_down, "Down")
screen.onkey(ball.debug, "space")

game_on = True
wall_collision = False
paddle_collision = False

while game_on:
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.wall_bounce()

    if ball.distance(ai_paddle) < 50 and ball.xcor() > 320 or ball.distance(user_paddle) < 50 and ball.xcor() < -340:
        ball.paddle_bounce()

    if ball.xcor() > 350:
        scoreboard.user_score += 1
        scoreboard.refresh()
        ball.reset_pos()

    elif ball.xcor() < -350:
        scoreboard.ai_score += 1
        scoreboard.refresh()
        ball.reset_pos()

    time.sleep(ball.time_speed)
    screen.update()

screen.exitonclick()
