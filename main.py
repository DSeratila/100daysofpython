# import random
import subprocess


def clear():
    subprocess.call("clear")


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

# resources = {
#     "water": 0,
#     "milk": 0,
#     "coffee": 0,
# }

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

bank = 0.00


def report():
    print(f"Water: {resources['water']}\nMilk: {resources['milk']}\nCoffee: {resources['coffee']}\nMoney: ${bank}")


def enough_resources(ordered_drink):
    recipe_ingridients = MENU[ordered_drink]["ingredients"]
    missing_ingrediends = []

    if ordered_drink in MENU.keys():
        for ingredient_name in recipe_ingridients:
            if resources[ingredient_name] < recipe_ingridients[ingredient_name]:
                missing_ingrediends.append(ingredient_name)

        if len(missing_ingrediends) > 0:
            return "Sorry there is not enough ingredients: " + ','.join(missing_ingrediends)

    return ""


def sum_coins(quarters: int, dimes: int, nickles: int, pennies: int):
    return quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.1


def deduct_resources(ordered_drink):
    for resource in MENU[ordered_drink]["ingredients"]:
        resources[resource] = resources[resource] - MENU[ordered_drink]["ingredients"][resource]


while True:
    user_input = input("What would you like? (espresso/latte/cappuccino):")
    if user_input == "report":
        report()
    elif user_input == "off":
        quit()
    elif user_input in MENU.keys():
        missing_ingredients = enough_resources(user_input)
        if missing_ingredients == "":
            print("Please insert coins.")
            quarters = int(input("how many quarters?: "))
            dimes = int(input("how many dimes?: "))
            nickles = int(input("how many nickles?: "))
            pennies = int(input("how many pennies?: "))

            user_money = sum_coins(quarters, dimes, nickles, pennies)
            change = user_money - MENU[user_input]["cost"]

            if change < 0:
                print("Sorry that's not enough money. Money refunded.")

            deduct_resources(user_input)
            print(f"Here's ${change} in change.")
            print(f"Here is your {user_input}")
            bank += user_money - change
        else:
            print(missing_ingredients)
    else:
        quit()

