#!/usr/bin/python3
"""
module to convert class to JSON
"""


def class_to_json(obj):
    """
    Converts an object to a dictionary with serializable data structures
    (list, dictionary, string, integer, and boolean).

    Args:
        obj: An instance of a Class with serializable attributes.

    Returns:
        dict: A dictionary representation of the object with serializable data.
    """
    return obj.__dict__
