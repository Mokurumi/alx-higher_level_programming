#!/usr/bin/python3
"""
The Rectangle class represents a rectangle with width, height,
and position (x, y).
It inherits from the Base class for ID management.
"""


# Import the Base class from models.base
from models.base import Base


class Rectangle(Base):
    """
    Attributes:
        id (int): The unique identifier for the rectangle.
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        x (int): The x-coordinate of the top-left corner of the rectangle.
        y (int): The y-coordinate of the top-left corner of the rectangle.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a Rectangle object.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional):
                The x-coordinate of the top-left corner (default is 0).
            y (int, optional):
                The y-coordinate of the top-left corner (default is 0).
            id (int, optional):
                The unique identifier for the rectangle (default is None).
        """
        # Call the constructor of the Base class to handle the 'id' attribute.
        super().__init__(id)

        # Set the private instance attributes with their respective values.
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    # Getter and setter methods for the width attribute.
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError("Width must be greater than 0")
        self.__width = value

    # Getter and setter methods for the height attribute.
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError("Height must be greater than 0")
        self.__height = value

    # Getter and setter methods for the x attribute.
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if value < 0:
            raise ValueError("X coordinate must be non-negative")
        self.__x = value

    # Getter and setter methods for the y attribute.
    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if value < 0:
            raise ValueError("Y coordinate must be non-negative")
        self.__y = value
