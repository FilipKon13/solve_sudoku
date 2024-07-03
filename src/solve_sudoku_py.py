class SudokuSolver:
    def __init__(self, tab: list[list[int]]) -> None:
        self.tab = tab.copy()
    
    def _check_row(self, x: int, y: int) -> bool:
        val = self.tab[x][y]
        for i in range(9):
            if i != y and self.tab[x][i] == val:
                return False
        return True

    def _check_column(self, x: int, y: int) -> bool:
        val = self.tab[x][y]
        for i in range(9):
            if i != x and self.tab[i][y] == val:
                return False
        return True
    
    def _check_square(self, x: int, y: int) -> bool:
        val = self.tab[x][y]
        X = x // 3
        Y = y // 3
        for i in range(X*3,(X+1)*3):
            for j in range(Y*3,(Y+1)*3):
                if i != x or j != y:
                    if self.tab[i][j] == val:
                        return False
                    
        return True
    
    def _next(x: int, y: int) -> tuple[int,int]:
        return (x, y+1) if y != 8 else (x+1,0)
    
    def _rec_solve(self, x: int, y: int) -> bool:
        if x == 9:
            return True
        if self.tab[x][y] != 0:
            return self._rec_solve(*SudokuSolver._next(x,y))
        for val in range(1,10):
            self.tab[x][y] = val
            if self._check_column(x,y) and self._check_row(x,y) and self._check_square(x,y):
                if self._rec_solve(*SudokuSolver._next(x,y)):
                    return True
        self.tab[x][y] = 0
        return False

    def solve(self) -> list[list[int]]:
        self._rec_solve(0,0)
        return self.tab

def solve_sudoku(tab):
    return SudokuSolver(tab).solve()
