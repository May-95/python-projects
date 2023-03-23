# Day 25 -- U.S. States Game
import turtle
import pandas

# screen setup.
screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(width=725, height=491)
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# reading data from csv file and saving the data into a list.
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()


# prints the correctly guessed states onto the map where they are located.
def print_on_map(guessed_answer):
    write = turtle.Turtle()
    write.hideturtle()
    write.penup()
    state_date = data[data.state == guessed_answer]
    write.goto(int(state_date.x), int(state_date.y))
    write.write(guessed_answer)


guessed_states = []
window_title = "Guess the State"

# game loop.
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=window_title, prompt="What is another State's name?").title()
    # exits out of the game if user inputs "exit", csv file generated with all the missing states that were not guessed.
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        missing_states_data = pandas.DataFrame(missing_states)
        missing_states_data.to_csv("states_to_learn_csv")
        break
    # if user's answer is a correct state, and they have not guessed the state before,
    # then answer is added to guessed_states list and printed onto the map.
    if answer_state in all_states:
        if answer_state not in guessed_states:
            guessed_states.append(answer_state)
            print_on_map(answer_state)
            window_title = f"{len(guessed_states)}/50 states correct"

screen.exitonclick()
