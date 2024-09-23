# flake8: noqa F401
import typing

# === MAIN FUNCTIONS ==========================================================
"""!@file back_tracking_solver.py
@brief Module containing tools to solve a sudoku using backtracking algorithm.

@details  This script takes a sudoku array (list of lists) as an input and
returns a solved sudoku array (list of lists) using the backtracking algorithm.
@author Created by Steven Dillmann 17/12/2023
"""


# 1. solve_sudoku_bt
def solve_sudoku_bt(sudoku):
    """!@brief This is the main function to solve a sudoku using the
    backtracking algorithm.

    @details It takes a sudoku array (list of lists) as an input and
    returns a solved sudoku array (list of lists). The algorithm works by
    iterating through each cell in the sudoku and trying all numbers and
    backtracking when necessary to ensure a valid solution.

    @param sudoku The sudoku array (list of lists) to solve
    @type sudoku list of lists
    @return sudoku_solved The solved sudoku array (list of lists)
    @rtype list of lists
    @see is_number_valid Function to check if a number is valid in sudoku

    References:
    - Dhanya Job and Varghese Paul. Recursive backtracking for solving 9*9
    sudoku puzzle. Bonfring International Journal of Data Mining, 6(1):7–9,
    2016.

    Example:
    >>> sudoku = [
        [3, 0, 2, 6, 0, 9, 0, 0, 5],
        [5, 0, 0, 7, 3, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 9, 0, 0],
        [0, 0, 0, 9, 4, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 9],
        [0, 0, 0, 0, 5, 7, 0, 6, 0],
        [0, 0, 8, 5, 0, 0, 0, 0, 6],
        [0, 0, 0, 0, 0, 0, 0, 0, 3],
        [0, 1, 9, 0, 8, 2, 0, 4, 0],
        ]
    >>> solve_sudoku_bt(sudoku)
    [
        [3, 8, 2, 6, 1, 9, 4, 7, 5],
        [5, 9, 4, 7, 3, 8, 6, 2, 1],
        [1, 7, 6, 4, 2, 5, 9, 3, 8],
        [8, 6, 3, 9, 4, 1, 7, 5, 2],
        [4, 5, 7, 2, 6, 3, 1, 8, 9],
        [9, 2, 1, 8, 5, 7, 3, 6, 4],
        [7, 3, 8, 5, 9, 4, 2, 1, 6],
        [2, 4, 5, 1, 7, 6, 8, 9, 3],
        [6, 1, 9, 3, 8, 2, 5, 4, 7],
    ]
    """
    # Create copy of initial sudoku
    sudoku_solved = [row[:] for row in sudoku]

    # Run backtracking algorithm
    def solve():
        for row in range(9):
            for col in range(9):
                # Find empty cell
                if sudoku_solved[row][col] == 0:
                    # Try all numbers for this cell
                    for num in range(1, 10):
                        # Check if number is valid for this cell based on rules
                        if is_number_valid(sudoku_solved, row, col, num):
                            sudoku_solved[row][col] = num
                            # Solve the updated sudoku with recursion
                            if solve():
                                return True
                            # Backtrack if the number doesn't lead to solution
                            sudoku_solved[row][col] = 0
                    return False
        return True

    # Return the solved sudoku if the sudoku is valid
    if solve():
        return sudoku_solved
    else:
        # Print a warning if sudoku is invalid/unsolveable
        print("Unsolveable Sudoku. Returned 'None'.")
        return None


# === HELPER FUNCTIONS ========================================================

# 1.1 is_number_valid


def is_number_valid(sudoku, row, col, num):
    """!@brief Checks if a number is valid in sudoku at the given row and
    column index.

    @details This is a helper function for the backtracking algorithm. It
    takes a sudoku array (list of lists), a row index, a column index, and
    a number as inputs and returns a boolean value indicating if the number
    is valid in the sudoku array at the given row and column index.

    @param sudoku The sudoku array (list of lists) to solve
    @type sudoku list of lists
    @param row The row index of the cell to check
    @type row int
    @param col The column index of the cell to check
    @type col int
    @param num The number to check
    @type num int
    @return A boolean value indicating if the number is valid in sudoku
    @rtype bool
    """
    # Check if the given number is valid in its row and column
    for i in range(9):
        if sudoku[row][i] == num or sudoku[i][col] == num:
            return False
    # Check if the given number is possible in its subgrid
    sub_row_start = (row // 3) * 3  # define subgrid row start index
    sub_col_start = (col // 3) * 3  # define subgrid column start index
    for i in range(0, 3):
        for j in range(0, 3):
            if sudoku[sub_row_start + i][sub_col_start + j] == num:
                return False
    return True
