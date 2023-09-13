#!/usr/bin/python3
'''module for rectangle class'''


class BaseGeometry:
    '''Base class'''
    def area(self):
        """
        Raises an Exception with the message "area() is not implemented".
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that the value is an integer greater than 0.

        Args:
        name (str): The name of the value being validated.
        value: The value to be validated.

        Raises:
        TypeError: If the value is not an integer.
        ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


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

    def area(self):
        """
        Calculates and returns the area of the rectangle.

        Returns:
        int: The area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns a string representation of the Rectangle object.

        Returns:
        str: A string in the format "[Rectangle] width/height".
        """
        return f"[Rectangle] {self.__width}/{self.__height}"


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
