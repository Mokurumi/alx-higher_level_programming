#!/usr/bin/python3
"""
The Base class serves as the foundation for other classes in the project.
It manages the 'id' attribute for objects and ensures unique IDs are assigned.
"""

import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Return the JSON string representation of a list of dictionaries.

        Args:
            list_dictionaries (list): A list of dictionaries.

        Returns:
            str: JSON string representation of list_dictionaries.
        """
        if not list_dictionaries:
            return "[]"

        # Use json module to convert the list of dictionaries to a JSON string
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Write the JSON string representation of list_objs to a file.

        Args:
            list_objs (list): A list of instances that inherit from Base.

        Returns:
            None
        """
        # Get the class name to use in the filename (e.g., Rectangle.json).
        class_name = cls.__name__
        # Create the filename by appending '.json' to the class name.
        filename = f"{class_name}.json"

        # Initialize an empty list if list_objs is None.
        if list_objs is None:
            list_objs = []

        # Convert the list of instances to a list of dictionaries
        # using to_dictionary method.
        list_dicts = [obj.to_dictionary() for obj in list_objs]

        # Use the json module to convert the list of dict to a JSON string.
        json_string = json.dumps(list_dicts)

        # Write JSON string to the file, overwriting it if it already exists.
        with open(filename, "w") as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """
        Return a list from the JSON string representation.

        Args:
            json_string (str): A string representing a list of dictionaries.

        Returns:
            list: The list represented by json_string.
        """
        if not json_string:
            return []

        # Use the json module to parse the JSON string into a list of dict
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Create an instance with attributes set based on the provided dict

        Args:
            **dictionary: Keyword arguments representing
                attribute names and values.

        Returns:
            Base: An instance of the class with
                attributes set according to the dictionary.
        """
        # Create a "dummy" instance with mandatory attributes.
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)
        else:
            raise ValueError("Unsupported class")

        # Use the update method to set the attributes based on the dictionary.
        dummy_instance.update(**dictionary)

        return dummy_instance
