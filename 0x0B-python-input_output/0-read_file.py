#!/usr/bin/python3
"""Module that reads a file"""


def read_file(filename=''):
    """
    Reads the contents of a text file (UTF-8) and prints it to stdout.

    :param filename: The path to the text file to be read
        (default is an empty string).
    :type filename: str
    """
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read(), end="")
