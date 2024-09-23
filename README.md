
# C1 Research Computing Coursework Submission (sd2022)

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

## Description
This project is associated with the submission of the coursework for the C1 Research Computing Module as part of the MPhil in Data Intensive Science at the University of Cambridge. The Coursework Instructions can be found under [Instructions.md](Instructions.md). The associated project report can be found under [C1 Coursework Report](report/c1_sd2022_report.pdf).

This project presents a sudoku solver written in Python, that takes as an input a not yet solved sudoku in the form of a text file `input.txt` of a 9x9 sudoku puzzle with zero representing unknown values and `|`,`+`,`-` separating cells, i.e.:

```
$ cat input.txt
000|007|000
000|009|504
000|050|169
---+---+---
080|000|305
075|000|290
406|000|080
---+---+---
762|080|000
103|900|000
000|600|000
```

and outputs the solved sudoku puzzle to the terminal in the same form, including the elapsed time taken to solve the sudoku puzzle, with the option to save the sudoku in a new file.

The sudoku solver offers the following additional functionalities:

1. The sudoku solver informs the user if the file type or content is invalid, if the input sudoku puzzle is invalid according to [sudoku rules](https://sudoku.com/how-to-play/sudoku-rules-for-complete-beginners/#:~:text=Sudoku%20is%20played%20on%20a,the%20row%2C%20column%20or%20square.) or is [unsolveable](https://www.sudokudragon.com/unsolvable.htm). It __does not__ inform the user if the sudoku is [improper](https://masteringsudoku.com/can-sudoku-have-multiple-solutions/), i.e. if the sudoku does not have a unique solution.

2. The sudoku solver detects bad input files, attempts to fix them and if successful saves the fixed sudoku to a file in the same directory as the input file with the following naming convention: input_fixed.txt.

3. The sudoku solver offers a range of solving algorithms, including [backtracking](https://en.wikipedia.org/wiki/Sudoku_solving_algorithms#Backtracking), [constraint satisfaction](https://en.wikipedia.org/wiki/Sudoku_solving_algorithms#Constraint_programming) (backtracking + elimination constraint), and [linear programming](https://en.wikipedia.org/wiki/Sudoku_solving_algorithms#Stochastic_search_/_optimization_methods), empowering users to choose the most suitable strategy for different sudoku difficulty levels.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Support](#support)
- [License](#license)
- [Documentation](#documentation)
- [Data Availability](#data-availability)
- [Project Status](#project-status)
- [Authors and Acknowledgment](#authors-and-acknowledgment)

## Installation

To get started with the sudoku solver, follow these steps:

### Requirements

- Python 3.9 or higher installed on your system.
- Conda installed (for managing the Python environment).
- Docker (if using containerisation for deployment).

### Steps

#### Local Setup (Without Docker)

1. **Clone the Repository:**

    Clone the repository to your local machine with the following command:

    ```
    $ git clone https://gitlab.developers.cam.ac.uk/phy/data-intensive-science-mphil/c1_assessment/sd2022
    ```
    or simply download it from [C1 Research Computing Coursework (sd2022)](https://gitlab.developers.cam.ac.uk/phy/data-intensive-science-mphil/c1_assessment/sd2022).

2. **Navigate to the Project Directory:**

    On your local machine, navigate to the project directory with the following command:

    ```
    $ cd /full/path/to/sd2022
    ```

    and replace `/full/path/to/` with the directory on your local machine where the repository lives in.

3. **Setting up the Environment:**

    Set up and activate the environment with the following command:

    ```
    $ conda env create -f environment.yml
    $ conda activate sd2022_c1_env
    ```

#### Using Docker (Recommended for Containerised Deployment)

1. **Clone the Repository:**

    Clone the repository to your local machine with the following command:

    ```
    $ git clone https://gitlab.developers.cam.ac.uk/phy/data-intensive-science-mphil/c1_assessment/sd2022
    ```

    or simply download it from [C1 Research Computing Coursework (sd2022)](https://gitlab.developers.cam.ac.uk/phy/data-intensive-science-mphil/c1_assessment/sd2022).

2. **Navigate to the Project Directory:**

    On your local machine, navigate to the project directory with the following command:

    ```
    $ cd /full/path/to/sd2022
    ```

    and replace `/full/path/to/` with the directory on your local machine where the repository lives in.

3. **Install and Run Docker:**

    You can install Docker from the official webpage under [Docker Download](https://www.docker.com/).
    Once installed, make sure to run the Docker application.

4. **Build the Docker Image:**

    You can build a Docker image with the following command:

    ```
    $ docker build -t [image] .
    ```

    and replace `[image]` with the name of the image you want to build.


## Usage

### Usability

#### Local Usage (Without Docker)

The script can be run from the command line with the following command (assuming you are in the directory `/full/path/to/sd2022`):

```
$ python src/solve_sudoku.py input.txt [solver] [save_file]
```

where `input.txt` is the input sudoku file, `[solver]` is the optional solver argument and `[save_file]` is the optional argument to save the solved sudoku to a file in the same directory as the input file with the following naming convention: `input_solved.txt`.

The `[solver]` argument can be one of the following:

1. bt: backtracking algorithm
2. cs: constraint satisfaction algorithm
3. lp: linear programming algorithm

If no or an invalid `[solver]` argument is specified, the script will use the linear programming algorithm by default.

The `[save_file]` argument can be one of the following:

1. True: save the solved sudoku to a file
2. False: do not save the solved sudoku to a file

If no `[save_file]` argument is specified, the script will not save the solved sudoku to a file by default.

#### Using Docker (Recommended for Containerised Deployment)

Once Docker is running and you created an image, follow the next steps to run the script within Docker.

**Run script on an existing input file in the Docker Container:**

If you want to run `solve_sudoku.py` on an input file within the Docker container, first
create and run a container with the following command:

```
$ docker run -it --name=[container] [image]
```
and replace `[container]` with the container name and `[image]` with the image name you created. Then simply run
the script with the following command:

```
$ python src/solve_sudoku.py tests_resources/input.txt [solver] [save_file]
```

where `input.txt` is the input sudoku file within the container, `[solver]` is the optional solver argument and `[save_file]` is the optional argument to save the solved sudoku to a file in the same directory as the input file with the following naming convention: `input_solved.txt`.

**Run script on any input file outside the Docker Container:**

If you want to run `solve_sudoku.py` on an input file outside the Docker container, first create and run a container and link the file on your local machine with the container with the following command:

```
$ docker run -it --name=[container] -v /path/to/input_out.txt:/sd2022/tests_resources/input_out.txt [image]
```

and replace `[container]` with the container name and `[image]` with the image name you created. Then simply run
the script with the following command:

```
$ python src/solve_sudoku.py tests_resources/input_out.txt [solver] [save_file]
```

where `input_out.txt` is the input sudoku file linked to the container, `[solver]` is the optional solver argument and `[save_file]` is the optional argument to save the solved sudoku to a file in the same directory as the input file with the following naming convention: `input_out_solved.txt`.

### Example:

Let's run the sudoku solver on on of the test files located in `sd2022/tests_resources` from the command line:

File:

```
$ cat sd2022/tests_resources/easy_1.txt
000|007|000
000|009|504
000|050|169
---+---+---
080|000|305
075|000|290
406|000|080
---+---+---
762|080|000
103|900|000
000|600|000
```

Run sudoku solver:

```
$ python src/solve_sudoku.py tests_resources/easy_1.txt bt True
```

Output:

```
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

Solved sudoku saved to the following file: tests_resources/easy_1_solved.txt
```

### Demonstration on how to use the sudoku solver from the Terminal:

The demonstration below shows how to run the sudoku solver from the command line:

![utils/sudoku_demonstration.gif](utils/sudoku_demonstration.gif)

## Features

### Core Functionalities

The sudoku solver effectively solves any valid and solveable 9x9 sudoku puzzles and measures the elapsed time taken to solve it.

### Key Functionalities

#### `processors` package

The `processors` package includes the `checkers` and `converters` modules.

- `checkers` module:

    The `checkers` module takes a sudoku file as an input and returns True if the sudoku file is valid, if the sudoku puzzle itself is valid or if it is solved. It returns False otherwise. The sudoku file is valid if it has the correct file type and content. The sudoku puzsle is valid if it has no duplicates in the rows, columns or subgrids. The sudoku puzzle is solved if it has no duplicates or zeros in the rows, columns or subgrids.

- `converters` module:

    The `converters` module takes a sudoku text file as an input and returns a sudoku array (list of lists) and vice versa.

#### `solvers` package

The `solvers` package includes the `back_tracking_solver`, `constraint_satisfaction_solver` and `linear_programming_solver`.

- `back_tracking_solver`:

    The `back_tracking_solver` takes a sudoku array (list of lists) as an input and returns a solved sudoku array (list of lists) using the backtracking algorithm.

- `constraint_satisfaction_solver`:

    The `constraint_satisfaction_solver` takes a sudoku array (list of lists) as an input and returns a solved sudoku array (list of lists) using the backtracking algorithm including an elimination constraint.

- `linear_programming_solver`:

    The `linear_programming_solver` takes a sudoku array (list of lists) as an input and returns a solved sudoku array (list of lists) using the linear programming algorithm.

### Special Abilities

**Sudoku File and Puzzle Validation:**

The sudoku solver informs the user if the file type or content is invalid, if the input sudoku puzzle is invalid according to sudoku rules or is unsolveable.

**Sudoku File Fixing:**

The sudoku solver detects bad input files, attempts to fix them and if successful saves the fixed sudoku to a file in the same directory as the input file with the following naming convention: input_fixed.txt.

**Sudoku Algorithm Selection:**

The sudoku solver offers a range of solving algorithms: backtracking, constraint satisfaction, and linear programming, empowering users to choose the most suitable strategy for different sudoku difficulty levels.

The recommended solver algorithm depends on the difficulty level of the sudoku:

| Sudoku Puzzle Difficulty | Initial Sudoku Numbers | Recommended Sudoku Solver |
|----------|----------|----------|
| Easy | ~45 initial numbers | Constraint Satisfaction |
| Medium | ~35 initial numbers | Constraint Satisfaction |
| Hard | ~25 initial numbers | Linear Programming |
| Extreme | <20 initial numbers | Linear Programming |
| Default Solver: Linear Programming |

## Frameworks

- **Programming Languages:** Python
- **Testing Frameworks:** pytest
- **CI/CD:** -
- **Containerisation:** Docker

## Support
For any questions, feedback, or assistance, please feel free to reach out via email at [sd2022@cam.ac.uk](sd2022@cam.ac.uk).

## License
This project is licensed under the [MIT License](https://opensource.org/license/mit/) - see the [LICENSE](LICENSE) file for details.

## Documentation
A documentation of the code can be generated with [Doxygen](https://www.doxygen.nl/). Make sure you have Doxygen installed:

```
$ brew install doxygen # for Mac
Win/Linux: https://www.doxygen.nl/manual/install.html or https://www.doxygen.nl/download.html
```

Navigate to the `docs` documentation folder with:

```
$ cd docs
```

Then build the documentation with:

```
$ doxygen
```

Navigate to the generated `latex` folder with:

```
$ cd latex
```

The build the latex into a PDF document with:

```
$ make
```

You can now view the generated documentation in PDF format under `refman.pdf`.

## Data Availability

The data used in the default algorithm selection study in the [C1 Coursework Report](report/c1_sd2022_report.pdf) is stored in
[Google-Drive-C1-Submission-Data](https://drive.google.com/drive/folders/1IG4CmGPqNPPf0LOCNBbgdu_RGJV8Dlk4?usp=drive_link).

## Project Status
The project is in a state ready for submission. All essential features have been implemented, and the codebase is stable. Future updates may focus on minor improvements, bug fixes, or optimisations.

## Note on the Use of auto-generation tools
GitHub Co-Pilot assisted the author in producing all function docstrings present in the project repository. No specific commands have been given, instead auto-completion suggestions have occasionally been accepted.

## Authors and Acknowledgment
This project is maintained by [Steven Dillmann](https://www.linkedin.com/in/stevendillmann/) at the University of Cambridge.

17th December 2023
