def multiply(a, b):
    """Multiplies two numbers and returns the result."""
    return a * b
def divide(a, b):
    """Divides the first number by the second and returns the result."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b