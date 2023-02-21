# Day 8 -- Caesar Cipher
from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
            'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# encoding/decoding function
def caesar(text, shift, direction):
    end_text = ""
    if direction == "decode":
        shift *= -1
    for char in text:
        if char not in alphabet:
            end_text += char
        else:
            position = alphabet.index(char)
            new_position = position + shift
            end_text += alphabet[new_position]
    print(f"Here's the {direction}d message: {end_text}")


print(logo)
continue_again = True

# program loop
while continue_again:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    while shift >= 26 or shift == 0:
        if shift == 0:
            shift = int(
                input(f"{shift} is too small. Type a shift number that is above 0:\n"))
        else:
            shift = int(
                input(f"{shift} is too large. Type a shift number that is below 26:\n"))

    caesar(text=text, shift=shift, direction=direction)
    answer = input(
        "\nDo you want to use the Caesar Cipher again? Enter 'yes' to continue and 'no' to exit.\n").lower()
    if answer == 'no':
        continue_again = False
    else:
        continue_again = True
