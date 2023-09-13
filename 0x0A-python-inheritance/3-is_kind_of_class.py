#!/usr/bin/python3
'''
module to check object is an instance of,
or is an instance of a class that inherited from
a specified class
'''


def is_kind_of_class(obj, a_class):
    """
    Checks if the object is an instance of,
        or inherited from, the specified class.

    Args:
    obj: The object to be checked.
    a_class: The class to compare the object with.

    Returns:
    bool: True if the object is an instance of the specified classo
        or its subclasses; otherwise, False.
    """
    return isinstance(obj, a_class)
