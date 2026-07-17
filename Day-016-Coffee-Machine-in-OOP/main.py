"""
Instructions:
The goal is to refactor the program for a coffee machine to an OOP format using the provided classes.

Program Requirements
The PDF for the program requirements is Coffee_Machine_Program_Requirements.pdf
"""

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def prompt_order():
    menu = Menu()
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()

    order = input(f"What would you like? ({menu.get_items()}): ").lower()
    if order not in menu:
        if order == "report":
            coffee_maker.report()
            money_machine.report()
        elif order == "off":
            exit()
        else:
            print("I'm sorry, you didn't enter a valid order.")
    else:
        menu_item = menu.find_drink(order)
        if coffee_maker.is_resource_sufficient(menu_item.ingredients):
            if money_machine.make_payment(menu_item.cost):
                coffee_maker.make_coffee(menu_item)


while True:
    prompt_order()

