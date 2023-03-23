# Day 26 -- NATO Alphabet
import pandas

# read csv file and turn it into a DataFrame.
alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")
alphabet_df = pandas.DataFrame(alphabet)
# loop through DataFrame. Adding the data into a dict with the
# letter as the key and the NATO phonetic alphabet as its value.
nato_alphabet = {}
for (index, row) in alphabet_df.iterrows():
    nato_alphabet[row[0]] = row[1]

# welcome message to user.
print("Welcome to the NATO Alphabet program.")
is_on = True
# program loop.
while is_on:
    # user inputs a word.
    word = input("Enter the word: ")
    word_as_nato = []
    # loops through the word and finds each letter's NATO phonetic alphabet and appends it to word_as_nato variable.
    for letter in word.upper():
        if letter in nato_alphabet:
            word_as_nato.append(nato_alphabet[letter])
        else:
            word_as_nato.append(letter)
    # prints to user their word as a NATO phonetic alphabet.
    print(f"Your NATO phonetic alphabet for {word.title()} is {word_as_nato}.")
    # user asked if they want to run program again.
    run_again = input("Do you want to start again? yes or no: ").lower()

    if run_again == "no":
        is_on = False
    else:
        print("-------------------\n")
