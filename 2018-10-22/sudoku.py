# We use numpy for an easy to use multi-dimensional array.
# https://www.numpy.org
import numpy as np


# Preliminaries
# --------------------------------------------------

def check_group(group):
    '''Asserts that ``group`` is a valid Sudoku row, column, or block.
    '''
    assert len(group.flat) == 9
    counts = np.zeros(10)  # An array of 10 zeros.
    for cell in group.flat:
        assert 0 <= cell <= 9
        if cell != 0: counts[cell] += 1
    assert (counts < 2).all()


def check_sudoku(board):
    '''Asserts that ``board`` is a valid Sudoku.
    '''
    assert board.shape == (9, 9)

    for row in range(9):
        check_group(board[row, :])

    for col in range(9):
        check_group(board[:, col])

    for rows in [slice(0, 3), slice(3, 6), slice(6, 9)]:
        for cols in [slice(0, 3), slice(3, 6), slice(6, 9)]:
            check_group(board[rows, cols])

# Sudoku Solver
# --------------------------------------------------

def find_zero(board):
    '''Find the row and column of a cell containing 0.
    '''
    for row in range(9):
        for col in range(9):
            if board[row, col] == 0:
                return row, col
    return -1, -1


def solve_sudoku(board):
    '''Solve a partial Sudoku board in-place.
    '''
    # Find a cell with a zero.
    # If there are no zeros, we've found a solution.
    row, col = find_zero(board)
    if (row, col) == (-1, -1):
        return board

    # Try to put a value in that cell.
    # If it fails the check or the recursive call, backtrack.
    for value in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        try:
            board[row, col] = value
            check_sudoku(board)
            return solve_sudoku(board)
        except AssertionError:
            board[row, col] = 0
            continue

    # If we made it this far, nothing worked.
    # Raise an AssertionError to make the caller backtrack.
    assert False


# Testing
# --------------------------------------------------

def test_sudoku():
    board = np.array([
        [5, 3, 0,   0, 7, 0,   0, 0, 0],
        [6, 0, 0,   1, 9, 5,   0, 0, 0],
        [0, 9, 8,   0, 0, 0,   0, 6, 0],

        [8, 0, 0,   0, 6, 0,   0, 0, 3],
        [4, 0, 0,   8, 0, 3,   0, 0, 1],
        [7, 0, 0,   0, 2, 0,   0, 0, 6],

        [0, 6, 0,   0, 0, 0,   2, 8, 0],
        [0, 0, 0,   4, 1, 9,   0, 0, 5],
        [0, 0, 0,   0, 8, 0,   0, 7, 9],
    ])

    check_sudoku(board)
    board = solve_sudoku(board)
    check_sudoku(board)
    return board
