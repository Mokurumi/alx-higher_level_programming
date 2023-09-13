#!/usr/bin/python3
'''module to append to a file'''


def append_write(filename="", text=""):
    """
    Appends a string to the end of a text file (UTF-8)
        and returns the number of characters added.

    :param filename: The path to the text file where the text will be appended
        (default is an empty string).
    :type filename: str
    :param text: The string to be appended to the file.
    :type text: str
    :return: The number of characters added to the file.
    :rtype: int
    """
    with open(filename, 'a', encoding='utf-8') as file:
        return (file.write(text))
