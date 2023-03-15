import time
from turtle import Screen, Turtle
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

# creating game screen.
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# game objects.
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

# listening to key presses.
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

# game loop.
game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    # detects wall collision and bounces the ball.
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detects paddle collision and bounces the ball.
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        scoreboard.update_right()
        ball.bounce_x()
    if ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        scoreboard.update_left()
        ball.bounce_x()

    # detects when paddles miss the ball.
    # Ball is reset to the centre of the board and a point is given to their opponent.
    if ball.xcor() > 380:
        scoreboard.update_left()
        ball.reset()

    if ball.xcor() < -380:
        scoreboard.update_right()
        ball.reset()

screen.exitonclick()
