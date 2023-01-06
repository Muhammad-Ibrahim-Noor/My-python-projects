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


out = True
while out:

    def report(resources_, user_choice_):
        water = resources_['water'] - MENU[user_choice_]['ingredients']['water']
        milk = resources_['milk'] - MENU[user_choice_]['ingredients']['milk']
        coffee = resources_['coffee'] - MENU[user_choice_]['ingredients']['coffee']
        money = resources_["money"] = cost_of_product
        return f"Water: {water}\nMilk: {milk}\nCoffee: {coffee}\nmoney: ${money}"


    user_choice = input("What would you like? (espresso/latte/cappuccino):\n").lower()

    if user_choice == 'latte' or user_choice == 'espresso' or user_choice == 'cappuccino':
        print("Please insert coins")
    elif user_choice == 'report':
        report = user_choice

        print(report)
        # print(report(resources, user_choice__))
    else:
        print("Khabees admi ")
        out = False

    quarter = float(0.25)
    dime = float(0.10)
    nickle = float(0.05)
    penny = float(0.01)
    quarters = float(input("How many quarters?\n")) * quarter
    dimes = float(input("How many dimes?\n")) * dime
    nickles = float(input("How many dimes?\n")) * nickle
    pennies = float(input("How many pennies?\n")) * penny
    total = quarters + dimes + nickles + pennies
    cost_of_product = MENU[user_choice]['cost']
    change = round(total - cost_of_product, 2)

    if cost_of_product > total:
        print("Sorry that's not enough money. Money refunded")
    elif cost_of_product <= total:
        print(f"Here is your change : ${change}")
        print(f"Here is your {user_choice}. Enjoy")
    # print(report(resources, user_choice))

    for items in resources:
        if resources[items] < MENU[user_choice]['ingredients'][items]:
            print(f"Sorry there is not enough {items}")
            out = False
