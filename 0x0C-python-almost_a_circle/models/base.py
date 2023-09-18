#!/usr/bin/python3
"""
The Base class serves as the foundation for other classes in the project.
It manages the 'id' attribute for objects and ensures unique IDs are assigned.
"""


class Base:
    """
    Attributes:
        __nb_objects (int): A private class attribute
            to keep track of the number of objects created.

    Methods:
        __init__(self, id=None): Class constructor for Base objects.
            If 'id' is provided,
                it assigns the provided value to the 'id' attribute.
            If 'id' is not provided,
                it increments the __nb_objects counter
                and assigns the new value to the 'id' attribute.
    """

    # Private class attribute to keep track of the number of objects created.
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a Base object.

        Args:
            id (int, optional): The ID to assign to the object.
                If not provided, a unique ID will be generated
                based on __nb_objects.

        Attributes:
            id (int): The unique identifier for the object.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
