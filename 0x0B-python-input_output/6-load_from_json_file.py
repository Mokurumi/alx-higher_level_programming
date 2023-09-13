#!/usr/bin/python3
"""module to save an object to a file"""

import json


def load_from_json_file(filename):
    """
    Loads a JSON file and creates a Python object from its contents.

    Args:
        filename (str): The name of the JSON file to load.

    Returns:
        object: The Python object created from the JSON file.
    """
    with open(filename, 'r') as file:
        return json.load(file)
