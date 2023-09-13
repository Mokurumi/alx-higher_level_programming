#!/usr/bin/python3
'''module to append text to a file'''


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text
        after each line containing a specific string in a file.

    Args:
        filename (str): The name of the file to modify.
        search_string (str): The string to search for in each line.
        new_string (str): The line of text to insert
            after lines containing the search string.
    """
    text = ""
    with open(filename) as file_r:
        for line in file_r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as file_w:
        file_w.write(text)
