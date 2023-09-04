#!/usr/bin/python3
"""A class that defines a rectangle."""


class Rectangle:
    """
    This class defines a rectangle with width and height attributes.
    """

    # Class attribute to track the number of instances
    number_of_instances = 0
    # Class attribute for the symbol used in string representation
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle instance with optional width and height.

        Args:
            width (int): The width of the rectangle (default is 0).
            height (int): The height of the rectangle (default is 0).
        """
        self.width = width
        self.height = height
        # Increment the number of instances
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Getter method for width.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for width.

        Args:
            value (int): The width to set.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        Getter method for height.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for height.

        Args:
            value (int): The height to set.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Returns a string representation of the rectangle with the print_symbol.

        Returns:
                str: The string representation of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
                return ""
        if isinstance(self.print_symbol, str):
                symbol = self.print_symbol
        else:
                symbol = str(self.print_symbol)

        rectangle_str = ""
        for i in range(self.__height):
                rectangle_str += symbol * self.__width
                if i < self.__height - 1:
                        rectangle_str += '\n'
        return rectangle_str

    def __repr__(self):
        """
        Returns a string representation of the rectangle
            for recreation using eval().

        Returns:
            str: A string that can recreate the instance using eval().
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
        Destructor method for Rectangle instances.

        Prints a message when an instance of Rectangle is deleted.
        Decrements the number of instances.
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")