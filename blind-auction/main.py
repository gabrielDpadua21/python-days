from logo import logo

bidders = {}

def add_bidders(name, value):
    bidders[name] = value;

def calculate_bigger_bid():
    winner = ''
    winner_value = 0
    for name in bidders:
        if winner_value < bidders[name]:
            winner_value = bidders[name]
            winner = name
    print(f"The winner of bid is {winner} with ${winner_value} ")


if __name__ == '__main__':
    logo()
    print("Welcome to the secret auction program")
    while True:
        name = input("What is you name: ")
        value = int(input("What is your bid: $"))
        add_bidders(name, value)
        option = input("Are there any other bidders? Type 'yes' or 'no' ")
        if option != "yes":
            break
    calculate_bigger_bid()



