#!/usr/bin/python3
import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """
    Multiply two matrices m_a and m_b using NumPy.

    Args:
    m_a (list of lists): The first matrix.
    m_b (list of lists): The second matrix.

    Returns:
    numpy.ndarray: The result of multiplying m_a and m_b as a NumPy array.

    Raises:
    ValueError: If the matrices
        cannot be multiplied due to incompatible dimensions.

    Example:
    >>> lazy_matrix_mul([[1, 2], [3, 4]], [[5, 6], [7, 8]])
    array([[19, 22],
           [43, 50]])
    """
    try:
        np_m_a = np.array(m_a)
        np_m_b = np.array(m_b)
        result = np.dot(np_m_a, np_m_b)
        return result
    except ValueError as ve:
        raise ValueError("NumPy matrix multiplication error: " + str(ve))
