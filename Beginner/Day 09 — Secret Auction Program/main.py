# Day 9 -- Secret Auction Program
from art import logo
import os

# function that clears user's console to hide previous bidder's details.
def clear():
    # mac/linux
    if (os.name == 'posix'):
        os.system('clear')
    # windows
    else:
        os.system('cls')

# winner function
def winner():
    print(f"The winner is {highest_bid[0]} with a bid of £{highest_bid[1]}.")

def secret_auction(name, bid, highest_bid, total_bids):
    total_bids[name] = bid
    for key, value in total_bids.items():
        if int(value) > int(highest_bid[1]):
            highest_bid[0] = key
            highest_bid[1] = value
    return highest_bid

print(logo)
print("Welcome to the secret auction program.")
add_another = True
highest_bid = ["", 0]
total_bids = {}
while add_another:
    name = str(input("What is your name?:\n")).title()
    bid = str(input("What's your bid:\n£"))
    highest_bid = secret_auction(name, bid, highest_bid, total_bids)
    other_bids = input(
        "Are there any other bidders? Type 'yes' or 'no'").lower()
    if other_bids == 'yes':
        add_another = True
        clear()
    elif other_bids == 'no':
        add_another = False
        winner()
    # handles invalid inputs.
    else:
        error = True
        while error:
            other_bids = input(
                "Invalid input. Try again. Are there any other bidders? Type 'yes' or 'no'").lower()
            if other_bids == 'yes':
                error = False
                clear()
            if other_bids == 'no':
                error = False
                add_another = False
                winner()
