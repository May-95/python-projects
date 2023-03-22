from turtle import Turtle

# constant values.
ALIGN = "center"
FONT = ('Courier', 20, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.write_score()

    # writes score onto screen.
    def write_score(self):
        self.write(f"Score: {self.score}   High Score: {self.high_score}", align=ALIGN, font=FONT)

    # prints GAME OVER message.
    def game_over(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.goto(0, 0)
        self.write("GAME OVER!", align=ALIGN, font=FONT)

    # updates score after snake has eaten the food. Writes updated score onto the screen.
    def update_score(self):
        self.score += 1
        self.clear()
        self.write_score()
