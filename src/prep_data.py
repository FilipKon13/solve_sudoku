import string
import random
from PIL import Image
from pynput.mouse import Controller, Button
from time import sleep

from util import get_image, take_out

# save_path = "pictures/
save_path = "temp/"

def rand_file_name():
    s = string.ascii_lowercase+string.digits
    return ''.join(random.sample(s, 16))

def grab_tiles():
    pixels = get_image(True)
    for i in range(9):
        for j in range(9):
            Image.fromarray(take_out(pixels,i,j)).save(save_path + rand_file_name() + ".png")

def refresh():
    mouse = Controller()
    mouse.position = (734, 611)
    mouse.click(Button.left)
    sleep(1)
    mouse.position = (756, 297)
    mouse.click(Button.left)

# print("Prepare")
# sleep(10)
# print("Start")
# for i in range(100):
#     print(i)
#     refresh()
#     sleep(5)
#     grab_tiles()

if __name__ == "__main__":
    grab_tiles()

