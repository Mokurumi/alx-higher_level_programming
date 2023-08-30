#!/usr/bin/python3
"""A class that defines a square"""


class Square:
    """A class that defines a square.

    Private instance attribute:
        _size (number): The size of the square's sides.

    Attributes:
        size (number): The size of the square's sides.

    Raises:
        TypeError: If size is not a number (float or integer).
        ValueError: If size is less than 0.

    Methods:
        area(): Calculate the area of the square.
        __eq__(other): Compare if two squares have equal areas.
        __ne__(other): Compare if two squares have different areas.
        __lt__(other): Compare if the area of the current square
                is less than the area of another square.
        __le__(other): Compare if the area of the current square
                is less than or equal to the area of another square.
        __gt__(other): Compare if the area of the current square
                is greater than the area of another square.
        __ge__(other): Compare if the area of the current square
                is greater than or equal to the area of another square.

    """

    def __init__(self, size=0):
        """Initialize a square with a given size.

        Args:
            size: The size of the square's sides.
                Defaults to 0.
        """
        self.size = size

    @property
    def size(self):
        """Get the size of the square's sides."""
        return self._size

    @size.setter
    def size(self, value):
        """Set the size of the square's sides.

        Args:
            value: The new size value.

        Raises:
            TypeError: If value is not a number (float or integer).
            ValueError: If value is less than 0.
        """
        if not isinstance(value, (float, int)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._size = value

    def area(self):
        """Calculate the area of the square.

        Returns:
            float: The area of the square.
        """
        return self._size ** 2

    def __eq__(self, other):
        """Compare if two squares have equal areas."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Compare if two squares have different areas."""
        return self.area() != other.area()

    def __lt__(self, other):
        """
            Compare if the area of the current square
            is less than the area of another square.
            """
        return self.area() < other.area()

    def __le__(self, other):
        """
            Compare if the area of the current square is less than
            or equal to the area of another square.
            """
        return self.area() <= other.area()

    def __gt__(self, other):
        """
            Compare if the area of the current square
            is greater than the area of another square.
            """
        return self.area() > other.area()

    def __ge__(self, other):
        """
            Compare if the area of the current square is greater than
            or equal to the area of another square.
            """
        return self.area() >= other.area()
