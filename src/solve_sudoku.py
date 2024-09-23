"""!@mainpage C1 Coursework Submission: Sudoku Solver Documentation
@section intro_sec Introduction
This is a Python script that implements a Sudoku solver with the option to
choose between three different algorithms:

1. backtracking algorithm
2. constraint satisfaction algorithm
3. linear programming algorithm

@section install_sec Installation
To install the script, simply clone the repository and run the script with
Python 3.9 or higher.

@section example_sec Example
Example usage of the script:

python sudoku_solve.py input.txt lp

This will solve the sudoku in input.txt using the linear programming
algorithm and print the solution to the terminal.

@author Steven Dillmann
@date 17/12/2023

@file solve_sudoku.py
@brief Script containing the main function to solve a sudoku.
@details This script contains the main function to solve a sudoku. It takes a
sudoku file as an input and returns a solved sudoku file. The script can be
run from the command line with the following command:

python sudoku_solve.py input.txt [solver]

where input.txt is the input sudoku file and solver is the optional solver
argument. The solver argument can be one of the following:

1. bt: backtracking algorithm
2. cs: constraint satisfaction algorithm
3. lp: linear programming algorithm

If no solver argument is specified, the script will use the constraint
satisfaction algorithm by default.

@package processors
@package solvers
"""

import sys
import os
import time
from processors import checkers, converters
from solvers import (
    back_tracking_solver,
    constraint_satisfaction_solver,
    linear_programming_solver,
)

# === OVERALL SUDOKU SOLVER FUNCTION ==========================================


def solve_sudoku(sudoku_file, solver="lp", save_file=False):
    """!@brief This is the main function to solve a sudoku.

    @details It takes a sudoku file as an input and returns a solved sudoku
    file. The script can be run from the command line with the following
    command:

    python sudoku_solve.py input.txt [solver] [save_file]

    where input.txt is the input sudoku file, [solver] is the optional solver
    argument and [save_file] is the optional argument to save the solved sudoku
    to a file in the same directory as the input file with the following naming
    convention: input_solved.txt.

    The [solver] argument can be one of the following:

    1. bt: backtracking algorithm
    2. cs: constraint satisfaction algorithm
    3. lp: linear programming algorithm

    If no [solver] argument is specified, the script will use the linear
    programming algorithm by default.

    The [save_file] argument can be one of the following:

    1. True: save the solved sudoku to a file
    2. False: do not save the solved sudoku to a file

    If no [save_file] argument is specified, the script will not save the
    solved sudoku to a file by default.

    @param sudoku_file Textfile with unsolved sudoku
    @type sudoku_file Textfile
    @param solver Optional solver argument (bt, cs, lp)
    @type solver str
    @param save_file Optional argument to save the solved sudoku to a file
    (True/False)
    @type save_file bool
    @return sudoku_solution Print the solved sudoku to the terminal
    @return duration Print the duration to the terminal
    @see checkers.is_sudoku_file_valid Function to check if the sudoku file is
    valid
    @see converters.convert_sudoku_txt_to_arr Function to convert the sudoku
    file to an array
    @see checkers.is_sudoku_valid Function to check if the sudoku is valid
    @see back_tracking_solver.solve_sudoku_bt Function to solve the sudoku with
    the backtracking algorithm
    @see constraint_satisfaction_solver.solve_sudoku_cs Function to solve the
    sudoku with the constraint satisfaction algorithm
    @see linear_programming_solver.solve_sudoku_lp Function to solve the sudoku
    with the linear programming algorithm
    @see checkers.is_sudoku_solved Function to check if the sudoku is solved
    @see converters.convert_sudoku_arr_to_txt Function to convert the solved
    sudoku array to text

    Example:

    $ python src/solve_sudoku.py test_resources/easy_1.txt bt True

    Use backtracking solver.
    Solved sudoku in 0.00111 seconds using bt solver.

    Sudoku Solution:

    241|768|539
    573|924|186
    896|531|742
    ---+---+---
    734|295|618
    189|476|325
    652|813|497
    ---+---+---
    465|382|971
    327|159|864
    918|647|253

    Solved sudoku saved to the following file: test_resources/easy_1_solved.txt
    """
    # Record the start time
    start_time = time.time()
    # Check if the input sudoku file is valid
    if not checkers.is_sudoku_file_valid(sudoku_file):
        return None
    # Convert the sudoku file to an array
    sudoku = converters.convert_sudoku_txt_to_arr(sudoku_file)
    # Check if the sudoku is valid
    if not checkers.is_sudoku_valid(sudoku):
        return None
    # Solve the sudoku with specified solver or default solver
    if solver == "bt":
        print("Use backtracking solver.")
        sudoku_solved = back_tracking_solver.solve_sudoku_bt(sudoku)
    elif solver == "cs":
        print("Use constraint satisfaction solver.")
        sudoku_solved = constraint_satisfaction_solver.solve_sudoku_cs(sudoku)
    elif solver == "lp":
        print("Use linear programming solver.")
        sudoku_solved = linear_programming_solver.solve_sudoku_lp(sudoku)
    else:
        print("Invalid solver specified.")
        print("Use default solver (constraint satisfaction solver).")
        sudoku_solved = constraint_satisfaction_solver.solve_sudoku_cs(sudoku)
    # Check if the sudoku was unsolveable
    if sudoku_solved is None:
        return None
    else:
        # Check if the sudoku is valid and solved
        if checkers.is_sudoku_solved(sudoku_solved):
            # Convert the solved Sudoku array back to text
            solution = converters.convert_sudoku_arr_to_txt(sudoku_solved)
            end_time = time.time()  # record the end time
            duration = end_time - start_time  # calculate the duration
            print(f"Solved in {duration:.5f} seconds with {solver} solver.\n")
            print("Sudoku solution:\n")
            print(solution, "\n")
            # Save the solved Sudoku string to a file if save_file is True
            if save_file:
                solved_file = os.path.splitext(sudoku_file)[0] + "_solved.txt"
                with open(solved_file, "w") as file:
                    file.write(solution)
                print(f"Solved sudoku saved to this file: {solved_file}")
        else:
            print("Sudoku solution is invalid or not solved. Returned 'None'.")
            return None
        return solution, duration


# === MAIN ====================================================================


def main():
    """!@brief Parse command line arguments and call solve_sudoku function.

    @details This function parses the command line arguments and calls the
    solve_sudoku function with the specified arguments. It takes the following
    command line arguments:

    1. sudoku_file: The path to the sudoku file to be solved.
    2. solver: Optional solver argument (bt, cs, lp)
    3. save_file: Optional argument to save the solved sudoku to a file
    (True/False)

    If no [solver] argument is specified, the script will use the linear
    programming algorithm by default. If no [save_file] argument is specified,
    the script will not save the solved sudoku to a file by default.
    """
    if len(sys.argv) < 2 or len(sys.argv) > 4:
        print("Usage: python solve_sudoku.py input.txt [solver] [save_file]")
        return

    sudoku_file = sys.argv[1]
    solver = "lp"  # Default solver
    save_file = False  # Default save_file

    if len(sys.argv) >= 3:
        solver = sys.argv[2]

    if len(sys.argv) == 4:
        save_file = True if sys.argv[3].lower() == "true" else False

    solve_sudoku(sudoku_file, solver, save_file)


if __name__ == "__main__":
    main()
