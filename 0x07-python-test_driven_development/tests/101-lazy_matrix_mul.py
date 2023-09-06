#!/usr/bin/python3
"""Unit tests for lazy_matrix_mul"""


import unittest
import numpy as np
from lazy_matrix_multiplication import lazy_matrix_mul


class TestLazyMatrixMultiplication(unittest.TestCase):
    """
    A set of unit tests for the lazy_matrix_mul function.
    """

    def test_valid_matrix_multiplication(self):
        """
        Test case for valid matrix multiplication.

        The lazy_matrix_mul function should correctly multiply two matrices
            and return the result as a NumPy array.
        """
        m_a = [[1, 2], [3, 4]]
        m_b = [[5, 6], [7, 8]]
        result = lazy_matrix_mul(m_a, m_b)
        expected_result = np.array([[19, 22], [43, 50]])
        np.testing.assert_array_equal(result, expected_result)

    def test_invalid_matrix_multiplication(self):
        """
        Test case for invalid matrix multiplication.

        The lazy_matrix_mul function should raise a ValueError
        with a specific message when given matrices that cannot be multiplied.
        """
        m_a = [[1, 2, 3], [4, 5, 6]]
        m_b = [[7, 8], [9, 10]]
        with self.assertRaises(ValueError) as context:
            lazy_matrix_mul(m_a, m_b)
        self.assertIn(
                "NumPy matrix multiplication error:", str(context.exception)
                )

    def test_invalid_matrix_a(self):
        """
        Test case for invalid matrix m_a.

        The lazy_matrix_mul function should raise a ValueError
            with a specific message for invalid m_a.
        """
        invalid_matrices = [
            ([], [[]]),
            ([[]], [[]]),
            ([["a"]], [[]]),
            ([["a", 2], [3, 4]], [[]]),
            (["a"], [[]]),
        ]
        for m_a in invalid_matrices:
            with self.subTest(m_a=m_a):
                with self.assertRaises(ValueError) as context:
                    lazy_matrix_mul(m_a, [[1]])
                self.assertIn(
                        "NumPy matrix multiplication error:",
                        str(context.exception)
                        )

    def test_invalid_matrix_b(self):
        """
        Test case for invalid matrix m_b.

        The lazy_matrix_mul function should raise a ValueError
            with a specific message for invalid m_b.
        """
        invalid_matrices = [
            ([[]], []),
            ([[]], [["a"]]),
            ([[]], [["a", 2], [3, 4]]),
            ([[]], ["a"]),
        ]
        for m_b in invalid_matrices:
            with self.subTest(m_b=m_b):
                with self.assertRaises(ValueError) as context:
                    lazy_matrix_mul([[]], m_b)
                self.assertIn(
                        "NumPy matrix multiplication error:",
                        str(context.exception)
                        )

if __name__ == '__main__':
    unittest.main()
