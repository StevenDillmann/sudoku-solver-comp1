import os
import shutil
import re

# flake8: noqa F401
import typing


# === MAIN FUNCTIONS ==========================================================
"""!@file checkers.py
@brief Module containing tools to check if a sudoku file is valid, solveable or
solved.

@details This script takes a sudoku file as an input and returns True if the
sudoku file is valid, if the sudoku puzzle itself is valid or if it is solved.
It returns False otherwise. The sudoku file is valid if it has the correct file
type and content. The sudoku puzsle is valid if it has no duplicates in the
rows, columns or subgrids. The sudoku puzzle is solved if it has no duplicates
or zeros in the rows, columns or subgrids.

@author Created by Steven Dillmann 17/12/2023
"""

# 1. is_sudoku_file_valid


def is_sudoku_file_valid(sudoku_file):
    """!@brief Check if the sudoku file is valid.

    @details This function checks if the sudoku file is valid by checking
    if the file type and content are valid.

    @param sudoku_file The path to the sudoku file
    @type sudoku_file str
    @return valid True if the sudoku file is valid, False otherwise
    @rtype bool
    @see is_file_type_valid Function to check if the file type is valid
    @see is_file_content_valid Function to check if the file content is valid
    """
    # Check if the file type is valid
    if not is_file_type_valid(sudoku_file):
        print("WARNING SUMMARY: INVALID FILE TYPE!\n")
        return False
    # Check if the file content is valid
    if not is_file_content_valid(sudoku_file):
        print("WARNING SUMMARY: INVALID FILE CONTENT!\n")
        return False
    return True


# 2. is_sudoku_valid


def is_sudoku_valid(sudoku_arr):
    """!@brief Check if the sudoku puzzle is valid.

    @details This function checks if the sudoku puzzle is valid by examining
    for duplicates in the rows, columns, or subgrids.

    @param sudoku_arr The sudoku array (list of lists) to check
    @type sudoku_arr list
    @return True if the sudoku is valid, False otherwise
    @rtype bool
    @raises TypeError: If the sudoku array is not a list of lists
    """
    # Check if the sudoku is a list of lists
    if not isinstance(sudoku_arr, list) or not all(
        isinstance(row, list) for row in sudoku_arr
    ):
        raise TypeError("Input Sudoku should be a list of lists.")
    # Store error messages in a list
    error_list = []

    # Check if a list of numbers has duplicates (excluding zeros)
    def check_duplicates(list_of_numbers):
        non_zeros_list = [num for num in list_of_numbers if num != 0]
        return len(non_zeros_list) != len(set(non_zeros_list))

    # Check rows for duplicates
    for row_idx, row in enumerate(sudoku_arr):
        if check_duplicates(row):
            error_list.append(f"Duplicate numbers in row {row_idx + 1}.\n")
    # Check columns for duplicates
    for col in range(9):
        column = [sudoku_arr[row][col] for row in range(9)]
        if check_duplicates(column):
            error_list.append(f"Duplicate numbers in column {col + 1}.\n")
    # Check subgrids for duplicates
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            subgrid = [
                sudoku_arr[a][b]
                for a in range(i, i + 3)
                for b in range(j, j + 3)
            ]
            if check_duplicates(subgrid):
                error_list.append(
                    f"Duplicate numbers in subgrid starting"
                    f"at cell ({i + 1}, {j + 1}).\n"
                )
    # Print error messages if there are any and return False
    if error_list:
        for error_message in error_list:
            print("Error: ", error_message)
        print("WARNING SUMMARY: INVALID SUDOKU!\n")
        return False
    return True


# 3. is_sudoku_solved


def is_sudoku_solved(sudoku_arr):
    """!@brief Check if the sudoku puzzle is solved.

    @details This function checks if the sudoku puzzle is solved by examining
    for duplicates and zeros in the rows, columns, or subgrids.

    @param sudoku_arr The sudoku array (list of lists) to check
    @type sudoku_arr list
    @return True if the sudoku is solved, False otherwise
    @rtype bool
    @raises TypeError If the sudoku array is not a list of lists
    """
    # Check if the sudoku is a list of lists
    if not isinstance(sudoku_arr, list) or not all(
        isinstance(row, list) for row in sudoku_arr
    ):
        raise TypeError("Input Sudoku should be a list of lists.")
    # Store error messages in a list
    error_list = []
    # Check rows and columns for unique numbers and zeros
    for i in range(9):
        row_numbers = set(sudoku_arr[i])
        col_numbers = set(sudoku_arr[j][i] for j in range(9))

        if len(row_numbers) != 9:
            error_list.append(f"Duplicate/missing numbers in row {i+1}.\n")

        if len(col_numbers) != 9:
            error_list.append(f"Duplicate/missing numbers in column {i+1}.\n")
    # Check subgrids for unique numbers and zeros
    for a in range(0, 9, 3):
        for b in range(0, 9, 3):
            subgrid_numbers = set()
            for i in range(3):
                for j in range(3):
                    subgrid_numbers.add(sudoku_arr[a + i][b + j])
            if len(subgrid_numbers) != 9:
                error_list.append(
                    f"Duplicate/missing numbers in subgrid"
                    f"starting at cell ({a+1}, {b+1}).\n"
                )
    if error_list:
        for error_message in error_list:
            print("Error: ", error_message)
        print("WARNING SUMMARY: SUDOKU NOT SOLVED!\n")
        return False
    return True


