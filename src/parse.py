import tensorflow as tf
import numpy as np
from pynput import keyboard
from time import time
from os.path import join

from src.util import take_out, get_image, new_game, input_solution

model = tf.keras.models.load_model(join('models','digit_model_v3.h5'))

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

