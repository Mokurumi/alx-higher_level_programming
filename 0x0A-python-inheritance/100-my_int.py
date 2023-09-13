#!/usr/bin/python3
'''module that implements a class inheriting from int'''


class MyInt(int):
    '''A class that inherits from int'''
    def __eq__(self, other):
        """
        Override the == operator to invert its behavior.

        Args:
        other: The other object to compare with.

        Returns:
        bool: True if the objects are not equal, False if they are equal.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Override the != operator to invert its behavior.

        Args:
        other: The other object to compare with.

        Returns:
        bool: True if the objects are equal, False if they are not equal.
        """
        return super().__eq__(other)
