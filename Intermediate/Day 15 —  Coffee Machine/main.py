# Day 15 -- Coffee Machine
from resource import MENU, resources


# prints out the amount of ingredients in stock
def report(water_balance, milk_balance, coffee_balance, money_balance):
    print(f"Water: {water_balance}ml.")
    print(f"Milk: {milk_balance}ml.")
    print(f"Coffee: {coffee_balance}g.")
    print(f"Money: ${money_balance}.")


# checks if there are enough ingredients for the customer's beverage
def check_resource(beverage_choice):
    drink = MENU[beverage_choice]['ingredients']
    for item in drink:
        if drink[item] > resources[item]:
            print(f"Sorry, there is not enough {item} to make the {beverage_choice}.")
            return False
    return True


# checks if customer has put enough money for their beverage
def coin_check(beverage_choice):
    quarters = int(input("Please insert coins.\nhow many quarters?:")) * 0.01
    dimes = int(input("How many dimes?:")) * 0.05
    nickels = int(input("How many nickels?:")) * 0.10
    pennies = int(input("How many pennies?:")) * 0.25
    total = round(quarters + dimes + nickels + pennies, 2)
    change = round(total - MENU[beverage_choice]['cost'], 2)
    if change < 0:
        print(
            f"Sorry, ${total} is not enough money. A {beverage_choice} is ${MENU[beverage_choice]['cost']}. Money refunded.")
        return False
    else:
        print(f"Here is ${change} dollars in change.")
        return True


# makes the customer's coffee if they have enough money. Deducts the amount of ingredients used from stock total
def make_coffee(beverage_choice):
    global profit
    match beverage_choice:
        case "espresso":
            resources['water'] -= MENU[beverage_choice]['ingredients']['water']
            resources['coffee'] -= MENU[beverage_choice]['ingredients']['coffee']
            profit += MENU[beverage_choice]['cost']
        case "latte" | "cappuccino":
            resources['water'] -= MENU[beverage_choice]['ingredients']['water']
            resources['coffee'] -= MENU[beverage_choice]['ingredients']['coffee']
            resources['milk'] -= MENU[beverage_choice]['ingredients'][
                'milk']
            profit += MENU[beverage_choice]['cost']


profit = 0
running = True

# coffee machine loop
print("Welcome to the Coffee Machine!")
while running:
    beverage = input("What would you like? (espresso/latte/cappuccino): ").lower()
    match beverage:
        case "espresso" | "latte" | "cappuccino":
            check = check_resource(beverage)
            if check:
                running = coin_check(beverage)
                if running:
                    make_coffee(beverage)
                    print(f"Here is your {beverage} ☕️ Enjoy!")
                    print("--------------")
                    answer_again = input("Do you want to use the Coffee Machine again? Type 'y' or 'n': ").lower()
                    if answer_again == 'y':
                        running = True
                    else:
                        running = False
        case "report":
            report(resources['water'], resources['milk'], resources['coffee'], profit)
        case "off":
            running = False
