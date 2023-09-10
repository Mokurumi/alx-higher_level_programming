#!/usr/bin/python3
"""add integer module that takes in floats and integers"""


def add_integer(a, b=98):
    """
    Adds two numbers, allowing for integers and floats as input.

    Args:
        a: The first number (integer or float).
        b: The second number (integer or float). Default is "98".

    Returns:
        int: The addition of the two numbers, cast to an integer.

    Raises:
        TypeError: If a or b is not an integer, float,
            or a string representing a number.

    Example usage:
        result = add_integer(5, 3.5)
        print(result)  # Output: 8
    """
    # Check if a and b are integers or floats
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # Return the addition of a and b as an integer
    return int(a + b)
