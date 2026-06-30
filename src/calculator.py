# src/calculator.py
# Securepipe Demo application
# A simple calculator to demonstrate secure CI/CD pipeline


def add(a, b):
    """Return the sum of two numbers."""
    return a + b


def subtract(a, b):
    """Return the diffrence of two numbers."""
    return a - b


def multiply(a, b):
    """Return product of two numbers."""
    return a * b


def divide(a, b):
    """Return the result of dividing a by b.
    Raises ValueError if b is zero
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


def square_root(a):
    """Return the square root of a.
    Raises ValueError if a is negative.
    """
    if a < 0:
        raise ValueError("Cannot take square root of a negative number.")
    return a**0.5
