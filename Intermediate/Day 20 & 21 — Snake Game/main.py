from turtle import Screen

from scoreboard import Scoreboard
from snake import Snake
from food import Food
import time

# create screen.
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game!")
screen.tracer(0)

# create snake, food, and score objects from their classes.
snake = Snake()
food = Food()
score = Scoreboard()

# add listeners to keys.
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.right, "Right")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")

game_on = True

# game loop.
while game_on:
    screen.update()
    time.sleep(0.2)
    snake.move()

    # detects if snake has eaten the food.
    if snake.head.distance(food) < 15:
        food.new_location()
        score.update_score()
        snake.extend_snake()

    # detects if snake is outside the game window. GAME OVER if out of bounds.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_on = False
        score.game_over()

    # detects if snake has collided into itself. GAME OVER if snake crashes into itself.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_on = False
            score.game_over()

screen.exitonclick()
