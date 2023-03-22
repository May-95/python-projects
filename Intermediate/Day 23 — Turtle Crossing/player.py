from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.go_to_start()
        self.setheading(90)

    # moves player forward.
    def move(self):
        self.forward(MOVE_DISTANCE)

    # checks if player has reached the finish line.
    def finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

    # takes player to the starting position.
    def go_to_start(self):
        self.goto(STARTING_POSITION)
