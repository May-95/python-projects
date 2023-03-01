# Day 12 -- Number Guessing Game
import random
from time import sleep
from art import logo
import os

def clear():
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")

# game loop
def number_guessing(lives):
    random_number = random.randint(1, 100)
    lives = lives
    while lives != 0:
        print(
            f"You have {lives} attempt{'s' if lives > 1 else ''} remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if random_number == guess:
            lives = 0
            print(f"You've guessed the number correctly -- {random_number} 😃")
        elif guess < random_number:
            print(f"{guess} is too low. \n{'Guess again.' if lives > 1 else ''}")
            lives -= 1
        elif guess > random_number:
            print(f"{guess} is too high. \n{'Guess again.' if lives > 1 else ''}")
            lives -= 1
        else:
            print("error")
    if lives == 0 and guess != random_number:
        print("You've run out of guesses. You lose 😭")
        return False
    elif lives == 0 and guess == random_number:
        return False

print(logo)
print("Welcome to the Number Guessing Game!")
sleep(1)
play_again = True
while play_again:
    print("Thinking of a number between 1 and 100.")
    answer = input("Choose a difficulty, type 'easy' or 'hard': \n").lower()
    running = True
    while running:
        if answer == 'easy':
            running = number_guessing(10)
        elif answer == 'hard':
            running = number_guessing(5)
        else:
            print("Error has occured, Restart game.")
    go_again = input("Do you want to play again? Type 'y' or 'n': \n").lower()
    if go_again == 'y':
        print("-----------------------------------")
        clear()
        play_again = True
    else:
        play_again = False
