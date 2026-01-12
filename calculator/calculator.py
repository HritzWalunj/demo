"""add simple calculator functions"""

def add(a, b):
    """return addition"""
    return a + b


def subtract(a, b):
    """return subtraction"""
    return a - b


def multiply(a, b):
    """return multiplication"""
    return a * b


def divide(a, b):
    """return division"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
