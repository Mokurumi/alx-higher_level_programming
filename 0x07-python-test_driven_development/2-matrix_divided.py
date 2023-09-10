#!/usr/bin/python3
"""dividing matrix module that takes in floats and integers"""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a given divisor.

    Args:
    matrix (list of lists): The input matrix,
        where each row must be of the same size.
    div (int or float): The divisor.

    Returns:
    list of lists: A new matrix with all elements divided by 'div',
        rounded to 2 decimal places.

    Raises:
    TypeError: If the input matrix is not a list of lists of integers/floats,
               or if each row of the matrix doesn't have the same size.
               If 'div' is not a number (integer or float).
    ZeroDivisionError: If 'div' is equal to 0.

    Example:
    >>> matrix_divided([[1, 2, 3], [4, 5, 6]], 2)
    [[0.5, 1.0, 1.5], [2.0, 2.5, 3.0]]
    """
    # Check if 'matrix' is a list of lists of integers/floats
    if not matrix or not all(isinstance(row, list) and
    all(isinstance(num, (int, float)) for num in row) for row in matrix):
        raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
                )

    # Check if all rows have the same size
    if len(set(len(row) for row in matrix)) != 1:
        raise TypeError("Each row of the matrix must have the same size")

    # Check if 'div' is a number (integer or float)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check if 'div' is not equal to 0
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Perform the division and rounding
    result_matrix = []
    for row in matrix:
        new_row = [round(num / div, 2) for num in row]
        result_matrix.append(new_row)

    return result_matrix
