import turtle
from turtle import Turtle, Screen
import random

# import colorgram
# # Extract 20 colors from an image that will be used to create the painting.
# colours = colorgram.extract('image.jpg', 20)
# rbg_colours = []
# # loop to append rbg colours into the colours_list
# for colour in colours:
#     r = colour.rgb.r
#     g = colour.rgb.g
#     b = colour.rgb.b
#     rbg_colours.append((r, g, b))

colours_list = [(1, 12, 31), (53, 25, 17), (218, 127, 106), (10, 104, 159), (242, 213, 68), (149, 83, 39), (215, 87, 63),
               (155, 6, 24), (165, 162, 31), (157, 62, 102), (10, 64, 33), (206, 74, 104), (11, 96, 57), (95, 6, 20),
               (174, 135, 163), (1, 61, 145)]

turtle.colormode(255)

# create a turtle object from Turtle class.
timmy = Turtle()

# turtle speed changed to fastest.
timmy.speed("fastest")

# hides turtle.
timmy.hideturtle()

# pen is up so turtle doesn't write a line when moving.
timmy.penup()

# setting starting positions for x and y.
timmy.setx(-250)
timmy.sety(-250)

# loop to create 10 by 10 dots.
for _ in range(10):
    for _ in range(10):
        # creates a dot with a random colour chosen from the colours_list.
        timmy.dot(20, random.choice(colours_list))
        # turtle moves forward by 50.
        timmy.forward(50)
    # x coordinates are reset.
    timmy.setx(-250)
    # 50 is added to current y coordinates to create a new line on top of the current line.
    timmy.sety(timmy.ycor() + 50)

screen = Screen()
screen.exitonclick()
