#!/usr/bin/python3
import sys


def is_safe(board, row, col, n):
    """
    Check if it's safe to place a queen at the specified position (row, col) on the board.

    Args:
        board (list): The current state of the chessboard.
        row (int): The row to check.
        col (int): The column to check.
        n (int): The size of the chessboard.

    Returns:
        bool: True if it's safe to place a queen at the given position, False otherwise.
    """
    # Check the left side of the current row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_nqueens(n):
    """
    Solve the N Queens puzzle and print all possible solutions.

    Args:
        n (int): The size of the chessboard and the number of queens to place.
    """
    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []

    def solve(row):
        if row == n:
            # Found a solution, append it to the list
            solutions.append([list(row) for row in board])
            return
        for col in range(n):
            if is_safe(board, row, col, n):
                # Place a queen and continue solving
                board[row][col] = 1
                solve(row + 1)
                # Backtrack by removing the queen before exploring other possibilities
                board[row][col] = 0

    solve(0)

    for solution in solutions:
        # Print each solution
        for row in solution:
            print(''.join('Q' if cell == 1 else '.' for cell in row))
        print()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        if n < 4:
            print("N must be at least 4")
            sys.exit(1)
        solve_nqueens(n)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
