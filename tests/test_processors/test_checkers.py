from src.processors import checkers, converters
import pytest

# === MAIN FUNCTION TESTS =====================================================
"""!@file test_checkers.py
    @brief Module containing tests for the checkers module.

    @details This script contains tests for the checkers module. It tests the
    following functions: is_sudoku_file_valid, is_sudoku_valid,
    is_sudoku_solved. The tests are parametrised to test a variety of
    different inputs. The test resources are located in the tests_resources
    folder.

    @author Created by Steven Dillmann 17/12/2023
"""

# 1. Test is_sudoku_file_valid


@pytest.mark.parametrize(
    "sudoku_files_valid, expected_valid",
    [
        ("tests_resources/sudoku_valid_solveable.txt", True),
        ("tests_resources/sudoku_valid_not_yet_solved.txt", True),
        ("tests_resources/sudoku_valid_solved.txt", True),
        ("tests_resources/sudoku_valid_solved_rules_invalid.txt", True),
        ("tests_resources/sudoku_valid_rules_invalid.txt", True),
        ("tests_resources/sudoku_valid_unsolveable.txt", True),
        ("tests_resources/sudoku_invalid_bad_file_type_docx.docx", False),
        ("tests_resources/sudoku_invalid_bad_file_type_md.md", False),
        ("tests_resources/sudoku_invalid_bad_file_type_pdf.pdf", False),
        ("tests_resources/sudoku_invalid_bad_file_type_docx_fixed.txt", True),
        ("tests_resources/sudoku_invalid_bad_file_type_md_fixed.txt", True),
        ("tests_resources/sudoku_invalid_bad_file_type_pdf_fixed.txt", True),
        ("tests_resources/sudoku_invalid_bad_numbered_lines.txt", False),
        ("tests_resources/sudoku_invalid_bad_separator_lines.txt", False),
        ("tests_resources/sudoku_invalid_bad_separator_lines_fixed.txt", True),
        ("tests_resources/sudoku_invalid_extra_character_line.txt", False),
        ("tests_resources/sudoku_invalid_extra_sudoku_line.txt", False),
        ("tests_resources/sudoku_invalid_leading_empty_lines.txt", False),
        ("tests_resources/sudoku_invalid_leading_empty_lines_fixed.txt", True),
        ("tests_resources/sudoku_invalid_leading_white_space.txt", False),
        ("tests_resources/sudoku_invalid_leading_white_space_fixed.txt", True),
        ("tests_resources/sudoku_invalid_trailing_empty_lines.txt", False),
        (
            "tests_resources/sudoku_invalid_trailing_empty_lines_fixed.txt",
            True,
        ),
        ("tests_resources/sudoku_invalid_trailing_white_space.txt", False),
        (
            "tests_resources/sudoku_invalid_trailing_white_space_fixed.txt",
            True,
        ),
        ("tests_resources/sudoku_invalid_middle_empty_lines.txt", False),
        ("tests_resources/sudoku_invalid_middle_empty_lines_fixed.txt", True),
    ],
)
def test_is_sudoku_file_valid(sudoku_files_valid, expected_valid):
    """!@brief Test is_sudoku_file_valid function.

    @details This function tests the is_sudoku_file_valid function. It
    tests the following cases:

    1. Test is_sudoku_file_valid with a valid sudoku file that is solveable.
    2. Test is_sudoku_file_valid with a valid sudoku file that is not yet
    solved.
    3. Test is_sudoku_file_valid with a valid sudoku file that is solved.
    4. Test is_sudoku_file_valid with a valid sudoku file that is solved but
    has invalid rules.
    5. Test is_sudoku_file_valid with a valid sudoku file that is unsolveable.
    6. Test is_sudoku_file_valid with a valid sudoku file that has invalid
    rules.
    7. Test is_sudoku_file_valid with a invalid sudoku file that is a docx.
    8. Test is_sudoku_file_valid with a invalid sudoku file that is a md.
    9. Test is_sudoku_file_valid with a invalid sudoku file that is a pdf.
    10. Test is_sudoku_file_valid with a invalid sudoku file that was a docx
    but has a fixed file extension.
    10. Test is_sudoku_file_valid with a invalid sudoku file that was a md
    but has a fixed file extension.
    12. Test is_sudoku_file_valid with a invalid sudoku file that was a pdf
    but has a fixed file extension.
    13. Test is_sudoku_file_valid with a invalid sudoku file that has bad
    numbered lines.
    14. Test is_sudoku_file_valid with a invalid sudoku file that has bad
    separator lines.
    15. Test is_sudoku_file_valid with a invalid sudoku file that has bad
    separator lines but has been fixed.
    16. Test is_sudoku_file_valid with a invalid sudoku file that has extra
    characters in a line.
    17. Test is_sudoku_file_valid with a invalid sudoku file that has extra
    sudoku lines.
    18. Test is_sudoku_file_valid with a invalid sudoku file that has leading
    empty lines.
    19. Test is_sudoku_file_valid with a invalid sudoku file that had leading
    empty lines but has been fixed.
    20. Test is_sudoku_file_valid with a invalid sudoku file that has leading
    white space.
    21. Test is_sudoku_file_valid with a invalid sudoku file that had leading
    white space but has been fixed.
    22. Test is_sudoku_file_valid with a invalid sudoku file that has trailing
    empty lines.
    23. Test is_sudoku_file_valid with a invalid sudoku file that had trailing
    empty lines but has been fixed.
    24. Test is_sudoku_file_valid with a invalid sudoku file that has trailing
    white space.
    25. Test is_sudoku_file_valid with a invalid sudoku file that had trailing
    white space but has been fixed.
    26. Test is_sudoku_file_valid with a invalid sudoku file that has middle
    empty lines.
    27. Test is_sudoku_file_valid with a invalid sudoku file that had middle
    empty lines but has been fixed.

    @param sudoku_files_valid The path to the sudoku text file
    @type sudoku_files_valid str
    @param expected_valid The expected validity of the sudoku text file
    @type expected_valid bool
    @return assertion True if the sudoku text file is valid. False otherwise.
    """
    assert checkers.is_sudoku_file_valid(sudoku_files_valid) == expected_valid


