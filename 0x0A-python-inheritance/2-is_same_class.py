#!/usr/bin/python3
'''module to check type class'''


def is_same_class(obj, a_class):
    """
    Checks if the object is exactly an instance of the specified class.

    Args:
    obj: The object to be checked.
    a_class: The class to compare the object with.

    Returns:
    bool: True if the object is an instance of the specified class;
    otherwise, False.
    """
    return type(obj) is a_class
