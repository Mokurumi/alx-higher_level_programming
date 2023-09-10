#!/usr/bin/python3
'''the function for testing text indentation'''


def text_indentation(text):
    """
    Print a text with 2 new lines after each '.', '?', and ':' character.
    Args:
    text (str): The input text.
    Raises:
    TypeError: If 'text' is not a string.
    Example:
    >>> text_indentation("Hello there. How are you? I'm good: thanks.")
    Hello there
    How are you
    I'm good
    thanks.
    """
    # Check if 'text' is a string
    if not text or not isinstance(text, str):
        raise TypeError("text must be a string")

    new_line_chars = ['.', '?', ':']

    current_line = ""
    for char in text:
        current_line += char
        if char in new_line_chars:
            print(current_line.strip())
            print()  # Add an empty line
            current_line = ""

    if current_line:
        print(current_line.strip(), end='')
