import numpy as np
from time import time

from src.parse import get_sudoku
from src.util import new_game, input_solution, wait_for_signal
from src.solve_sudoku_c import solve_sudoku # faster version, but uses c bindings
# from src.solve_sudoku_py import solve_sudoku

while True:
    wait_for_signal()
    st = time()
    sudoku = get_sudoku()
    solution = solve_sudoku(sudoku)
    end = time()
    print(f"Solving took {end-st} s")
    print(sudoku)
    print(solution)
    if not np.array_equal(sudoku, solution):
        input_solution(sudoku, solution)
    wait_for_signal()
    new_game()
