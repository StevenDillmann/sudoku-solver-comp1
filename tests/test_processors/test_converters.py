from src.processors import converters
import pytest

# === TEST EXAMPLE DEFINITIONS ================================================

sudoku_not_yet_solved_arr = [
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

with open("tests_resources/sudoku_valid_not_yet_solved.txt", "r") as file:
    sudoku_not_yet_solved_txt = file.read()

sudoku_solved_arr = [
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

with open("tests_resources/sudoku_valid_solved.txt", "r") as file:
    sudoku_solved_txt = file.read()

sudoku_unsolved_arr = [
    [3, 8, 2, 6, 1, 9, 5, 7, 5],
    [5, 9, 4, 7, 3, 8, 6, 2, 1],
    [1, 7, 6, 4, 2, 5, 9, 3, 8],
    [8, 6, 3, 9, 4, 1, 7, 5, 2],
    [4, 5, 7, 2, 6, 3, 1, 8, 9],
    [9, 2, 1, 8, 5, 7, 3, 6, 4],
    [7, 3, 8, 5, 9, 4, 2, 1, 6],
    [2, 4, 5, 1, 7, 6, 8, 9, 3],
    [6, 1, 9, 3, 8, 2, 5, 4, 7],
]

with open(
    "tests_resources/sudoku_valid_solved_rules_invalid.txt", "r"
) as file:
    sudoku_unsolved_txt = file.read()
    print(sudoku_unsolved_txt)

# === MAIN FUNCTION TESTS =====================================================
"""!@file test_converters.py
    @brief Module containing tests for the converters module.

    @details This script contains tests for the converters module. It tests the
    following functions: convert_sudoku_txt_to_arr, convert_sudoku_arr_to_txt.
    The tests are parametrised to test a variety of different inputs. The test
    resources are located in the tests_resources folder.

    @author Created by Steven Dillmann 17/12/2023
"""

# 1. Test convert_sudoku_txt_to_arr


@pytest.mark.parametrize(
    "sudoku_txt, expected_sudoku_arr",
    [
        (
            "tests_resources/sudoku_valid_not_yet_solved.txt",
            sudoku_not_yet_solved_arr,
        ),
        ("tests_resources/sudoku_valid_solved.txt", sudoku_solved_arr),
        (
            "tests_resources/sudoku_valid_solved_rules_invalid.txt",
            sudoku_unsolved_arr,
        ),
    ],
)
def test_convert_sudoku_txt_to_arr(sudoku_txt, expected_sudoku_arr):
    """!@brief Test convert_sudoku_txt_to_arr function.

    @details This function tests the convert_sudoku_txt_to_arr function. It
    tests the following cases:

    1. Test convert_sudoku_txt_to_arr with a valid sudoku that is not yet
    solved.
    2. Test convert_sudoku_txt_to_arr with a valid sudoku that is solved.
    3. Test convert_sudoku_txt_to_arr with a valid sudoku that is solved but
    has invalid rules.

    @param sudoku_txt The sudoku txt file to convert to an array.
    @type sudoku_txt str
    @param expected_sudoku_arr The expected sudoku array.
    @type expected_sudoku_arr list of lists

    @return assertion True if the sudoku array is equal to the expected sudoku
    array. False otherwise.
    """
    assert (
        converters.convert_sudoku_txt_to_arr(sudoku_txt) == expected_sudoku_arr
    )


# 2. Test convert_sudoku_arr_to_txt


@pytest.mark.parametrize(
    "sudoku_arr, expected_sudoku_txt",
    [
        (sudoku_not_yet_solved_arr, sudoku_not_yet_solved_txt),
        (sudoku_solved_arr, sudoku_solved_txt),
        (sudoku_unsolved_arr, sudoku_unsolved_txt),
    ],
)
def test_convert_sudoku_arr_to_txt(sudoku_arr, expected_sudoku_txt):
    """!@brief Test convert_sudoku_arr_to_txt function.

    @details This function tests the convert_sudoku_arr_to_txt function. It
    tests the following cases:

    1. Test convert_sudoku_arr_to_txt with a sudoku that is not yet
    solved.
    2. Test convert_sudoku_arr_to_txt with a sudoku that is solved.
    3. Test convert_sudoku_arr_to_txt with a sudoku that is solved but
    has invalid rules.

    @param sudoku_arr The sudoku array to convert to a txt file.
    @type sudoku_arr list of lists
    @param expected_sudoku_txt The expected sudoku txt file.
    @type expected_sudoku_txt str

    @return assertion True if the sudoku txt file is equal to the expected
    sudoku txt file. False otherwise.
    """
    print(converters.convert_sudoku_arr_to_txt(sudoku_arr))
    assert (
        converters.convert_sudoku_arr_to_txt(sudoku_arr) == expected_sudoku_txt
    )
