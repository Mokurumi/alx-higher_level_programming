#!/usr/bin/python3
"""
module to add all arguments to a Python list, and then save them to a file
"""


import json
import sys


# Import the functions using __import__
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


if __name__ == "__main__":
    # Check if the JSON file exists, and if not, create it
    try:
        existing_data = load_from_json_file('add_item.json')
    except FileNotFoundError:
        existing_data = []

    # Combine existing data with command line arguments
    new_data = existing_data + sys.argv[1:]

    # Save the combined data to 'add_item.json'
    save_to_json_file(new_data, 'add_item.json')
