from turtle import Turtle
from random import randint as r

CARS_SPAWN_Y_BORDERS = (-190, 235)
CARS_SPAWN_X_BORDERS = (300, 380)
CAR_LIMIT_START = 8
CAR_LIMIT_MAX = 16


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.step = r(10, 20)


class CarsManager:
    def __init__(self):
        self.cars = []
        self.level = 0
        self.car_limit = CAR_LIMIT_START + self.level

    def create(self):
        car = Car()
        car.penup()
        car.shape("square")
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.color(r(0, 255), r(0, 255), r(0, 255))
        car.teleport(r(CARS_SPAWN_X_BORDERS[0], CARS_SPAWN_X_BORDERS[1]),
                     r(CARS_SPAWN_Y_BORDERS[0], CARS_SPAWN_Y_BORDERS[1]))
        car.setheading(270)
        car.showturtle()
        return car

    def start_generation(self):
        self.car_limit = CAR_LIMIT_START + self.level
        for num in range(self.car_limit):
            if len(self.cars) < self.car_limit:
                car = self.create()
                self.cars.append(car)

        for i in range(len(self.cars)):
            self.cars[i].forward(self.cars[i].step)
            if self.cars[i].xcor() < -310:
                self.cars[i].hideturtle()
                self.cars[i] = self.create()

    def reset(self):
        self.cars.clear()