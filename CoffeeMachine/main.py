from data import MENU, COINS

resources = {
    "water": {
        "total": 300,
        "prefix": "ml"
    },
    "milk": {
        "total": 200,
        "prefix": "ml"
    },
    "coffee": {
        "total": 100,
        "prefix": "g"
    },
    "money": {
        "total": 0,
        "prefix": "$"
    }
}


def get_money():
    quarters = int(input("How manu quarters do you have? ")) * COINS['quarters']
    dimes = int(input("How manu dimes do you have? ")) * COINS['dimes']
    nickles = int(input("How manu nicker do you have? ")) * COINS['nickles']
    pennies = int(input("How manu pennies do you have? ")) * COINS['pennies']
    return quarters + dimes + nickles + pennies


def recalculate_resources(coffee, money):
    resources['water']['total'] -= coffee['ingredients']['water']
    if 'milk' in coffee['ingredients']:
        resources['milk']['total'] -= coffee['ingredients']['milk']
    resources['coffee']['total'] -= coffee['ingredients']['coffee']
    resources['money']['total'] += money


def calculate_resources(coffee):
    if resources['water']['total'] < coffee['ingredients']['water']:
        return False
    if resources['coffee']['total'] < coffee['ingredients']['coffee']:
        return False
    if 'milk' in coffee['ingredients'] and resources['milk']['total'] < coffee['ingredients']['milk']:
        return False
    return True


def make_coffee(coffee):
    coffee_selected = MENU[coffee]
    total = get_money()
    if not calculate_resources(coffee_selected):
        print("The machine dont have the resources to make this coffee")
    elif coffee_selected['cost'] < total:
        print(f'Enjoy your coffee: {coffee}')
        change = round((total - coffee_selected["cost"]), 2)
        if change > 0:
            print(f"There is your change: {change}")
        recalculate_resources(coffee_selected, total)
    else:
        print(f'The coffee select cost {coffee_selected["cost"]} do you have {total}')
        print('The money refunded')
        print('Bye')



def report_machine():
    print("REPORT")
    for resource in resources:
        total = resources[resource]["total"]
        prefix = resources[resource]["prefix"]
        print(f'{resource} - {total} {prefix} ')


OPTIONS = {
    "espresso": make_coffee,
    "latte": make_coffee,
    "cappuccino": make_coffee,
    "report": report_machine
}


if __name__ == "__main__":
    print("Coffee Machine")
    while True:
        option = input("Do you want make a coffee? type espresso/latte/cappuccino ")
        if option != 'report':
            OPTIONS[option](option)
        else:
            OPTIONS[option]()