#!/usr/bin/python3
"""A class that defines a square"""


class Square:
    """A class that represents a square.

    Attributes:
        size: The size of the square's sides.
        position: The position of the top-left corner of the square.

    """

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a Square instance.

        Args:
            size: The size of the square's sides. Defaults to 0.
            position: The position of the top-left corner of the square.
                   Defaults to (0, 0).

        Raises:
            TypeError: If size is not an integer,
                  or if position is not a tuple of two positive integers.
            ValueError: If size is negative.

        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """int: The size of the square's sides."""
        return self._size

    @size.setter
    def size(self, value):
        """Set the size of the square's sides.

        Args:
            value (int): The size to set.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is negative.

        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._size = value

    @property
    def position(self):
        """tuple: The position of the top-left corner of the square."""
        return self._position

    @position.setter
    def position(self, value):
        """Set the position of the square's top-left corner.

        Args:
            value (tuple): The position to set.

        Raises:
            TypeError: If value is not a tuple of two positive integers.

        """
        if not isinstance(value, tuple) or len(value) != 2 or \
                not all(isinstance(num, int) and num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self._position = value

    def area(self):
        """Calculate the area of the square.

        Returns:
            int: The area of the square.

        """
        return self._size ** 2

    def my_print(self):
        """Print a representation of the square.

        If size is 0, prints an empty line.
        Otherwise, prints a square with '#' characters.

        """
        if self._size == 0:
            print()
            return

        for _ in range(self._position[1]):
            print()

        for _ in range(self._size):
            print(" " * self._position[0] + "#" * self._size)

    def __str__(self):
        """Get a string representation of the square.

        Returns:
                str: A string representation of the square,
                   or an empty string if no visual representation.

        """
        if self._size == 0 or self._position[0] < 0 or self._position[1] < 0:
                return ""

        square_str = ""
        for _ in range(self._size):
                square_str += " " * self._position[0] + "#" * self._size + "\n"

        return square_str[:-1]
