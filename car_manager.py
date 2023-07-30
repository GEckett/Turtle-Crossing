from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        """Generates the cars"""
        self.cars = []
        self.move_dist = STARTING_MOVE_DISTANCE
        self.create_cars()

    def create_cars(self):
        car = Turtle(shape="square")
        car.color(random.choice(COLORS))
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.penup()
        car.goto((300, random.randrange(-200, 200, 20)))
        car.setheading(180)
        self.cars.append(car)

    def move(self):
        for item in range(len(self.cars)):
            self.cars[item].forward(self.move_dist)

    def speed_up(self):
        self.move_dist += MOVE_INCREMENT

