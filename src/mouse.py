from pynput.mouse import Controller
from time import sleep

sleep(5)

mouse = Controller()
print(mouse.position)