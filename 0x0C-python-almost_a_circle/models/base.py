#!/usr/bin/python3
"""
The Base class serves as the foundation for other classes in the project.
It manages the 'id' attribute for objects and ensures unique IDs are assigned.
"""

import json
import turtle
import csv


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
        if list_objs is None:
            list_objs = []

        filename = "{}.json".format(cls.__name__)
        with open(filename, "w", encoding="utf-8") as f:
            f.write(cls.to_json_string([o.to_dictionary() for o in list_objs]))

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

    @classmethod
    def load_from_file(cls):
        """
        Load instances from a JSON file and return a list of instances.

        Returns:
            list: A list of instances loaded from the file.
        """
        # Determine the filename based on the class name.
        filename = f"{cls.__name__}.json"

        try:
            with open(filename, "r") as file:
                json_data = file.read()
        except FileNotFoundError:
            # If the file doesn't exist, return an empty list.
            return []

        # Parse the JSON string into a list of dicts using from_json_string.
        data_list = cls.from_json_string(json_data)

        # Create instances from the dictionaries using the create method.
        instance_list = [cls.create(**data) for data in data_list]

        return instance_list


    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Serialize and save instances to a CSV file.

        Args:
            list_objs (list): A list of instances to serialize and save.

        Returns:
            None
        """
        # Determine the filename based on the class name.
        filename = f"{cls.__name__}.csv"

        # Create or overwrite the CSV file.
        with open(filename, "w", newline="") as csvfile:
            writer = csv.writer(csvfile)

            for obj in list_objs:
                if cls.__name__ == "Rectangle":
                    # For Rectangle, write id, width, height, x, to CSV file.
                    writer.writerow(
                            [obj.id, obj.width, obj.height, obj.x, obj.y]
                            )
                elif cls.__name__ == "Square":
                    # For Square, write id, size, x, y to the CSV file.
                    writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """
        Deserialize and load instances from a CSV file.

        Returns:
            list: A list of instances loaded from the CSV file.
        """
        # Determine the filename based on the class name.
        filename = f"{cls.__name__}.csv"

        try:
            with open(filename, "r", newline="") as csvfile:
                reader = csv.reader(csvfile)
                instance_list = []

                for row in reader:
                    if cls.__name__ == "Rectangle" and len(row) == 5:
                        # Create instances from CSV (id, width, height, x, y)
                        id, width, height, x, y = map(int, row)
                        instance = cls(width, height, x, y, id)
                    elif cls.__name__ == "Square" and len(row) == 4:
                        # For Square, create instances from CSV data
                        # (id, size, x, y).
                        id, size, x, y = map(int, row)
                        instance = cls(size, x, y, id)
                    else:
                        raise ValueError("Invalid CSV format")

                    instance_list.append(instance)

            return instance_list
        except FileNotFoundError:
            # If the file doesn't exist, return an empty list.
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Draw Rectangles and Squares using the Turtle graphics module.

        Args:
            list_rectangles (list): A list of Rectangle instances.
            list_squares (list): A list of Square instances.

        Returns:
            None
        """
        # Create a Turtle screen
        screen = turtle.Screen()
        screen.title("Drawing Rectangles and Squares")

        # Create a Turtle object for drawing
        drawer = turtle.Turtle()

        # Set up the drawing speed and other properties
        drawer.speed(0)  # Fastest drawing speed
        drawer.penup()    # Lift the pen to move without drawing lines

        # Draw Rectangles
        for rect in list_rectangles:
            drawer.goto(rect.x, rect.y)
            drawer.pendown()
            for _ in range(2):
                drawer.forward(rect.width)
                drawer.left(90)
                drawer.forward(rect.height)
                drawer.left(90)
            drawer.penup()

        # Draw Squares
        for square in list_squares:
            drawer.goto(square.x, square.y)
            drawer.pendown()
            for _ in range(4):
                drawer.forward(square.size)
                drawer.left(90)
            drawer.penup()

        # Close the drawing window when clicked
        screen.exitonclick()
