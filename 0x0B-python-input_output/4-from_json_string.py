#!/usr/bin/python3
"""module to get an object from a string"""

import json


def from_json_string(my_str):
    """
    Converts a JSON string to a Python data structure (object).

    Args:
        my_str (str): The JSON string to be converted to a Python object.
    """
    return json.loads(my_str)
