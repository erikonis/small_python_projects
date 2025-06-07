from turtle import Screen
import time

from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.colormode(255)
screen.setup(width=600, height=600)
screen.bgcolor("Black")
screen.title("The greatest snake game ever")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()


def game_over():
    scoreboard.game_over()
    return False


food_collision = False
wall_collision = False
tail_collision = False
game_on = True

while game_on:

    screen.listen()
    screen.update()
    time.sleep(0.1)

    snake.move()

    if snake.head.distance(food) < 16:
        food_collision = True

    if snake.head.pos()[0] < -285 or snake.head.pos()[0] > 285 or snake.head.pos()[1] < -285 or snake.head.pos()[
        1] > 285:
        wall_collision = True

    for square in snake.squares[1:]:
        if snake.head.distance(square.pos()) < 19:
            tail_collision = True

    if tail_collision:
        game_on = game_over()

    elif wall_collision:
        snake.teleport()
        # game_on = game_over()

    if food_collision:
        food.refresh()
        snake.grow()
        scoreboard.count(1)

    screen.onkey(snake.left, key="Left")
    screen.onkey(snake.right, key="Right")
    screen.onkey(snake.up, key="Up")
    screen.onkey(snake.down, key="Down")
    screen.onkey(snake.space, key="space")

    food_collision = False

screen.exitonclick()