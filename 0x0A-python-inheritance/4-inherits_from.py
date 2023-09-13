#!/usr/bin/python3
'''
module to check if the object is an instance of a class
that inherited (directly or indirectly) from the specified class
'''


def inherits_from(obj, a_class):
    """
    Args:
    obj: The object to be checked.
    a_class: The class to compare the object with.

    Returns:
    bool:
        True if the object is an instance of a subclass of the specified class;
        otherwise, False.
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
