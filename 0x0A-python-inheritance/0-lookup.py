#!/usr/bin/python3
'''class with object to list its attributes and properties'''


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Args:
    obj (object): The object to look up attributes and methods for.

    Returns:
    list: A list containing the names of available attributes and methods.
    """
    return [attr for attr in dir(obj) if callable(getattr(obj, attr)) or
            not callable(getattr(obj, attr))]
