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


def make_coffee(coffee):
    pass


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
    OPTIONS['report']()