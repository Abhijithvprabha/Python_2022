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
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_enough(order_ingredients):
    """return true if order can be processed , false if not"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            is_enough = False
            return is_enough
        else:
            is_enough = True
            return is_enough


def process_coins():
    """returns the total calculated from coins inserted"""
    print("Please insert coins")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def is_transaction_success(money_received, drink_cost):
    """return True when payment accepted and false is money is not enough"""
    if money_received >= drink_cost:
        global profit
        profit += drink_cost
        change = round(money_received - drink_cost, 2)
        print(f"Here is your balance {change}")
        return True
    else:
        print("Sorry, that's not enough money, money refunded")
        return False


def make_coffee(drink_name, order_ingredients):
    """deduct required ingredients from resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕")


# TODO: Prompt user by asking “What would you like? (espresso/latte/cappuccino):”

machine_status = True
while machine_status == True:
    choice = input("What would you like? (espresso/latte/cappuccino):").lower()

    # TODO: Turn off the Coffee Machine by entering “off” to the prompt.
    if choice == "off":
        machine_status = False
    # TODO: Print report.
    elif choice == "report":
        print(f"Water:{resources['water']} ml")
        print(f"Milk: {resources['milk']} ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: {profit}")

    else:
        drink = MENU[choice]
        if is_resource_enough(drink["ingredients"]) == True:
            payment = process_coins()
            is_transaction_success(payment, drink["cost"])
            make_coffee(choice, drink["ingredients"])
