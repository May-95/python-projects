from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.color("Black")
        self.hideturtle()
        self.penup()
        self.goto(-230, 250)
        self.write_level()

    # writes current level to the game window.
    def write_level(self):
        self.write(f"Level: {self.level}", align='center', font=FONT)

    # writes game over message to player.
    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER!", align='center', font=FONT)

    # updates level when player has reached the other side.
    def update_level(self):
        self.level += 1
        self.clear()
        self.write_level()
