# Day 27 -- Mile to Kilometers Converter

from tkinter import *

# sets up window.
window = Tk()
window.title("Mile to Kilometers Converter")
window.config(padx=20, pady=20)


# calculates miles into km. Takes user input and updates the miles_to_kilometre text with the calculation.
def miles_to_km():
    inputted_miles = float(user_input.get())
    miles_as_km = round(inputted_miles * 1.609344, 2)
    miles_to_kilometres.config(text=f"{miles_as_km}")


# user inputs the number of miles they want to convert into km.
user_input = Entry(width=10)
user_input.grid(column=1, row=0)

miles = Label(text="miles", font=("Ariel", 20, "bold"))
miles.config(padx=10, pady=10)
miles.grid(column=2, row=0)

equal_to = Label(text="is equal to", font=("Ariel", 20, "bold"))
equal_to.config(padx=10, pady=10)
equal_to.grid(column=0, row=1)

# result of calculation is displayed here.
miles_to_kilometres = Label(text="0", font=("Ariel", 20, "bold"))
miles_to_kilometres.config(padx=10, pady=10)
miles_to_kilometres.grid(column=1, row=1)

kilometres = Label(text="km", font=("Ariel", 20, "bold"))
kilometres.config(padx=10, pady=10)
kilometres.grid(column=2, row=1)

# calculate button which runs the miles_to_km function when pressed.
button = Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=2)

window.mainloop()
