import tensorflow as tf
import numpy as np
from pynput import keyboard, mouse
from time import sleep, time
from os.path import join

from src.util import take_out, get_image
# from src.solve_sudoku_c import solve_sudoku # faster version, but uses c bindings
from src.solve_sudoku_py import solve_sudoku

model = tf.keras.models.load_model(join('models','digit_model.h5'))

m_keyboard = keyboard.Controller()
m_mouse = mouse.Controller()

def timer_func(func): 
    def wrap_func(*args, **kwargs): 
        t1 = time() 
        result = func(*args, **kwargs) 
        t2 = time() 
        print(f'Function {func.__name__!r} executed in {(t2-t1):.4f}s') 
        return result 
    return wrap_func 

@timer_func
def get_prediction(img):
    res = model.predict(img)
    return np.argmax(res,axis=1)

@timer_func
def get_sudoku():
    pixels = get_image()
    imgs = np.array([take_out(pixels,i,j) for i in range(9) for j in range(9)])
    return get_prediction(imgs).reshape((9,9))

def new_game():
    m_mouse.position = (739, 594)
    m_mouse.click(mouse.Button.left)
    m_mouse.position = (673, 500)
    sleep(1)
    m_mouse.click(mouse.Button.left)
    sleep(3)

def wait_for_signal():
    print("Waiting for keyboard input")
    def on_release(_key):
        return False
    with keyboard.Listener(on_release=on_release) as l:
        l.join()

start = (230, 230)
dif = 47

while True:
    wait_for_signal()
    st = time()
    sudoku = get_sudoku()
    solution = solve_sudoku(sudoku)
    end = time()
    print(f"Solving took {end-st} s")
    print(sudoku)
    print(solution)
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                m_mouse.position = (start[0] + j*dif, start[1] + i*dif)
                m_mouse.click(mouse.Button.left)
                m_keyboard.tap(str(solution[i][j]))
                # sleep(0.1)
    wait_for_signal()
    new_game()