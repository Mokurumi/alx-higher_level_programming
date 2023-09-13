#!/usr/bin/python3
'''module for pascal's triangle'''


def pascal_triangle(n):
    """
    Generates Pascal's triangle up to the specified number of rows (n).

    Args:
        n (int): The number of rows in Pascal's triangle.

    Returns:
        list of lists: A list of lists representing Pascal's triangle.
    """
    if n <= 0:
        return []

    # Initialize the result list with the first row
    result = [[1]]

    for i in range(1, n):
        # Generate the next row based on the previous row
        prev_row = result[-1]
        next_row = [1]

        for j in range(1, i):
            next_row.append(prev_row[j - 1] + prev_row[j])

        next_row.append(1)
        result.append(next_row)

    return result
