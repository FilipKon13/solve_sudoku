from src.solve_sudoku_py import solve_sudoku
# from src.solve_sudoku_c import solve_sudoku
from src.util import input_solution, wait_for_signal
from src.parse import get_sudoku

for line in get_sudoku():
    print(*line)

wait_for_signal()

inp = [[int(x) for x in input().split()] for _ in range(9)]

print(inp)
res = solve_sudoku(inp)
print(inp)
print(res)
input_solution(inp, res)
