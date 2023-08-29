#!/usr/bin/python3
"""A class that defines a square"""


class Square:
    """
    Represents a square.

    Attributes:
        __size (int): The size of the square's sides.

    Methods:
        __init__(self, size=0): Initializes a new Square instance.
        size(self): Getter for the size attribute.
        size(self, value): Setter for the size attribute.
        area(self): Calculates the area of the square.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
    """
    def __init__(self, size=0):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the square's sides. Default is 0.
        """
        self.size = size
        
    @property
    def size(self):
        """
        Getter for the size attribute.

        Returns:
            int: The current size of the square's sides.
        """
        return self.__size
    
    @size.setter
    def size(self, value):
        """
        Setter for the size attribute.

        Args:
            value (int): The new size value for the square's sides.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    
    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2