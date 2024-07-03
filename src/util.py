from PIL import ImageGrab
import numpy as np

IMG_SHAPE = (58, 58)
SUDOKU_REC = (257, 269, 785, 797)

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
        snapshot.save("screenshot.png")
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
    print(res.shape)
    return res
