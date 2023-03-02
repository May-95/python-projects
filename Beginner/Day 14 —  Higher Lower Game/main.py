# Day 14 -- Higher Lower Game
import random
import os
from art import logo, vs
from game_data import data


# function to check if description starts with vowel.
def check_vowel(text):
    if text.startswith('A'):
        return True
    elif text.startswith('E'):
        return True
    elif text.startswith('I'):
        return True
    elif text.startswith('O'):
        return True
    elif text.startswith('U'):
        return True
    else:
        return False

# function to check which account has the higher follower count.
def higher():
    if random_choice[0]['follower_count'] > random_choice[1]['follower_count']:
        return 'a'
    else:
        return 'b'

# function to clear screen and print logo.
def clear():
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")
    print(logo)

print(logo)
current_score = 0
continue_game = True

while continue_game:
    # generate two random accounts to compare.
    random_choice = random.choices(data, k=2)
    # check if description starts with vowel/consonant so the description reads correctly.
    vowel_check1 = check_vowel(random_choice[0]['description'])
    vowel_check2 = check_vowel(random_choice[1]['description'])
    # compare A against B
    print(
        f"Compare A: {random_choice[0]['name']}, {'an' if vowel_check1 else 'a'} {random_choice[0]['description']}, from {random_choice[0]['country']}.")
    print(vs)
    print(
        f"Against B: {random_choice[1]['name']}, {'an' if vowel_check2 else 'a'} {random_choice[1]['description']}, from {random_choice[1]['country']}.")
    # user's answer
    answer = input("Who has more followers? Type 'A' or 'B': ").lower()
    # checks which account has the higher follower count
    is_higher = higher()
    if is_higher == answer:
        current_score += 1
        clear()
        print(f"You're right! Current score: {current_score}.")
    else:
        clear()
        print(f"Sorry, that's wrong. Final score: {current_score}.")
        print("-----------------------------")
        answer = input("Do you want to play again? Type 'y' or 'n': ").lower()
        if answer == 'y':
            clear()
            current_score = 0
        else:
            continue_game = False
