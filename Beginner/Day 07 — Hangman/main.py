# Day 7 -- Hangman

import random
import hangman_art
import hangman_words

# random word chosen.
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

# game logo.
print(hangman_art.logo)

# generates blanks for chosen word.
display = []
for _ in range(word_length):
    display += "_"

# game loop.
while not end_of_game:
    # user's guess.
    guess = input("Guess a letter: ").lower()
    # checks if user has already guessed the letter. If they have, it lets them know. If they haven't, it checks their guess against the chosen word.
    if guess in display:
        print(f"You have already guessed the letter {guess}. Try again.")
    else:
        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter

    # checks if user is wrong. Deducts 1 life from their lives if wrong. Also checks if they have lives still left. If lives = 0, game ends.
    if guess not in chosen_word:
        print(
            f"You guessed {guess}, that letter is not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You have used up all your lives. You lose!")
    print(f"{' '.join(display)}")

    # checks if user has found all letters in the word. Game ends if all are found.
    if "_" not in display:
        end_of_game = True
        print("You have guessed correctly. You win.")

    # prints hangman stages.
    print(hangman_art.stages[lives])
