from calculator import tip

if __name__ == '__main__':
    print("Welcome to the tip calculator")
    bill = input("What was the total bill? $")
    split = input("Who manu people to split the bill? ")
    percentage = input("What percentage tip would you like to give? 10, 12, or 15? ")
    result = tip(float(bill), int(split), int(percentage))
    result = "{:.2f}".format(result)
    print(f"Each person should pay: ${result}")


