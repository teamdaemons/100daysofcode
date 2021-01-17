# TODO: 2 Check resources sufficient to make drink order

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


# TODO: 1 Print report of all the coffee machine resources
def report():
    print(f"Water: {resources['water']} \nMilk: {resources['milk']} \nCoffee: {resources['coffee']}")


def ingredients(choice):
    if choice == "report" or choice == "off":
        return
    else:
        water = MENU[choice]['ingredients']['water']
        coffee = MENU[choice]['ingredients']['coffee']
        try:
            milk = MENU[choice]['ingredients']['milk']
        except KeyError:
            milk = 0
    return [water, coffee, milk]


def collect_coins(cost, choice):
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    total = round((quarters * .25) + (dimes * .1) + (nickles * .05) + (pennies * .01), 2)
    if total < cost:
        print(f"Insufficient funds, dispensing all coins {total}")
        collect_coins(cost, choice)
    else:
        print(f"Total funds received${total}.Here is ${round(total - cost, 2)} in change")
        print(f"Here is your {choice} Enjoy!")
        global money
        money += cost
    return total


option = "on"
money = 0
while option != "off":
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    ing = ingredients(choice)
    if choice == "report":
        report()
        print(f"Money: ${money}")
    elif choice == "off":
        break
    elif ing[0] > resources['water'] or ing[1] > resources['coffee'] or ing[2] > resources['milk']:
        print("Insufficient ingredients")
        choice = "off"
        break
    elif choice == "espresso":
        # 50 ml water 18g Coffee
        #print(MENU[choice])
        cost = float(MENU[choice]['cost'])
        #print(ing, cost)
        resources['water'] -= ing[0]
        resources['coffee'] -= ing[1]
        resources['milk'] -= ing[2]
        report()
        collect_coins(cost, choice)
        print(f"Cost: ${cost}")
    elif choice == "latte":
        # 200 ml water 24g Coffee 150ml Milk
        #print(MENU[choice])
        ing = ingredients(choice)
        cost = MENU[choice]['cost']
        #print(ing, cost)
        resources['water'] -= ing[0]
        resources['coffee'] -= ing[1]
        resources['milk'] -= ing[2]
        report()
        collect_coins(cost, choice)
        print(f"Cost: ${cost}")
    elif choice == "cappuccino":
        # 250 ml water 24g Coffee 100ml Milk
        #print(MENU[choice])
        ing = ingredients(choice)
        cost = MENU[choice]['cost']
        #print(ing, cost)
        resources['water'] -= ing[0]
        resources['coffee'] -= ing[1]
        resources['milk'] -= ing[2]
        report()
        print(f"Cost: ${cost}")

