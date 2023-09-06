#!/usr/bin/python3
"""Unit tests for max_integer"""


import unittest
from max_integer import max_integer


class TestMaxInteger(unittest.TestCase):
    """
    A set of unit tests for the max_integer function.
    """

    def test_empty_list(self):
        """
        Test case for an empty list.

        The max_integer function should return None when given an empty list.
        """
        result = max_integer([])
        self.assertIsNone(result)

    def test_single_element_list(self):
        """
        Test case for a list with a single element.

        The max_integer function should return the only element
            when the list contains only one element.
        """
        result = max_integer([42])
        self.assertEqual(result, 42)

    def test_positive_integer_list(self):
        """
        Test case for a list of positive integers.

        The max_integer function should return the largest integer
            from a list of positive integers.
        """
        result = max_integer([1, 3, 5, 7, 9])
        self.assertEqual(result, 9)

    def test_negative_integer_list(self):
        """
        Test case for a list of negative integers.

        The max_integer function should return the largest integer
            from a list of negative integers.
        """
        result = max_integer([-2, -4, -6, -8])
        self.assertEqual(result, -2)

    def test_mixed_integer_list(self):
        """
        Test case for a list of mixed integers.

        The max_integer function should return the largest integer
            from a list of mixed positive and negative integers.
        """
        result = max_integer([-2, 5, 0, 7, -8])
        self.assertEqual(result, 7)

    def test_float_list(self):
        """
        Test case for a list of floating-point numbers.

        The max_integer function should return the largest
            floating-point number from a list of floats.
        """
        result = max_integer([1.5, 2.5, 0.5])
        self.assertEqual(result, 2.5)

    def test_string_list(self):
        """
        Test case for a list of strings.

        The max_integer function should return the string
            with the highest lexicographic order from a list of strings.
        """
        result = max_integer(["apple", "banana", "cherry"])
        self.assertEqual(result, "cherry")

    def test_mixed_data_types(self):
        """
        Test case for a list with mixed data types.

        The max_integer function should return None
            when given a list with mixed data types.
        """
        result = max_integer([3, "apple", 7.5, -2])
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
