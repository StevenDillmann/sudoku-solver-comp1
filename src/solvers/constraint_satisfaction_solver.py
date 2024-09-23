# flake8: noqa F401
import typing

# === MAIN FUNCTIONS ==========================================================
"""!@file constraint_satisfaction_solver.py
@brief Module containing tools to solve a sudoku using constraint satisfaction.

@details  This script takes a sudoku array (list of lists) as an input and
returns a solved sudoku array (list of lists) using the backtracking algorithm
with an elimination constraint.
@author Created by Steven Dillmann 17/12/2023
"""

# 1. solve_sudoku_cs


def solve_sudoku_cs(sudoku):
    """!@brief This is the main function to solve a sudoku using the
    backtracking algorithm with an elimination constraint.

    @details It takes a sudoku array (list of lists) as an input and
    returns a solved sudoku array (list of lists). The algorithm works by
    iterating through each cell in the sudoku and trying all possible
    numbers and backtracking when necessary to ensure a valid solution.

    @param sudoku The sudoku array (list of lists) to solve
    @type sudoku list of lists
    @return sudoku_solved The solved sudoku array (list of lists) to solve
    @rtype list of lists
    @see get_valid_numbers Function to get all valid numbers for a cell

    References:
    - Helmut Simonis. Sudoku as a constraint problem. In CP Workshop on
    modeling and reformulating Constraint Satisfaction Problems, volume 12,
    pages 13–27. Citeseer, 2005.
    - https://sudoku.com/sudoku-rules/notes-in-sudoku/

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
    >>> solve_sudoku_cs(sudoku)
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

    # Run backtracking algorithm including elimination constraint
    def solve():
        for row in range(9):
            for col in range(9):
                # Find an empty cell
                if sudoku_solved[row][col] == 0:
                    # Get all valid numbers for this cell based on rules
                    valid_numbers = get_valid_numbers(sudoku_solved, row, col)
                    # Trigger backtracking if no valid numbers
                    if len(valid_numbers) == 0:
                        return False
                    # Try the valid numbers for this cell
                    for num in valid_numbers:
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

# 1.1 get_valid_numbers


def get_valid_numbers(sudoku, row, col):
    """!@brief Gets all valid numbers for a cell in the sudoku array
    (list of lists).

    @details This is a helper function for the constraint satisfaction
    algorithm. It takes a sudoku array (list of lists), a row index and a
    column index as inputs and returns a list of valid numbers for the cell
    at the given row and column index.

    @param sudoku The sudoku array (list of lists) to solve
    @type sudoku list of lists
    @param row The row index of the cell to check
    @type row int
    @param col The column index of the cell to check
    @type col int
    @return A list of valid numbers for the cell at the given row and
    column index
    @rtype list
    """
    # Get a set of all numbers
    valid_numbers = set(range(1, 10))
    # Eliminate numbers from the set that exist in row and column
    for i in range(9):
        valid_numbers.discard(sudoku[row][i])
        valid_numbers.discard(sudoku[i][col])
    # Eliminate numbers from the set that exist in subgrid
    sub_row_start = (row // 3) * 3  # define subgrid row start index
    sub_col_start = (col // 3) * 3  # define subgrid column start index
    for i in range(3):
        for j in range(3):
            valid_numbers.discard(sudoku[sub_row_start + i][sub_col_start + j])
    return list(valid_numbers)
