import textwrap

# flake8: noqa F401
import typing

# === MAIN FUNCTIONS ==========================================================
"""!@file converters.py
@brief Module containing tools to convert a sudoku text file to a sudoku array
(list of lists) and vice versa.

@details This script takes a sudoku text file as an input and returns a sudoku
array (list of lists) and vice versa.

@author Created by Steven Dillmann 17/12/2023
"""

# 1. convert_sudoku_txt_to_arr


def convert_sudoku_txt_to_arr(sudoku_txt: str) -> list:
    """!@brief Converts a sudoku text file to a sudoku array (list of lists).

    @details Converts a sudoku text file with a content of format\n

    xxx|xxx|xxx\n
    xxx|xxx|xxx\n
    xxx|xxx|xxx\n
    ---+---+---\n
    xxx|xxx|xxx\n
    xxx|xxx|xxx\n
    xxx|xxx|xxx\n
    ---+---+---\n
    xxx|xxx|xxx\n
    xxx|xxx|xxx\n
    xxx|xxx|xxx\n

    to a sudoku array (list of lists).

    @param sudoku_txt The path to the sudoku text file
    @type sudoku_txt str
    @return sudoku_arr The sudoku array (list of lists)
    @rtype list of lists
    @raises FileNotFoundError If the sudoku text file does not exist
    """
    # Check if the sudoku text file exists
    try:
        # Open the file in read mode
        with open(sudoku_txt, "r") as file:
            # Read sudoku text and split into lines
            sudoku_txt = file.read()
            sudoku_lines = sudoku_txt.split("\n")
            # Remove separator rows ('---+---+---')
            sudoku_lines = [line for line in sudoku_lines if "+" not in line]
            # Create sudoku array and return by iterating over each line
            sudoku_arr = []
            for line in sudoku_lines:
                line = line.replace("|", "")  # remove '|' separators
                row = [int(char) for char in line]
                sudoku_arr.append(row)
        return sudoku_arr
    except FileNotFoundError:
        raise FileNotFoundError("Sudoku text file does not exist.\n")


# 2. convert_sudoku_arr_to_txt


def convert_sudoku_arr_to_txt(sudoku_arr: list) -> str:
    """!@brief Converts a sudoku array (list of lists) to a sudoku text file.

    @details Converts a sudoku array (list of lists) to a sudoku text with a
    content of format

    xxx|xxx|xxx\n
    xxx|xxx|xxx\n
    xxx|xxx|xxx\n
    ---+---+---\n
    xxx|xxx|xxx\n
    xxx|xxx|xxx\n
    xxx|xxx|xxx\n
    ---+---+---\n
    xxx|xxx|xxx\n
    xxx|xxx|xxx\n
    xxx|xxx|xxx\n

    @param sudoku_arr The sudoku array (list of lists)
    @type sudoku_arr list of lists
    @return sudoku_txt The sudoku text file
    @rtype str
    @raises ValueError If the sudoku array is empty
    @raises ValueError If the sudoku array is not 9x9
    """
    # Check if the sudoku array is empty
    if not sudoku_arr:
        raise ValueError("Sudoku array is empty.\n")
    # Check if the sudoku array is 9x9
    if len(sudoku_arr) != 9 or len(sudoku_arr[0]) != 9:
        raise ValueError("Sudoku array is not 9x9.\n")
    # Initialise the sudoku text
    sudoku_txt = ""
    # Create sudoku text by iterating over each row
    for row in sudoku_arr:
        line = "".join(str(num) for num in row)
        line = "|".join(textwrap.wrap(line, width=3))  # insert '|' separators
        sudoku_txt += line + "\n"
    # Insert separator rows ('---+---+---')
    sudoku_lines = sudoku_txt.split("\n")
    sudoku_lines.insert(3, "---+---+---")
    sudoku_lines.insert(7, "---+---+---")
    sudoku_txt = "\n".join(sudoku_lines[:-1])  # exclude the last empty line
    return sudoku_txt
