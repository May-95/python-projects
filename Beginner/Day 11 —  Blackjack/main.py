# Day 11 -- Blackjack

from art import logo
import random
import math
import os


def clear():
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")


# dealing card function.
def deal_cards(cards, number, player_or_computer):
    dealt_cards = random.choices(cards, k=number)
    player_or_computer.extend(dealt_cards)

# calculates player or computer's score.
def calculate_score(player_or_computer):
    current_score = sum(player_or_computer)
    if current_score == 21:
        return 0
    elif current_score > 21 and 11 in player_or_computer:
        player_or_computer.remove(11)
        player_or_computer.append(1)
        return sum(player_or_computer)
    else:
        return current_score

# compares computer and player's score to determine the winner.
def compare_scores(player_score, computer_score):
    print(
        f"Your final hand: {player_cards}, final score: {21 if player_score == 0 else player_score}"
    )
    print(
        f"Computer's final hand: {computer_cards}, final score: {21 if computer_score == 0 else computer_score}"
    )
    if player_score == computer_score:
        print("It is a draw! 😕")
    elif computer_score == 0:
        print("You lose, computer has a Blackjack 😭")
    elif player_score == 0:
        print("You have a Blackjack, you win! 🎉")
    elif player_score > 21:
        print("You went over. You lose 😭")
    elif computer_score > 21:
        print("Computer has gone over. You win! 🎉")
    else:
        if player_score > computer_score:
            print("You have won, you have the highest score! 🎉")
        else:
            print("Computer has the highest score. You lose 😭")


def play_again():
    play_again = input(
        "Do you want to play another game of Blackjack? Type 'y' or 'n': "
    )
    if play_again == "y":
        player_cards.clear()
        computer_cards.clear()
        clear()
        return False
    else:
        return True


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_cards = []
computer_cards = []
blackjack = False

# game loop
while not blackjack:
    print(logo)
    deal_cards(cards, 2, player_cards)
    deal_cards(cards, 2, computer_cards)
    player_score = calculate_score(player_cards)
    computer_score = calculate_score(computer_cards)
    print(
        f"Your cards: {player_cards}, current score: {21 if player_score == 0 else player_score}"
    )
    print(f"Computer's first card: {computer_cards[0]}")
    if player_score == 0 or player_score > 21:
        compare_scores(player_score, computer_score)
        blackjack = True
    elif computer_score == 0 or computer_score > 21:
        compare_scores(player_score, computer_score)
        blackjack = play_again()
    elif player_score < 21:
        answer = input("Type 'y' to get another card, type 'n' to pass: ")
        if answer == "y":
            while answer == "y":
                deal_cards(cards, 1, player_cards)
                player_score = calculate_score(player_cards)
                if player_score > 21 or player_score == 0:
                    compare_scores(player_score, computer_score)
                    answer = ""
                    blackjack = play_again()
                elif computer_score == 0 or computer_score > 21:
                    compare_scores(player_score, computer_score)
                    answer = ""
                    blackjack = play_again()
                else:
                    print(
                        f"Your cards: {player_cards}, current score: {21 if player_score == 0 else player_score}"
                    )
                    print(f"Computer's first card: {computer_cards[0]}")
                    answer = input(
                        "Type 'y' to get another card, type 'n' to pass: ")
        else:
            deal_cards(cards, 1, computer_cards)
            computer_score = calculate_score(computer_cards)
            while computer_score < 17 and not 0:
                deal_cards(cards, 1, computer_cards)
                computer_score = calculate_score(computer_cards)
            compare_scores(player_score, computer_score)
            blackjack = play_again()
