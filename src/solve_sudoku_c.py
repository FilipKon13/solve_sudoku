import ctypes
import os
import numpy as np

dll_path = os.path.abspath(os.path.join("src","solve.dll"))
lib = ctypes.CDLL(dll_path)

lib.solve_sudoku.argtypes = [ctypes.POINTER(ctypes.c_char)]
lib.solve_sudoku.restype = ctypes.c_int

def solve_sudoku(tab: list[list[int]]) -> list[list[int]]:
    buf = bytes([s for x in tab for s in x])
    lib.solve_sudoku(buf)
    return np.array([int(x) for x in buf], dtype=int).reshape((9,9))
