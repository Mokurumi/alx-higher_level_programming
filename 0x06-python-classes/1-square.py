#!/usr/bin/python3
"""A class that defines a square"""


class Square:
    """
    Attributes:
        __size (int): The size of the square.

    Args:
        size (int): The size to initialize the square with.
    """

    def __init__(self, size):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size to initialize the square with.
        """
        self.__size = size