# 2. Test is_sudoku_valid


@pytest.mark.parametrize(
    "sudoku_valid, expected_valid",
    [
        ("tests_resources/sudoku_valid_solveable.txt", True),
        ("tests_resources/sudoku_valid_rules_invalid.txt", False),
        ("tests_resources/sudoku_valid_solved_rules_invalid.txt", False),
    ],
)
def test_is_sudoku_valid(sudoku_valid, expected_valid):
    """!@brief Test is_sudoku_valid function.

    @details This function tests the is_sudoku_valid function. It tests the
    following cases:

    1. Test is_sudoku_valid with a sudoku that is solveable.
    2. Test is_sudoku_valid with a sudoku that has invalid rules.
    3. Test is_sudoku_valid with a sudoku that is solved but has invalid
    rules.

    @param sudoku_files_solveable The path to the sudoku file to be solved.
    @type sudoku_files_solveable str
    @param expected_solveable The expected validity of the sudoku.
    @type expected_solveable bool
    @return assertion True if the sudoku is valid. False otherwise.
    """
    sudoku_arr = converters.convert_sudoku_txt_to_arr(sudoku_valid)
    assert checkers.is_sudoku_valid(sudoku_arr) == expected_valid


# 3. Test is_sudoku_solved


@pytest.mark.parametrize(
    "sudoku_files_solved, expected_solved",
    [
        ("tests_resources/sudoku_valid_solved.txt", True),
        ("tests_resources/sudoku_valid_not_yet_solved.txt", False),
        ("tests_resources/sudoku_valid_solved_rules_invalid.txt", False),
        ("tests_resources/easy_1.txt", False),
        ("tests_resources/medium_1.txt", False),
        ("tests_resources/hard_1.txt", False),
        ("tests_resources/easy_1_solved.txt", True),
        ("tests_resources/medium_1_solved.txt", True),
        ("tests_resources/hard_1_solved.txt", True),
    ],
)
def test_is_sudoku_solved(sudoku_files_solved, expected_solved):
    """!@brief Test is_sudoku_solved function.

    @details This function tests the is_sudoku_solved function. It tests the
    following cases:

    1. Test is_sudoku_solved with a sudoku that is solved.
    2. Test is_sudoku_solved with a sudoku that is not yet solved.
    3. Test is_sudoku_solved with a sudoku that is solved but has invalid
    rules.
    4. Test is_sudoku_solved with a easy sudoku that is not yet solved.
    5. Test is_sudoku_solved with a medium sudoku that is not yet solved.
    6. Test is_sudoku_solved with a hard sudoku that is not yet solved.
    7. Test is_sudoku_solved with a easy sudoku that is solved.
    8. Test is_sudoku_solved with a medium sudoku that is solved.
    9. Test is_sudoku_solved with a hard sudoku that is solved.

    @param sudoku_files_solved The path to the sudoku file to be solved.
    @type sudoku_files_solved str
    @param expected_solved The expected validity of the sudoku.
    @type expected_solved bool
    @return assertion True if the sudoku is solved. False otherwise.
    """
    sudoku_arr = converters.convert_sudoku_txt_to_arr(sudoku_files_solved)
    assert checkers.is_sudoku_solved(sudoku_arr) == expected_solved
