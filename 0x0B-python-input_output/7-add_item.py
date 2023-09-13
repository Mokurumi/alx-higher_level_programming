#!/usr/bin/python3
"""
module to add all arguments to a Python list, and then save them to a file
"""

import sys
import json
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file


def add_args_to_list_and_save():
    """add arguments to a list"""
    # Define the filename
    filename = 'add_item.json'

    try:
        # Load existing data from the file, if it exists
        data = load_from_json_file(filename)
    except FileNotFoundError:
        # If the file doesn't exist, start with an empty list
        data = []

    # Add command-line arguments to the list
    data.extend(sys.argv[1:])

    # Save the updated data to the file
    save_to_json_file(data, filename)

if __name__ == '__main__':
    add_args_to_list_and_save()
