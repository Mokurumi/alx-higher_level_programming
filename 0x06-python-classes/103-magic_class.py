#!/usr/bin/python3
"""this is a magic class"""
import math



class MagicClass:
    """A class that demonstrates the use of bytecode operations.

    This class provides methods to calculate the area and circumference of a circle.

    Attributes:
        __radius (float): The radius of the circle.

    Methods:
        __init__(self, radius): Initialize the MagicClass instance with a radius value.
        area(self): Calculate the area of the circle.
        circumference(self): Calculate the circumference of the circle.
    """

    def __init__(self, radius):
        """Initialize a MagicClass instance with a given radius.

        Args:
            radius (int or float): The radius of the circle.

        Raises:
            TypeError: If radius is not a number.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """Calculate the area of the circle.

        Returns:
            float: The calculated area of the circle.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Calculate the circumference of the circle.

        Returns:
            float: The calculated circumference of the circle.
        """
        return 2 * math.pi * self.__radius
