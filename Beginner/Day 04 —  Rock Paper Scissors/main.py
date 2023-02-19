# Day 4 -- Rock Paper Scissors
from time import sleep
import random

# game choices
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
choices = [rock, paper, scissors]

# method deciding the winner
def winner():
    if player_choice == rock and computer_choice == scissors:
        print("You have won!")
    elif player_choice == scissors and computer_choice == paper:
        print("You have won!")
    elif player_choice == paper and computer_choice == rock:
        print("You have won!")
    elif player_choice == computer_choice:
        print("It is a draw!")
    else:
        print("Computer has won!")

# loop running the game
play = True
while play:
    print("Welcome to Rock, Paper, Scissors!")
    sleep(1)
    player_choice = choices[int(
        input("What do you choose?\nType 0 for Rock, 1 for Paper and 2 for Scissors: "))]
    print("You chose: \n" + player_choice)
    computer_choice = choices[random.randint(0, 2)]
    print("Computer chose: \n" + computer_choice)
    winner()
    again = input(
        "\nDo you want to play again? enter 'y' for yes and 'n' for no: ").lower()
    if again == 'y':
        play = True
        print("-----------------------------\n")
    else:
        play = False