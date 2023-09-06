#!/usr/bin/python3
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
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    lines = text.split('.')
    for line in lines:
        questions = line.split('?')
        for question in questions:
            colons = question.split(':')
            for colon in colons:
                print(colon.strip())
            if len(colons) > 1:
                print()  # Add an empty line after ':' if present
        if len(questions) > 1:
            print()  # Add an empty line after '?' if present
    if len(lines) > 1:
        print()  # Add an empty line after '.' if present
