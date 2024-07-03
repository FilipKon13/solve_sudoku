static int check(char * tab, int x, int y, char val) {
    for(int i = 0; i < 9; i++) {
        if(tab[x*9 + i] == val) return 0;
        if(tab[i*9 + y] == val) return 0;
    }
    int X = (x/3)*3;
    int Y = (y/3)*3;
    for(int i = X; i < X + 3; i++) {
        for(int j = Y; j < Y + 3; j++) {
            if(tab[i*9 + j] == val) return 0;
        }
    }
    return 1;
}

static int solve_impl(char * tab, int x, int y) {
    if(x == 9) return 1;
    int X,Y;
    if(y == 8) {
        X = x + 1;
        Y = 0;
    } else {
        X = x;
        Y = y + 1;
    }
    if(tab[x*9 + y] != 0) return solve_impl(tab, X, Y);
    for(char v = 1; v <= 9; v++) if(check(tab,x,y,v)) {
        tab[x*9 + y] = v;
        if(solve_impl(tab, X, Y))   return 1;
    }
    tab[x*9+y] = 0;
    return 0;
}

__declspec(dllexport) int solve_sudoku(char * tab) {
    return solve_impl(tab, 0, 0);
}
