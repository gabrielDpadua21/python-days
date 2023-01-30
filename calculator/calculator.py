

def get_operation(operator, value1, value2):
    if operator == "+":
        return sum_values(value1, value2)
    elif operator == "-":
        return subtraction_values(value1, value2)
    elif operator == "*":
        return multiply_values(value1, value2)
    elif operator == "/":
        return divided_values(value1, value2)
    else:
        print("Invalid input...")
        return False

def sum_values(value1, value2):
    """Sum two values"""
    return value1 + value2

def subtraction_values(value1, value2):
    """Subtraction two values"""
    return value1 - value2

def multiply_values(value1, value2):
    """Multiply two values"""
    return value1 * value2

def divided_values(value1, value2):
    """Divided two numbers"""
    return value1 / value2
