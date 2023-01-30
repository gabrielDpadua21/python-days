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

operations = {
    "+": sum_values,
    "-": subtraction_values,
    "*": multiply_values,
    "/": divided_values
}

def get_operation(operator, value1, value2):
    calculator = operations[operator]
    return calculator(value1, value2)
