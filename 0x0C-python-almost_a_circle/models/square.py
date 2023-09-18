#!/usr/bin/python3
"""
The Square class represents a square with size, position (x, y), and ID.
It inherits from the Rectangle class.
"""


# Import the Rectangle class from models.rectangle
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Attributes:
        id (int): The unique identifier for the square.
        size (int): The size of the square.
        x (int): The x-coordinate of the top-left corner of the square.
        y (int): The y-coordinate of the top-left corner of the square.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a Square object.

        Args:
            size (int): The size of the square.
            x (int, optional):
                The x-coordinate of the top-left corner (default is 0).
            y (int, optional):
                The y-coordinate of the top-left corner (default is 0).
            id (int, optional):
                The unique identifier for the square (default is None).
        """
        # Call the constructor of the Rectangle class with the appropriate args
        super().__init__(size, size, x, y, id)

    # Getter and setter methods for the size attribute.
    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    # Override the __str__ method to customize the string representation.
    def __str__(self):
        """
        Return a string representation of the square.

        Returns:
            str: A string in the format [Square] (<id>) <x>/<y> - <size>.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    # Public method to update the attributes based on provided args or kwargs.
    def update(self, *args, **kwargs):
        """
        Update the attributes of the square based on provided args or kwargs.

        Args:
            *args: Variable number of arguments in the order: id, size, x, y.
            **kwargs: Keyword arguments representing attribute names and values

        Returns:
            None
        """
        if args:
            attrs = ["id", "size", "x", "y"]
            for i, value in enumerate(args):
                setattr(self, attrs[i], value)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
