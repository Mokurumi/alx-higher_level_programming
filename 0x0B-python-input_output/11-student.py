#!/usr/bin/python3
'''module that defines a student class'''


class Student:
    """
    Defines a Student with first_name, last_name, and age attributes.
    Provides a method to retrieve a dict representation of the Student instance
    """
    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance with first_name, last_name, and age.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        Args:
            attrs (list, optional): A list of strings specifying
                which attributes to include in the dictionary.
                If None, all attributes are included.

        Returns:
            dict: A dictionary with the specified attributes of the Student.
        """
        if attrs is None:
            return self.__dict__
        my_dict = {}
        for attr in attrs:
            if attr in self.__dict__.keys():
                my_dict[attr] = self.__dict__[attr]
        return my_dict

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance
            based on a dictionary representation (JSON).

        Args:
            json (dict): A dictionary containing attribute names
                and values to update the Student instance.
        """
        for key, value in json.items():
            setattr(self, key, value)
