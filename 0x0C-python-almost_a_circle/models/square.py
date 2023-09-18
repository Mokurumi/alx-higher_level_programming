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

    # Override the __str__ method to customize the string representation.
    def __str__(self):
        """
        Return a string representation of the square.

        Returns:
            str: A string in the format [Square] (<id>) <x>/<y> - <size>.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
