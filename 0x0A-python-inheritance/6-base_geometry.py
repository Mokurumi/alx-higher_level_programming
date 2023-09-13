#!/usr/bin/python3
'''empty base BaseGeometry'''


class BaseGeometry:
    '''Empty class'''
    def area(self):
        """
        Raises an Exception with the message "area() is not implemented".
        """
        raise Exception("area() is not implemented")
