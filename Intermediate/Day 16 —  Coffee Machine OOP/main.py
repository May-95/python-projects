# Day 16 -- Coffee Machine OOP

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# create objects from classes
coffee = CoffeeMaker()
menu = Menu()
money = MoneyMachine()

running = True
# coffee machine loop
while running:
    option = menu.get_items()
    customer_choice = input(f"What would you like? ({option}): ")
    if customer_choice == 'off':
        running = False
    elif customer_choice == 'report':
        coffee.report()
        money.report()
    else:
        drink = menu.find_drink(customer_choice)
        if coffee.is_resource_sufficient(drink):
            if money.make_payment(drink.cost):
                coffee.make_coffee(drink)
