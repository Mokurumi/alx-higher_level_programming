#!/usr/bin/python3
"""
A class with no class or object attribute
dynamically created instance attributes
"""


class LockedClass():
    """
    User cannot create any new instance attribute dynamically
    unless attribute is "first_name"
    """

    __slots__ = "first_name"
