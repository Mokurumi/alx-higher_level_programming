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
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    # Getter and setter methods for the height attribute.
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    # Getter and setter methods for the x attribute.
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    # Getter and setter methods for the y attribute.
    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    # Public method to calculate and return the area of the rectangle.
    def area(self):
        """
        Calculate and return the area of the rectangle.

        Returns:
            int: The area value.
        """
        return self.width * self.height

    # Public method to display the rectangle with correct positioning.
    def display(self):
        """
        Display the rectangle by printing it to stdout with '#' characters,
        considering the position (x, y).

        Returns:
            None
        """
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(' ' * self.x + '#' * self.width)

    # Override the __str__ method to customize the string representation.
    def __str__(self):
        """
        Return a string representation of the rectangle.

        Returns:
            str: A string in the format [Rectangle]
              (<id>) <x>/<y> - <width>/<height>.
        """
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - "\
               f"{self.width}/{self.height}"

    # Public method to update the attributes based on provided arguments.
    def update(self, *args):
        """
        Update the attributes of the rectangle based on provided arguments.

        Args:
            *args: Variable number of arguments in the order:
                id, width, height, x, y.

        Returns:
            None
        """
        if len(args) >= 1:
            self.id = args[0]
        if len(args) >= 2:
            self.width = args[1]
        if len(args) >= 3:
            self.height = args[2]
        if len(args) >= 4:
            self.x = args[3]
        if len(args) >= 5:
            self.y = args[4]
