#!/usr/bin/python3
'''module that uses numpy to multiply matrices'''


import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiply two matrices using NumPy.

    Args:
    m_a (numpy.ndarray): The first matrix.
    m_b (numpy.ndarray): The second matrix.

    Returns:
    numpy.ndarray: The result of matrix multiplication.
    """
    return np.matmul(m_a, m_b)
