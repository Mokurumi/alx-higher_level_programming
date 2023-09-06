#!/usr/bin/python3
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
    TypeError: If each row of the matrix doesn't have the same size.
               If 'div' is not a number
               (integer, float, or convertible from string).
    ZeroDivisionError: If 'div' is equal to 0.

    Example:
    >>> matrix_divided([[1, '2', 3], [4, 5, '6']], 2)
    [[0.5, 1.0, 1.5], [2.0, 2.5, 3.0]]
    """
    # Check if all rows have the same size
    if len(set(len(row) for row in matrix)) != 1:
        raise TypeError("Each row of the matrix must have the same size")

    # Check if 'div' is not equal to 0
    if div == 0:
        raise ZeroDivisionError("division by zero")

    result_matrix = []

    for row in matrix:
        new_row = []
        for element in row:
            # Try to convert the element to a number (integer or float)
            try:
                num = float(element)
                new_row.append(round(num / div, 2))
            except (ValueError, TypeError):
                raise TypeError(
                        "All elements of the matrix
                        must be convertible to numbers"
                    )

        result_matrix.append(new_row)

    return result_matrix
