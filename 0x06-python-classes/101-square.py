#!/usr/bin/python3
"""A class that defines a square"""


class Square:
    """A class that defines a square.

    Private instance attributes:
        _size (int): The size of the square's sides.
        _position (tuple): The position of the square.

    Attributes:
        size (int): The size of the square's sides.
        position (tuple): The position of the square.

    Raises:
        TypeError: If size is not an integer
                or position is not a tuple of 2 positive integers.
        ValueError: If size is less than 0.

    Methods:
        area(): Calculate the area of the square.
        my_print(): Print the square using '#' character.

    """

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a square with a given size and position.

        Args:
            size (int, optional): The size of the square's sides.
                            Defaults to 0.
            position (tuple, optional): The position of the square.
                                    Defaults to (0, 0).
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get the size of the square's sides."""
        return self._size

    @size.setter
    def size(self, value):
        """Set the size of the square's sides.

        Args:
            value (int): The new size value.

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
        """Get the position of the square."""
        return self._position

    @position.setter
    def position(self, value):
        """Set the position of the square.

        Args:
            value (tuple): The new position value.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
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
        """Print the square using '#' character."""
        if self._size == 0:
            print()
            return

        for _ in range(self._position[1]):
            print()

        for _ in range(self._size):
            print(" " * self._position[0] + "#" * self._size)
