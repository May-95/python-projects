from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        self.new_car()

    # new car generated when the random number generated equals 1.
    def new_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            car = Turtle("square")
            random_y = random.randint(-250, 250)
            car.color(random.choice(COLORS))
            car.penup()
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.goto(300, random_y)
            self.all_cars.append(car)

    # moves the cars forward.
    def move(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    # increases car speed when player has reached a new level.
    def next_level(self):
        self.car_speed += MOVE_INCREMENT
