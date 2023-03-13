from turtle import Turtle

# constant values.
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
RIGHT = 0
DOWN = 270
LEFT = 180


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    # create a 3 segment snake.
    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    # create each segment of the snake.
    def add_segment(self, position):
        new_turtle = Turtle()
        new_turtle.shape("square")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(position)
        self.segments.append(new_turtle)

    # adds another segment after each food is eaten.
    def extend_snake(self):
        last_position = self.segments[-1].position()
        self.add_segment(last_position)
        print(self.segments)

    # moving the snake.
    def move(self):
        for number in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[number - 1].xcor()
            new_y = self.segments[number - 1].ycor()
            self.segments[number].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    # sets snake's heading depending on user's choice.
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
