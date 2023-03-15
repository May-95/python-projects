from turtle import Turtle

FONT = ('Courier', 20, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.write_score()

    # writes score onto the board
    def write_score(self):
        self.clear()
        self.goto(100, 200)
        self.write(f"Score: {self.r_score}", align="center", font=FONT)
        self.goto(-100, 200)
        self.write(f"Score: {self.l_score}", align="center", font=FONT)

    # updates the score and writes the new score onto the screen.
    def update_right(self):
        self.r_score += 1
        print("right score")
        self.write_score()

    def update_left(self):
        self.l_score += 1
        print("left score")
        self.write_score()
