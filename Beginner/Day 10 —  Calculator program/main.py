# Day 10 -- Calculator program
from art import logo

# calculator functions
def add(first_number, second_number):
    return first_number + second_number


def subtract(first_number, second_number):
    return first_number - second_number


def multiply(first_number, second_number):
    return first_number * second_number


def division(first_number, second_number):
    return first_number / second_number

# # function that clears user's console
def clear():
    # mac/linux
    if (os.name == 'posix'):
        os.system('clear')
    # windows
    else:
        os.system('cls')

# calculates total using calculator functions
def calculate(first_number, second_number, operation):
    if operation == "+":
        return add(first_number, second_number)
    elif operation == "-":
        return subtract(first_number, second_number)
    elif operation == "*":
        return multiply(first_number, second_number)
    elif operation == "/":
        return round(division(first_number, second_number), 2)
    # exits program if operation is invalid
    else:
        print("Invalid operation. Start again!")
        return False

# prints finished calculation to user
def finished_calculation(current_total, first_number, second_number, operation):
    print(f"{first_number} {operation} {second_number} = {current_total}")

def operations():
    print("+")
    print("-")
    print("*")
    print("/")

continue_calculation = True
current_total = 0
# calculator loop
while continue_calculation:
    print(logo)
    first_number = int(input("What is the first number: "))
    operations()
    operation = input("Pick an operation: ")
    second_number = int(input("What is the second number: "))
    current_total = calculate(first_number, second_number, operation)
    # inputs to user the finished calculation only if current_total does not equal to False
    if current_total != False:
        finished_calculation(current_total, first_number,
                             second_number, operation)
        continue_on = input(
            f"Type 'y' to continue calculating with the current total: {current_total}. Or type 'n' to start a new calculation: ").lower()
        # user can continue calculating using their current total
        while continue_on == 'y':
            clear()
            print(f"Current total is {current_total}.")
            operations()
            operation = input("Pick another operation: ")
            first_number = current_total
            third_number = int(input("What is the other number: "))
            current_total = calculate(current_total, third_number, operation)
            finished_calculation(current_total, first_number,
                                 third_number, operation)
            if current_total == False:
                continue_on = False
            else:
                continue_on = input(
                    f"Type 'y' to continue calculating with the current total: {current_total}. Or type 'n' to start a new calculation: ").lower()
        # while loop starts again for user to calculate another calculation if they entered 'n'
        if continue_on == 'n':
            continue_calculation = True
            print("\n--------------------------")
            clear()
        else:
            print("Invalid input. Start program again to calculate.")
            continue_calculation = False
