#!/usr/bin/python3
"""A class that defines a square"""


class Square:
    """A class that defines a square.

    Private instance attributes:
        _size: The size of the square's sides.
        _position: The position of the square.

    Attributes:
        size: The size of the square's sides.
        position: The position of the square.

    Raises:
        TypeError: If size is not an integer
               or if position is not a tuple of 2 positive integers.
        ValueError: If size is less than 0.

    Methods:
        area(): Calculate the area of the square.
        my_print(): Print the square using '#' characters.
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a square with size and position.

        Args:
            size: The size of the square's sides. Defaults to 0.
            position: The position of the square. Defaults to (0, 0).
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get the size of the square's sides.

        Returns:
            int: The size of the square's sides.
        """
        return self._size

    @size.setter
    def size(self, value):
        """Set the size of the square's sides.

        Args:
            value: The new size value.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._size = value

    @property
    def position(self):
        """Get the position of the square.

        Returns:
            tuple: The position of the square.
        """
        return self._position

    @position.setter
    def position(self, value):
        """Set the position of the square.

        Args:
            value: The new position value.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        if not isinstance(value, tuple) or len(value) != 2 or \
           not all(isinstance(val, int) and val >= 0 for val in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self._position = value

    def area(self):
        """Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self._size ** 2

    def my_print(self):
        """Print the square using '#' characters."""
        if self._size == 0:
            print()
            return

        for _ in range(self._position[1]):
            print()
        for _ in range(self._size):
            print(" " * self._position[0] + "#" * self._size)
