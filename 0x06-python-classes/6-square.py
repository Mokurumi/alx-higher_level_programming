#!/usr/bin/python3
"""A class that defines a square"""


class Square:

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a square.

        Args:
            size (int, optional): The size of the square. Defaults to 0.
            position (tuple, optional): The position of the square.
                                Defaults to (0, 0).
                                Must be a tuple of 2 positive integers.
        """
        self.size = size
        self.position = position
        
    @property
    def size(self):
        """int: The size of the square."""
        return self.__size
    
    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Args:
            value (int): The new size value.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    
    @property
    def position(self):
        """tuple: The position of the square."""
        return self.__position
    
    @position.setter
    def position(self, value):
        """
        Set the position of the square.

        Args:
            value (tuple): The new position value.
                    Must be a tuple of 2 positive integers.

        Raises:
            TypeError: If value is not a tuple
                    or contains non-integer elements.
            ValueError: If value does not have 2 elements
                    or contains negative values.
        """
        if not isinstance(value, tuple) or len(value) != 2 or \
                not all(isinstance(i, int) for i in value) or \
                not all(i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
    
    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
    
    def my_print(self):
        """
        Print the square using '#' characters and proper positioning.

        If the size is 0, prints an empty line.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
