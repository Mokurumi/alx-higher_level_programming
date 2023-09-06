#!/usr/bin/python3
def add_integer(a, b="98"):
    """
    Adds two numbers, allowing for integers, floats,
        or strings representing numbers as input.

    Args:
        a: The first number (integer, float, or string).
        b: The second number (integer, float, or string). Default is "98".

    Returns:
        int: The addition of the two numbers, cast to an integer.

    Raises:
        TypeError: If a or b is not an integer, float,
            or a string representing a number.

    Example usage:
        result = add_integer(5, 3.5)
        print(result)  # Output: 8
    """
    # Check if a and b are integers, floats, or strings representing numbers
    if not isinstance(a, (int, float)) and not (isinstance(a, str) \
            and a.isdigit()) and not isinstance(b, (int, float)) \
            and not (isinstance(b, str) and b.isdigit()):
        raise TypeError("a must be an integer or b must be an integer")
        
    # Cast a and b to integers if they are strings
    if isinstance(a, str):
        a = int(a)
    if isinstance(b, str):
        b = int(b)

    # Return the addition of a and b as an integer
    return int(a + b)
