import cProfile
from memory_profiler import profile as mem_profile
from solve_sudoku import solve_sudoku

# import psutil
# import os

# === PROFILING FUNCTIONS =====================================================
"""!@file profiling.py
@brief Module containing tools to profile the sudoku solvers.

@details This script takes a sudoku text file as an input and profiles the
backtracking, constraint satisfaction and linear programming solvers.
@author Created by Steven Dillmann 17/12/2023
"""

# 1. profile_bt


def profile_bt(file_path):
    """!@brief Profile the backtracking (bt) algorithm solver.

    @details This function profiles the backtracking algorithm. It profiles the
    following cases:

    1. Profile the bt solver with an easy sudoku.
    2. Profile the bt solver with a medium sudoku.
    3. Profile the bt solver with a hard sudoku.
    4. Profile the bt solver with an extreme sudoku.

    @param file_path The path to the sudoku file to be solved.
    @type file_path str
    """
    print("Profiling Backtracking Solver for: ", file_path)
    solve_sudoku(file_path, solver="bt")


# 2. profile_cs


def profile_cs(file_path):
    """!@brief Profile the constraint satisfaction (cs) algorithm solver.

    @details This function profiles the constraint satisfaction solver. It
    profiles the following cases:

    1. Profile the cs solver with an easy sudoku.
    2. Profile the cs solver with a medium sudoku.
    3. Profile the cs solver with a hard sudoku.
    4. Profile the cs solver with an extreme sudoku.

    @param file_path The path to the sudoku file to be solved.
    @type file_path str
    """
    print("Profiling Constraint Satisfaction Solver for: ", file_path)
    solve_sudoku(file_path, solver="cs")


# 3. profile_lp


def profile_lp(file_path):
    """!@brief Profile the linear programming (lp) algorithm solver.

    @details This function profiles the linear programming solver. It profiles
    the following cases:

    1. Profile the lp solver with an easy sudoku.
    2. Profile the lp solver with a medium sudoku.
    3. Profile the lp solver with a hard sudoku.
    4. Profile the lp solver with an extreme sudoku.

    @param file_path The path to the sudoku file to be solved.
    @type file_path str
    """
    print("Profiling Linear Programming Solver for: ", file_path)
    solve_sudoku(file_path, solver="lp")


# === MAIN ====================================================================

if __name__ == "__main__":
    easy_file = "tests_resources/easy_1.txt"
    medium_file = "tests_resources/medium_1.txt"
    hard_file = "tests_resources/hard_1.txt"
    extreme_file = "tests_resources/extreme_1.txt"

    # Profiling using memory_profiler (mem_profile)
    profile_bt_mem = mem_profile(profile_bt)
    profile_bt_mem(easy_file)
    profile_bt_mem(medium_file)
    profile_bt_mem(hard_file)
    # profile_bt_mem(extreme_file)

    profile_cs_mem = mem_profile(profile_cs)
    profile_cs_mem(easy_file)
    profile_cs_mem(medium_file)
    profile_cs_mem(hard_file)
    # profile_cs_mem(extreme_file)

    profile_lp_mem = mem_profile(profile_lp)
    profile_lp_mem(easy_file)
    profile_lp_mem(medium_file)
    profile_lp_mem(hard_file)
    # profile_lp_mem(extreme_file)

    # Profiling using cProfile
    cProfile.run("profile_bt(easy_file)", sort="cumtime")
    cProfile.run("profile_bt(medium_file)", sort="cumtime")
    cProfile.run("profile_bt(hard_file)", sort="cumtime")
    # cProfile.run("profile_bt(extreme_file)", sort="cumtime")

    cProfile.run("profile_cs(easy_file)", sort="cumtime")
    cProfile.run("profile_cs(medium_file)", sort="cumtime")
    cProfile.run("profile_cs(hard_file)", sort="cumtime")
    # cProfile.run("profile_cs(extreme_file)", sort="cumtime")

    cProfile.run("profile_lp(easy_file)", sort="cumtime")
    cProfile.run("profile_lp(medium_file)", sort="cumtime")
    cProfile.run("profile_lp(hard_file)", sort="cumtime")
    # cProfile.run("profile_lp(extreme_file)", sort="cumtime")


# def profile_solve(file_path):
#     initial_memory = psutil.Process(os.getpid()).memory_info().rss / 1024
#     print("Initial Memory:", initial_memory, "KiB")

#     solve_sudoku(file_path, solver="bt")

#     final_memory = psutil.Process(os.getpid()).memory_info().rss / 1024
#     print("Final Memory:", final_memory, "KiB")

#     memory_increment = final_memory - initial_memory
#     print("Memory Increment:", memory_increment, "KiB")

# if __name__ == "__main__":
#     easy_file = "tests_resources/easy_1.txt"
#     medium_file = "tests_resources/medium_1.txt"
#     hard_file = "tests_resources/hard_1.txt"
#     extreme_file = "tests_resources/extreme_1.txt"

#     profile_lp(easy_file)
#     profile_lp(medium_file)
#     profile_lp(hard_file)
#     profile_lp(extreme_file)
