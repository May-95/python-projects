# Day 31 -- Flash Card App
from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

# opens file. If a words_to_learn file already exists, it uses that file.
try:
    data = pandas.read_csv("./data/words_to_learn.csv")
# if it is the first time running the program, it uses the original list of words to learn and saves it as a dict.
except FileNotFoundError:
    original_data = pandas.read_csv("./data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


# if the user knows a word, the word is removed from their list of words to learn and the new updated list is saved.
def is_known():
    to_learn.remove(current_card)
    new_to_learn = pandas.DataFrame(to_learn)
    new_to_learn.to_csv("./data/words_to_learn.csv", index=False)
    next_card()


# flips the card and shows the English translation of the French word.
def flipped_card():
    canvas.itemconfig(word_text, text=f"{current_card['English']}", fill="white")
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(background_image, image=back_img)


# runs the next card in the list of words to learn. There is a 3-second timer and the card is then flipped.
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(background_image, image=front_img)
    canvas.itemconfig(word_text, text=f"{current_card['French']}", fill="black")
    canvas.itemconfig(title_text, text="French", fill="black")
    flip_timer = window.after(3000, flipped_card)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashcard App")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=next_card)
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
front_img = PhotoImage(file="./images/card_front.png")
back_img = PhotoImage(file="./images/card_back.png")
background_image = canvas.create_image(400, 263, image=front_img)
title_text = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# buttons.
right_image = PhotoImage(file="./images/right.png")
known_button = Button(image=right_image, highlightthickness=0, command=is_known)
known_button.grid(column=0, row=1)

wrong_image = PhotoImage(file="./images/wrong.png")
unknown_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
unknown_button.grid(column=1, row=1)

next_card()
window.mainloop()