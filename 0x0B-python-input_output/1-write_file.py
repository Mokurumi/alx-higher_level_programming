#!/usr/bin/python3
'''module to write to a file'''


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF-8)
        and returns the number of characters written.

    :param filename: The path to the text file where the text will be written
        (default is an empty string).
    :type filename: str
    :param text: The string to be written to the file.
    :type text: str
    :return: The number of characters written to the file.
    :rtype: int
    """
    with open(filename, 'w', encoding='utf=8') as file:
        return file.write(text)
