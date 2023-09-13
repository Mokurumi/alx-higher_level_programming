#!/usr/bin/python3
'''module for rectangle class'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''rectangle class that inherits from BaseGeometry'''
    def __init__(self, width, height):
        """
        Initializes a Rectangle object with the specified width and height.

        Args:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.

        Raises:
        TypeError: If width or height is not an integer.
        ValueError: If width or height is less than or equal to 0.
        """
        # Initialize as 0, will be set through integer_validator
        self.__width = 0
        # Initialize as 0, will be set through integer_validator
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """
        Returns a string representation of the Rectangle object.

        Returns:
        str: A string in the format "[Rectangle] width/height".
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
