from turtle import Turtle
import random


# creates random food onto the screen.
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("green")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5, )
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)

    # generates new location for the food when snake has eaten it.
    def new_location(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
