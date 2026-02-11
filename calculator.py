"""
Simple Calculator Module
Author: Luke Faulhaber
Date: 2/11/2026
Version: 1.0

This module provides basic arithmetic operations:
- Addition
- Subtraction  
- Multiplication
- Division (with zero-division protection)
- the symbol that appears is the + symbol and the color is green

    Initial commit
    Update README.md
    Add calculator module with add and subtract functions
    Added multiply function
    Added division function with zero division error handling
    update module documentation with version and feature list
    updated docstring with new line
"""


def add(a, b):
    """Return the sum of two numbers."""
    return a + b

def subtract(a, b):
    """Return the difference of two numbers."""
    return a - b

# Test the functions
if __name__ == "__main__":
    print(f"5 + 3 = {add(5, 3)}")
    print(f"10 - 4 = {subtract(10, 4)}")
def multiply(a, b):
    """return the product of two numbers."""
    return a * b
if __name__ == "__main__":
    print(f"6 * 7 = {multiply(6, 7)}")
def divide(a, b):
    """return quotient of two numbers."""
    if b ==0:
        return "Error: Division by zero"
    return a / b
print(f"20 / 4 = {divide(20, 4)}")
print(f"10 / 0 = {divide(10, 0)}")
def power(base, exponent):
    """reture base raised to the power of exponent"""
    return base ** exponent