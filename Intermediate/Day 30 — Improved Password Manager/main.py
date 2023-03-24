# Day 29 -- Password Manager
from tkinter import *
from tkinter import messagebox
from random import choice, shuffle
import pyperclip
import json


# ---------------------------- SEARCH FOR PASSWORD ------------------------------- #
# search through password manager to find the details for a website.
def search_password():
    # get the website the user is trying to search for.
    search_website = website_entry.get().lower()
    try:
        # try loading the json file.
        with open("password_manager.json", mode="r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        # if json file is not found, error message displayed to user.
        messagebox.showinfo(title="Error", message="No data file found.")
    else:
        # if json file is found, searches for the website in the data. If there is a match, the email details and
        # password for that website is displayed to user.
        if search_website in data:
            messagebox.showinfo(title=search_website.title(), message=f"Email: {data[search_website]['email']} "
                                                                      f"\nPassword: {data[search_website]['password']}")
        # if website is not in password manager, error message is displayed to user telling them details do not exist.
        else:
            messagebox.showinfo(title="Error", message="No details for the website exists.")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# generates complex password that is 15 characters long. Clears the password field to make sure there is nothing there
# before inserting the new generated password. Modified day 5 password generator program.
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    generated_password = []

    if not generated_password:
        for letter in range(0, 5):
            generated_password.append(choice(letters))
        for symbol in range(0, 5):
            generated_password.append(choice(symbols))
        for number in range(0, 5):
            generated_password.append(choice(numbers))
        shuffle(generated_password)
        generated_password = "".join(generated_password)
        password_entry.delete(0, END)
        password_entry.insert(0, generated_password)
        # saves the generated password into the user's clipboard.
        pyperclip.copy(generated_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
# saves user's inputted website, email and password into a txt file. User asked if they are happy with the details they
# have entered. Upon confirmation, details are saved and each entry is saved onto a new line. Error message shown if any
# fields are left empty.
def save():
    saved_website = website_entry.get().lower()
    saved_email = email_username_entry.get()
    saved_password = password_entry.get()
    new_data = {
        saved_website: {
            "email": saved_email,
            "password": saved_password,
        }
    }
    if saved_website != "" and saved_email != "" and saved_password != "":
        try:
            # try loading json data if it exists.
            with open("password_manager.json", mode="r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            # if there is no json data file, we create a new json file with the current details.
            with open("password_manager.json", mode="w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # if json file does exist, we update the data and write it into the json file.
            data.update(new_data)
            with open("password_manager.json", mode="w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            # password and website fields are cleared.
            website_entry.delete(0, END)
            password_entry.delete(0, END)
    else:
        messagebox.showwarning(title="Oops", message="Please fill in all empty fields.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(pady=20, padx=20)
canvas = Canvas(width=200, height=200, highlightthickness=0)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)

website = Label(text="Website:", font=("Ariel", 16))
website.config(padx=5, pady=5)
website.grid(column=0, row=1)

# website input, user inputs the name of the website that the details belong to.
website_entry = Entry(width=21)
website_entry.grid(column=1, row=1, columnspan=1)
website_entry.focus()

search = Button(text="Search", width=12, command=search_password)
search.grid(column=2, row=1)

email_username = Label(text="Email/Username:", font=("Ariel", 16))
email_username.config(padx=5, pady=5)
email_username.grid(column=0, row=2)

# email input, pre-populated with an email but user can change it.
email_username_entry = Entry(width=37)
email_username_entry.grid(column=1, row=2, columnspan=2)
email_username_entry.insert(0, "example@email.com")

password = Label(text="Password:", font=("Ariel", 16))
password.config(padx=5, pady=5)
password.grid(column=0, row=3)

# password input, user inputs their own password, or they can press the generate button which fills in the password
# input field with a complex 15 character long password.
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

generate_password = Button(text="Generate Password", width=12, command=password_generator)
generate_password.grid(column=2, row=3)

# add button which asks user for confirmation of their details and saves the details in a txt file.
add_button = Button(text="Add", width=35, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()