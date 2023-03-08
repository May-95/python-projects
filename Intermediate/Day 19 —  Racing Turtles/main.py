from turtle import Turtle, Screen
import random

screen = Screen()

# setting screen width and height.
screen.setup(width=500, height=500)

# race begins when variable is True.
is_race_on = False

# list of turtle colours.
colours = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

# list of turtles that will race.
list_of_turtles = []

# starting y position for the first turtle.
y = -100

# for loop to create new racing turtles.
for _ in range(6):
    # turtle colour chosen from colours list.
    turtle_colour = colours[_]
    # new turtle object created.
    racing_turtle = Turtle(shape="turtle")
    # turtle colour is set.
    racing_turtle.color(turtle_colour)
    # turtle has pen up so that they don't write whilst moving.
    racing_turtle.penup()
    # turtle's starting position.
    racing_turtle.goto(x=-240, y=y)
    # y position updated so new turtle will have a different y position compared to the rest.
    y += 40
    # newly created turtle is added to list of turtles.
    list_of_turtles.append(racing_turtle)

# user makes their bet on which turtle will be the fastest.
user_bet = screen.textinput(title="Make your bet!", prompt="Which turtle will win the race? Enter a colour: ").lower()

# race is on when user has made a bet.
if user_bet:
    is_race_on = True

# race begins when is_race_on is True.
while is_race_on:
    for turtle in list_of_turtles:
        # if turtle's x coordinates are less than 230, they can move.
        if turtle.xcor() < 230:
            turtle.forward(random.randint(1, 10))
        # if turtle's x coordinates are more than 230, they have won.
        else:
            # is_race_on is turned False ending the game.
            is_race_on = False
            # saves the winning turtle's colour.
            winner = turtle.pencolor()
            # user's bet and the winning turtle are compared and message is printed to user.
            if winner == user_bet:
                print(f"Congratulations! You correctly bet that the {user_bet} turtle would win.")
            else:
                print(f"Sorry, the {user_bet} turtle did not win the race. {winner.title()} turtle won!")

screen.exitonclick()
