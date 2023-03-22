# Day 23 -- Turtle Crossing

import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# screen setup.
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# object initialisation.
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# screen listens for keypress.
screen.listen()
screen.onkeypress(player.move, "Up")

# game loop.
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    # new car generated.
    car_manager.new_car()
    # car moves forward.
    car_manager.move()

    # checks all the cars to see if player has collided into them. Game over if there is a collision.
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # if player has reached the other side, they level up and the speed of the cars increase.
    if player.finish_line():
        player.go_to_start()
        scoreboard.update_level()
        car_manager.next_level()

screen.exitonclick()
