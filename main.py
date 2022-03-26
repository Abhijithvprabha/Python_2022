from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# print report
my_money_machine = MoneyMachine()
my_coffeemaker = CoffeeMaker()
my_menu = Menu()
machine_status = True
while machine_status:
    options = my_menu.get_items()
    choice = input(f"What would you like? {options}: ”")
    if choice == "off":
        machine_status = False
    elif choice == "report":
        my_money_machine.report()
        my_coffeemaker.report()

    else:
        drink = my_menu.find_drink(choice)
        if my_coffeemaker.is_resource_sufficient(drink) and my_money_machine.make_payment(drink.cost):
            my_coffeemaker.make_coffee(drink)
