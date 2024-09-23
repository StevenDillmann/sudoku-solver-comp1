import os
import sys


def save_sudokus(sudoku_category_file):
    # Extract filename without extension
    category_name = os.path.splitext(os.path.basename(sudoku_category_file))[0]
    directory_path = os.path.dirname(sudoku_category_file)
    full_category_name = os.path.join(directory_path, category_name)
    # Create a directory for the sudokus
    if not os.path.exists(full_category_name):
        os.makedirs(full_category_name)
    # Read the file
    with open(sudoku_category_file, "r") as file:
        sudokus = file.read().splitlines()

    # Define a function to format and save sudoku puzzles
    def save_sudoku(idx, puzzle):
        sudoku_name = os.path.join(
            full_category_name, f"{category_name}_{idx}.txt"
        )
        formatted = [
            f"{puzzle[i:i+3]}|{puzzle[i+3:i+6]}|{puzzle[i+6:i+9]}"
            for i in range(0, 81, 9)
        ]
        formatted.insert(3, "---+---+---")
        formatted.insert(7, "---+---+---")
        formatted_sudoku = "\n".join(formatted)

        with open(sudoku_name, "w") as output_file:
            output_file.write(formatted_sudoku)

    # Parse each sudoku and save as separate file
    for idx, sudoku in enumerate(sudokus):
        save_sudoku(idx + 1, sudoku)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python sudoku_parser.py <sudoku_group_file>")
        sys.exit(1)

    sudoku_category_file = sys.argv[1]
    save_sudokus(sudoku_category_file)
