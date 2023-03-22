# Day 24 -- Mail Merge
PLACEHOLDER = "[name]"

# open list of names file. Read file and store names in a variable.
with open("./Input/Names/invited_names.txt") as list_of_names:
    names = list_of_names.readlines()

# open letter template and save contents in a variable.
with open("./Input/Letters/starting_letter.txt") as letter:
    letter_content = letter.read()
    # for each name in our list of names, we strip the extra spaces and replace the placeholder "[name]"
    # with the actual name of the letter recipient.
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_content.replace(PLACEHOLDER, stripped_name)
        print(new_letter)
        # write the new letter into a new file for each person in the list.
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as finished_letter:
            finished_letter.write(new_letter)