# === HELPER FUNCTIONS ========================================================

# 1.1 is_file_type_valid


def is_file_type_valid(sudoku_file):
    """!@brief Check if the sudoku file has the correct file type.

    @details This function checks if the sudoku file has the correct file
    type by checking if the file extension is '.txt'.

    @param sudoku_file The path to the sudoku file
    @type sudoku_file str
    @return True if the sudoku file has the correct file type, False
    otherwise
    @rtype bool
    """
    # Get the file name and extension of the sudoku input file
    file_name, file_extension = os.path.splitext(sudoku_file)
    # Check if the extension is .txt
    if file_extension == ".txt":
        return True
    else:
        # Try to create a new file with fixed .txt extension
        print(
            f"Error: The input file '{sudoku_file}' "
            f"does not have the expected '.txt' extension.\n"
        )
        print("Attempting to create a new file with the '.txt' extension...\n")
        fixed_sudoku_file = file_name + "_fixed.txt"
        try:
            shutil.copyfile(sudoku_file, fixed_sudoku_file)
            print(
                "Fixed: Created a new file with the '.txt' extension:"
                f"'{fixed_sudoku_file}'.\n"
            )
            print("Please use this new file as input.\n")
        # Print an error message if creating the new file fails
        except Exception as e:
            print(f"Error: Failed due to the following error: {e}.\n")
            print(
                "Make sure the input has the correct file extension: '.txt'\n"
            )
        return False


# 1.2 is_file_content_valid


def is_file_content_valid(sudoku_file):
    """!@brief Check if the sudoku file has the correct file content.

    @details This function checks if the sudoku file has the correct file
    content by checking if the file content matches the expected format.

    @param sudoku_file The path to the sudoku file
    @type sudoku_file str
    @return True if the sudoku file has the correct file content, False
    otherwise
    @rtype bool
    """
    # Define the format of the grid lines
    numbered_lines_format = r"^[0-9]{3}\|[0-9]{3}\|[0-9]{3}$"
    separator_lines_format = "---+---+---"
    # Read the sudoku file and split it into lines
    with open(sudoku_file, "r") as file:
        sudoku_txt = file.read()
        sudoku_lines = sudoku_txt.split("\n")
        # Check for leading or trailing whitespace and fix if needed
        fixed_sudoku_lines = [line.strip() for line in sudoku_lines]
        if sudoku_lines != fixed_sudoku_lines:
            print("Error: Leading/trailing white space detected.\n")
        # Check for leading or trailing empty lines and fix if needed
        leading_whitespace = False
        trailing_whitespace = False
        while fixed_sudoku_lines and not fixed_sudoku_lines[0]:
            fixed_sudoku_lines.pop(0)
            leading_whitespace = True
        while fixed_sudoku_lines and not fixed_sudoku_lines[-1]:
            fixed_sudoku_lines.pop()
            trailing_whitespace = True
        if leading_whitespace:
            print("Error: Leading empty lines detected.\n")
        if trailing_whitespace:
            print("Error: Trailing empty lines detected.\n")
        # Check the number of lines
        if len(fixed_sudoku_lines) != 11:
            print("Error: Incorrect number of lines in the file.\n")
            print("Make sure the input file matches the following format:")
            print(
                """
            xxx|xxx|xxx
            xxx|xxx|xxx
            xxx|xxx|xxx
            ---+---+---
            xxx|xxx|xxx
            xxx|xxx|xxx
            xxx|xxx|xxx
            ---+---+---
            xxx|xxx|xxx
            xxx|xxx|xxx
            xxx|xxx|xxx
            """
            )
            return False
        # Check the numbered lines for the expected format
        for i, line in enumerate(fixed_sudoku_lines):
            if i not in {3, 7} and not re.match(numbered_lines_format, line):
                print(f"Error: Line {i + 1} doesn't match expected format.\n")
                print("Make sure the input file matches the following format:")
                print(
                    """
                xxx|xxx|xxx
                xxx|xxx|xxx
                xxx|xxx|xxx
                ---+---+---
                xxx|xxx|xxx
                xxx|xxx|xxx
                xxx|xxx|xxx
                ---+---+---
                xxx|xxx|xxx
                xxx|xxx|xxx
                xxx|xxx|xxx
                """
                )
                return False
        # Check for incorrect separator lines and fix if needed
        for i, line in enumerate(fixed_sudoku_lines):
            if i in {3, 7} and line != separator_lines_format:
                print(f"Error: Line {i + 1} doesn't match expected format.\n")
                fixed_sudoku_lines[i] = separator_lines_format
        # Check if any fixes were made
        if sudoku_lines != fixed_sudoku_lines:
            print("Attempting to create a new file with the issues fixed...\n")
            fixed_sudoku_file = sudoku_file.replace(".txt", "_fixed.txt")
            with open(fixed_sudoku_file, "w") as fixed_file:
                fixed_file.write("\n".join(fixed_sudoku_lines))
            print(
                f"Fixed: Created a new file with the issues fixed:"
                f"'{fixed_sudoku_file}'.\n"
            )
            print("Please use this new file as input.\n")
            return False
    return True
