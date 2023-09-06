#!/usr/bin/python3
"""Unit tests for matrix_mul"""


import unittest
from matrix_multiplication import matrix_mul


class TestMatrixMultiplication(unittest.TestCase):
    """
    A set of unit tests for the matrix_mul function.
    """

    def test_valid_matrix_multiplication(self):
        """
        Test case for valid matrix multiplication.

        The matrix_mul function should correctly multiply two matrices
            and return the result.
        """
        m_a = [[1, 2], [3, 4]]
        m_b = [[5, 6], [7, 8]]
        result = matrix_mul(m_a, m_b)
        expected_result = [[19, 22], [43, 50]]
        self.assertEqual(result, expected_result)

    def test_invalid_matrix_multiplication(self):
        """
        Test case for invalid matrix multiplication.

        The matrix_mul function should raise a ValueError
            when given matrices that cannot be multiplied.
        """
        m_a = [[1, 2, 3], [4, 5, 6]]
        m_b = [[7, 8], [9, 10]]
        with self.assertRaises(ValueError):
            matrix_mul(m_a, m_b)

    def test_invalid_matrix_a(self):
        """
        Test case for invalid matrix m_a.

        The matrix_mul function should raise appropriate exceptions
            for invalid m_a.
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
                with self.assertRaises((TypeError, ValueError)):
                    matrix_mul(m_a, [[1]])

    def test_invalid_matrix_b(self):
        """
        Test case for invalid matrix m_b.

        The matrix_mul function should raise appropriate exceptions
            for invalid m_b.
        """
        invalid_matrices = [
            ([[]], []),
            ([[]], [["a"]]),
            ([[]], [["a", 2], [3, 4]]),
            ([[]], ["a"]),
        ]
        for m_b in invalid_matrices:
            with self.subTest(m_b=m_b):
                with self.assertRaises((TypeError, ValueError)):
                    matrix_mul([[]], m_b)

if __name__ == '__main__':
    unittest.main()
