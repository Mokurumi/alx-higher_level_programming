#!/usr/bin/python3
def matrix_mul(m_a, m_b):
    """
    Multiply two matrices m_a and m_b.

    Args:
    m_a (list of lists): The first matrix.
    m_b (list of lists): The second matrix.

    Returns:
    list of lists: The result of multiplying m_a and m_b.

    Raises:
    TypeError: If m_a or m_b is not a list or not a list of lists.
               If m_a or m_b is empty or contains non-integer/float elements.
               If the rows of m_a or m_b are not of the same size.
    ValueError: If m_a and m_b cannot be multiplied.

    Example:
    >>> matrix_mul([[1, 2], [3, 4]], [[5, 6], [7, 8]])
    [[19, 22], [43, 50]]
    """
    # Validate m_a and m_b
    for matrix, name in [(m_a, 'm_a'), (m_b, 'm_b')]:
        if not isinstance(matrix, list):
            raise TypeError(f"{name} must be a list")
        if not all(isinstance(row, list) for row in matrix):
            raise TypeError(f"{name} must be a list of lists")
        if len(matrix) == 0 or any(len(row) == 0 for row in matrix):
            raise ValueError(f"{name} can't be empty")
        if not all(isinstance(num, (int, float)) \
                for row in matrix for num in row):
            raise TypeError(f"{name} should contain only integers or floats")

    # Check if rows of m_a and m_b are of the same size
    if any(len(row) != len(m_a[0]) for row in m_a) \
            or any(len(row) != len(m_b[0]) for row in m_b):
        raise TypeError(
                "Each row of m_a must be of the same size
                or each row of m_b must be of the same size"
                )

    # Check if m_a and m_b can be multiplied
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Perform matrix multiplication
    result = [[0 for _ in range(len(m_b[0]))] for _ in range(len(m_a))]
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                result[i][j] += m_a[i][k] * m_b[k][j]

    return result
