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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_machine_resources_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print("Sorry, no enough ingredients")
            is_enough = False
            return is_enough
        else:
            is_enough = True
            return is_enough


def process_coins():
    print("Please insert coins")
    total = int(input("how many quarters? ")) * 0.25
    total += int(input("how many dimes? ")) * 0.1
    total += int(input("how many nickel? ")) * 0.05
    total += int(input("how many penny? ")) * 0.01
    return total


def is_transaction_success(money_receive, drink_cost):
    if money_receive >= drink_cost:
        global profit
        profit = profit + money_receive
        balance = money_receive - drink_cost
        print(f"here is your {balance} ")
        return True
    else:
        print("not enough money, money refunded")
        return False




def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] = resources[item] - order_ingredients[item]
    print(f"your {drink_name} is ready")





profit = 0
machine_status = True
while machine_status:
    choice = input("What would you like? (espresso/latte/cappuccino): ”")
    if choice == "off":
        machine_status == False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: 5{resources['milk']}l")
        print(f"Coffee:{resources['coffee']} g ")
        print(f"Money: {profit}")
    else:
        drink = MENU[choice]
        if is_machine_resources_sufficient(drink["ingredients"]) == True:
            payment = process_coins()
            if is_transaction_success(payment, drink["cost"]):
                make_coffee(choice,drink["ingredients"])
