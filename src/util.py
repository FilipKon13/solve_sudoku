from PIL import ImageGrab
import numpy as np
from pynput import mouse, keyboard
from time import sleep

IMG_SHAPE = (58, 58)
# SUDOKU_REC = (257, 269, 785, 797)
SUDOKU_REC = (257, 261, 785, 789)


def take_out(pixels, i, j):
    x, y = IMG_SHAPE
    return pixels[x*i:x*(i+1), y*j:y*(j+1)]

def convert_img(img):
    sizeX = img.shape[0]
    sizeY = img.shape[1]
    res = np.zeros((sizeX * sizeY), dtype=float)
    for i in range(sizeX):
        for j in range(sizeY):
            if img[i][j][0] >= 128:
                res[i*sizeY + j] = 1
    return res

def get_image(save=False):
    snapshot = ImageGrab.grab(SUDOKU_REC)
    snapshot = snapshot.convert("RGB")
    if save:
        snapshot.save("screenshot2.png")
    pixels = np.array(snapshot)
    print(pixels.shape)
    sizeX = pixels.shape[0]
    sizeY = pixels.shape[1]
    res = np.empty((sizeX, sizeY, 3), dtype=np.uint8)
    for i in range(sizeX):
        for j in range(sizeY):
            if pixels[i][j][0] < 128:
                res[i][j] = [0,0,0]
            else:
                res[i][j] = [255,255,255]
    return res


m_keyboard = keyboard.Controller()
m_mouse = mouse.Controller()
start = (230, 230)
dif = 47

def new_game():
    m_mouse.position = (739, 594)
    m_mouse.click(mouse.Button.left)
    m_mouse.position = (673, 500)
    sleep(1)
    m_mouse.click(mouse.Button.left)
    sleep(3)

def input_solution(sudoku, solution):
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                m_mouse.position = (start[0] + j*dif, start[1] + i*dif)
                m_mouse.click(mouse.Button.left)
                m_keyboard.tap(str(solution[i][j]))


def wait_for_signal():
    print("Waiting for left shift")
    def on_release(key):
        if key == keyboard.Key.shift_l:
            return False
        return True
    with keyboard.Listener(on_release=on_release) as l:
        l.join()

if __name__ == "__main__":
    get_image(True)