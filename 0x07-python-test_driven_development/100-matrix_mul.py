#!/usr/bin/python3
'''module for multiplying matrices'''


def validate_matrix(matrix, matrix_name):
    """
    Validate a matrix to ensure it meets the specified requirements.

    Args:
        matrix (list): The matrix to be validated.
        matrix_name (str): The name of the matrix for error messages.

    Raises:
        TypeError: If the matrix is not a list, not a list of lists,
            or contains non-integer/non-float elements.
        ValueError: If the matrix is empty or
            not a rectangular matrix (rows of different sizes).
    """
    if not isinstance(matrix, list):
        raise TypeError(f"{matrix_name} must be a list")
    if (not matrix or (len(matrix) == 1 and not matrix[0])):
        raise ValueError(f"{matrix_name} can't be empty")
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError(f"{matrix_name} must be a list of lists")

    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError(
                    f"each row of {matrix_name} must be of the same size"
                    )
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(
                        f"{matrix_name} should contain only integers or floats"
                        )


def matrix_mul(m_a, m_b):
    """
    Multiply two matrices and return the result.

    Args:
        m_a (list of lists): The first matrix.
        m_b (list of lists): The second matrix.

    Returns:
        list of lists: The result of multiplying m_a and m_b.

    Raises:
        TypeError: If m_a or m_b do not meet the validation requirements.
        ValueError: If m_a and m_b cannot be multiplied
            due to incompatible dimensions.
    """
    # Validate matrices
    validate_matrix(m_a, "m_a")
    validate_matrix(m_b, "m_b")

    # Check if matrices can be multiplied
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Perform matrix multiplication
    result = []
    for i in range(len(m_a)):
        row = []
        for j in range(len(m_b[0])):
            element = 0
            for k in range(len(m_b)):
                element += m_a[i][k] * m_b[k][j]
            row.append(element)
        result.append(row)

    return result
