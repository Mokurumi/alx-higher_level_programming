#!/usr/bin/python3
'''module for square class'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''square class that inherits from rectangle'''
    def __init__(self, size):
        """
        Initializes a Square object with the specified size.

        Args:
        size (int): The size of the square.

        Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than or equal to 0.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """
        Returns a string representation of the Square object.

        Returns:
        str: A string in the format "[Square] size/size".
        """
        return f"[Square] {self._Rectangle__width}/{self._Rectangle__height}"

