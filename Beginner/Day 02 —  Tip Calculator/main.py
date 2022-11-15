# Day 2 -- Tip Calculator
from time import sleep

print("Welcome to the Tip Calculator!")
print("--------------------")
sleep(0.5)

# user inputs total bill, tip amount and number of people at dinner.
total_bill = float(input("How much is the total bill? "))
tip = float(input("How much do you want to tip? "))
num_of_people = int(input("How many people are in your party? "))

# tip is converted from a percentage into a decimal.
tip = tip / 100 + 1

# each person's share calculated by multiplying the total bill by the tip and dividing it by the number of people. Number rounded to 2 decimal places.
each_person = round((total_bill * tip) / num_of_people, 2)

# tip calculator's calculation is printed to the user.
print(f"Total bill is £{total_bill}. Each person should pay £{each_person}.")