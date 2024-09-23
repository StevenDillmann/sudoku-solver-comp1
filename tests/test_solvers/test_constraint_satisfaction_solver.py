from src.solvers import constraint_satisfaction_solver
from src.processors import converters
import pytest

# === TEST EXAMPLE DEFINITIONS ================================================

sudoku_solved = converters.convert_sudoku_txt_to_arr(
    "tests_resources/sudoku_valid_solved.txt"
)

easy_solved = converters.convert_sudoku_txt_to_arr(
    "tests_resources/easy_1_solved.txt"
)

medium_solved = converters.convert_sudoku_txt_to_arr(
    "tests_resources/medium_1_solved.txt"
)

hard_solved = converters.convert_sudoku_txt_to_arr(
    "tests_resources/hard_1_solved.txt"
)

# === MAIN FUNCTION TESTS =====================================================
"""!@file test_constraint_satisfaction_solver.py
    @brief Module containing tests for the constraint_satisfaction_solver
    module.

    @details This script contains tests for the constraint_satisfaction_solver
    module. It tests the following function: solve_sudoku_cs.
    The tests are parametrised to test a variety of different inputs. The test
    resources are located in the tests_resources folder.

    @author Created by Steven Dillmann 17/12/2023
"""

# 1. Test solve_sudoku_cs


@pytest.mark.parametrize(
    "sudoku_files, expected_solved",
    [
        ("tests_resources/sudoku_valid_not_yet_solved.txt", sudoku_solved),
        ("tests_resources/easy_1.txt", easy_solved),
        ("tests_resources/medium_1.txt", medium_solved),
        ("tests_resources/hard_1.txt", hard_solved),
        ("tests_resources/sudoku_valid_unsolveable.txt", None),
        ("tests_resources/sudoku_valid_rules_invalid.txt", None),
    ],
)
def test_solve_sudoku_cs(sudoku_files, expected_solved):
    """!@brief Test solve_sudoku_cs function.

    @details This function tests the solve_sudoku_cs function. It
    tests the following cases:

    1. Test solve_sudoku_bt with a valid sudoku that is not yet solved.
    2. Test solve_sudoku_bt with a easy sudoku that is not yet solved.
    3. Test solve_sudoku_bt with a medium sudoku that is not yet solved.
    4. Test solve_sudoku_bt with a hard sudoku that is not yet solved.
    5. Test solve_sudoku_bt with a sudoku that is unsolveable.
    6. Test solve_sudoku_bt with a sudoku that is invalid.

    @param sudoku_files The path to the sudoku file to be solved.
    @type sudoku_files str
    @param expected_solved The expected solved sudoku.
    @type expected_solved list of lists or None
    @return assertion True if the solved sudoku is equal to the expected solved
    sudoku. Or if the sudoku is unsolvable or invalid, then the solved sudoku
    should be None.
    """
    sudoku_not_yet_solved = converters.convert_sudoku_txt_to_arr(sudoku_files)
    assert (
        constraint_satisfaction_solver.solve_sudoku_cs(sudoku_not_yet_solved)
        == expected_solved
    )
