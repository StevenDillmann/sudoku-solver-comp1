from pulp import (
    LpProblem,
    LpVariable,
    lpSum,
    value,
    LpInteger,
    LpMinimize,
    GLPK,
)

# === MAIN FUNCTIONS ==========================================================
"""!@file linear_programming_solver.py
@brief Module containing tools to solve a sudoku using linear programming.

@details  This script takes a sudoku array (list of lists) as an input and
returns a solved sudoku array (list of lists) using linear programming.
@author Created by Steven Dillmann 17/12/2023
"""

# 1. solve_sudoku_lp


def solve_sudoku_lp(sudoku):
    """!@brief This is the main function to solve a sudoku using the linear
    programming algorithm.

    @details It takes a sudoku array (list of lists) as an input and
    returns a solved sudoku array (list of lists). The algorithm works by
    creating a linear programming problem with a decision variable for each
    possible sudoku number in each cell. The algorithm then adds
    constraints to the problem to ensure that each cell contains exactly
    one sudoku number, each row contains unique sudoku numbers, each column
    contains unique sudoku numbers and each subgrid contains unique sudoku
    numbers. The algorithm then solves the linear programming problem.

    @param sudoku The sudoku array (list of lists) to solve
    @type sudoku list of lists
    @return sudoku_solved The solved sudoku array (list of lists) to solve
    @rtype list of listss
    @see define_constraints Function to define the constraints for the
    linear programming problem
    @see extract_sudoku Function to extract the solved sudoku numbers
    @see is_sudoku_solved Function to check if the sudoku is solved

    References:
    - Robert J Vanderbei et al. Linear programming. Springer, 2020.
    - https://towardsdatascience.com/solve-sudoku-using-linear-programming-
    python-pulp-b41b29f479f3

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
    >>> solve_sudoku_lp(sudoku)
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
    # Create a linear programming problem
    sudoku_lp = LpProblem("Sudoku_LP_Problem", LpMinimize)
    # Create all combinations of rows, columns and possible sudoku numbers
    cells = [
        (row, col, num)
        for row in range(9)
        for col in range(9)
        for num in range(1, 10)
    ]
    # Create a decision variable: number k exists in cell (i,j) or not (0 or 1)
    decision = LpVariable.dicts("Cell", cells, 0, 1, LpInteger)
    # Fix initial sudoku numbers
    for row in range(9):
        for col in range(9):
            if sudoku[row][col] != 0:
                sudoku_lp += decision[(row, col, sudoku[row][col])] == 1
    # Add cell, row, column and subgrid constraints
    define_constraints(sudoku_lp, decision)
    # Solve the linear programming problem
    sudoku_lp.solve(solver=GLPK(msg=0))
    # Extract the solved sudoku numbers from the decision variables
    sudoku_solved = extract_sudoku(decision)
    # Return the solved sudoku if the sudoku is valid (error trapping)
    if is_sudoku_solved(sudoku_solved):
        return sudoku_solved
    else:
        # Print a warning if sudoku is invalid/unsolveable
        print("Unsolveable Sudoku. Returned 'None'.")
        return None


# === HELPER FUNCTIONS ========================================================

# 1.1 define_constraints


def define_constraints(sudoku_lp, decision):
    """!@brief Adds constraints to the linear programming problem to ensure
    that each cell abides by the sudoku rules.

    @details This is a helper function for the linear programming
    algorithm. It takes a linear programming problem and a decision
    variable as an input and adds constraints to the linear programming
    problem to ensure that each cell contains exactly one sudoku number,
    each row contains unique sudoku numbers, each column contains unique
    sudoku numbers and each subgrid contains unique sudoku numbers.

    @param sudoku_lp The linear programming problem to solve (LpProblem)
    @type sudoku_lp LpProblem
    @param decision The decision variable for each possible sudoku number
    in each cell (LpVariable)
    @type decision LpVariable
    @return None
    @rtype None
    """
    # Cell constraint: cells must contain exactly one sudoku number
    for row in range(9):
        for col in range(9):
            sudoku_lp += (
                lpSum([decision[(row, col, num)] for num in range(1, 10)]) == 1
            )
    # Row constraint: rows must contain unique sudoku numbers
    for row in range(9):
        for num in range(1, 10):
            sudoku_lp += (
                lpSum([decision[(row, col, num)] for col in range(9)]) == 1
            )
    # Column constraint: columns must contain unique sudoku numbers
    for col in range(9):
        for num in range(1, 10):
            sudoku_lp += (
                lpSum([decision[(row, col, num)] for row in range(9)]) == 1
            )
    # Subgrid constraint: subgrids must contain unique sudoku numbers
    for a in range(0, 9, 3):
        for b in range(0, 9, 3):
            for num in range(1, 10):
                sudoku_lp += (
                    lpSum(
                        [
                            decision[(row, col, num)]
                            for row in range(a, a + 3)
                            for col in range(b, b + 3)
                        ]
                    )
                    == 1
                )


# 1.2 extract_sudoku


def extract_sudoku(decision):
    """!@brief Extracts the solved sudoku numbers from the decision variables.

    @details This is a helper function for the linear programming
    algorithm. It takes a decision variable as an input and returns a
    solved sudoku array (list of lists) containing the solved sudoku
    numbers. The  function loops through each cell and each possible sudoku
    number and checks if the decision variable is equal to 1. If the
    decision variable is equal to 1, the function adds the sudoku number to
    the solved sudoku array and breaks the loop.

    @param decision The decision variable for each possible sudoku number
    in each cell (LpVariable)
    @type decision LpVariable
    @return sudoku_solved The solved sudoku array (list of lists)
    @rtype list of lists
    """
    # Create an empty sudoku to store the solved sudoku numbers
    sudoku_solved = [[0 for _ in range(9)] for _ in range(9)]
    # Extract the solved sudoku numbers from the decision variables
    for row in range(9):
        for col in range(9):
            for num in range(1, 10):
                if value(decision[(row, col, num)]) == 1:
                    sudoku_solved[row][col] = num
                    break  # break once a valid k is found for cell (i,j)
    return sudoku_solved


# 1.3 is_sudoku_solved


def is_sudoku_solved(sudoku):
    """!@brief Checks if the sudoku array (list of lists) is solved.

    @details This is a helper function for the linear programming
    algorithm. It takes a sudoku array (list of lists) as an input and
    returns a boolean value indicating if the sudoku array is solved. The
    function checks if each row and column contains unique numbers and if
    each subgrid contains unique numbers.

    @param sudoku The sudoku array (list of lists)
    @type sudoku list of lists
    @return A boolean value indicating if the sudoku is solved
    @rtype bool
    """
    # Check rows and columns for unique numbers
    for i in range(9):
        row_numbers = set(sudoku[i])
        col_numbers = set(sudoku[j][i] for j in range(9))
        if len(row_numbers) != 9 or len(col_numbers) != 9:
            return False
    # Check subgrids for unique numbers
    for a in range(0, 9, 3):
        for b in range(0, 9, 3):
            subgrid_values = set()
            for i in range(3):
                for j in range(3):
                    subgrid_values.add(sudoku[a + i][b + j])
            if len(subgrid_values) != 9:
                return False
    return True
