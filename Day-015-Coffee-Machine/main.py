from typing import cast

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

COINS = {
    "penny": 0.01,
    "nickel": 0.05,
    "dime": 0.10,
    "quarter": 0.25,
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0.0

def prompt_order():
    global money
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if order not in MENU:
        if order == "report":
            display_report(money)
        elif order == "off":
            exit()
        else:
            print("I'm sorry, you didn't enter a valid order.")
    else:
        ingredients = cast(dict[str, int], MENU[order]["ingredients"])
        if check_resources(ingredients):
            price = cast(float, MENU[order]["cost"])
            is_paid, change = prompt_payment(price)

            if is_paid:
                if change != 0.0:
                    print(f"Here is ${change:.2f} in change.")
                make_drink(ingredients)
                print(f"Here is your {order}... Enjoy!")
            else:
                print(f"Sorry that's not enough money. Money refunded: ${change:.2f}.")

def display_report(total_coins: float):
    print("Current resources: ")
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${total_coins:.2f}")

def prompt_payment(drink_price):
    global money
    print("Please insert coins.")

    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))

    total = (
        quarters * COINS["quarter"] +
        dimes * COINS["dime"] +
        nickels * COINS["nickel"] +
        pennies * COINS["penny"]
    )

    if total < drink_price:
        return False, total

    change = round(total - drink_price, 2)
    money += drink_price
    return True, change

def check_resources(ingredients: dict[str, int]) -> bool:
    for resource, amount_needed in ingredients.items():
        if amount_needed > resources[resource]:
            print(f"Sorry, there is not enough {resource}.")
            return False
    return True

def make_drink(drink_name: dict[str, int]):
    for res, amount in drink_name.items():
        resources[res] -= amount

while True:
    prompt_order()