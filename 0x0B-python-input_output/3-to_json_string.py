#!/usr/bin/python3
"""module to stringify an object"""

import json


def to_json_string(my_obj):
    """
    Converts an object to its JSON representation as a string.
    """
    return json.dumps(my_obj)
