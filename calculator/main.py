
from calculator import get_operation
from logo import banner

def print_operations():
    print("+")
    print("-")
    print("*")
    print("/")

def get_chose(result):
    chose = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation, or any key to exit: ")
    return chose;

def chosen(chose, result=0):
    if chose == "y":
        second_calculation(result)
    elif chose == "n":
        first_calculation()
    else:
        print("Bye")
        return

def first_calculation():
    first_value = float(input("What's the first number?: "))
    print_operations()
    operation = input("Pick on operation: ")
    second_value = float(input("What's the second number?: "))
    result = get_operation(operation, first_value, second_value)
    print(f"Result of {first_value} {operation} {second_value} = {result}")
    chose = get_chose(result)
    chosen(chose, result)
    
    
def second_calculation(result):
    print_operations()
    operation = input("Pick on operation: ")
    second_value = float(input("What's the second number?: "))
    result2 = get_operation(operation, result, second_value)
    print(f"Result of {result} {operation} {second_value} = {result2}")
    chose = get_chose(result)
    chosen(chose)


if __name__ == "__main__":
    banner()
    first_calculation()
