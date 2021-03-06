import pyautogui # pip install pyautogui
from PIL import Image, ImageGrab # pip install pillow
#from numpy import asarray
import time

def hit(key):
    pyautogui.keyDown(key)

def isCollide(data):
    for i in range(340, 415):
        for j in range(410, 563):
            if data[i, j] < 100:
                hit("down")
                return True

    for i in range(340, 415):
        for j in range(563, 650):
            
            if data[i, j] < 100:
                hit("up")
                return True
                

    return False
if __name__ == "__main__":
    print("GAME IS ABOUT TO START PLEASE WAIT...IN 2 SECONDS THE GAME WILL START... YOU WILL")
    time.sleep(3)
    hit('up')
    hit('down')
    while True:
        
        image = ImageGrab.grab().convert('L')
        data = image.load()
        isCollide(data)
            

        # #DRAW THE RECTANGLE
        # for i in range(340, 415):
        #     for j in range(563, 650):
        #         data[i, j] = 0

        # #DRAW THE bird
        # for i in range(340, 415):
        #     for j in range(410, 563):
        #         data[i, j] = 171

        # image.show()
        # break
