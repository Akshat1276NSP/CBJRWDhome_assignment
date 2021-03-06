import pyautogui # pip install pyautogui
from PIL import Image, ImageGrab # pip install pillow
# from numpy import asarray
import time

def hit(key):
    pyautogui.keyDown(key)
    return

def isCollide(data):
    # Draw the rectangle for birds
    for i in range(300, 415):
        for j in range(410, 563):
            if data[i, j] < 100:
                hit("down")
                return

    for i in range(300, 415):
        for j in range(563, 650):
            if data[i, j] < 100:
                hit("up")
                return True
                return False
a = int(input())
b = int(input())

def add(a+b):
    print("THE SUM IS GONNA BE", a+b)

def mult(a*b):
    print("THE PRODUCT IS GONNA BE ", a*b)

def div(a/b):
    print("THE QUOTIENT IS GONNA BE ", a/b)

def sqrt(a**b):
    print("THE SQUARE ROOT IS GONNA BE ", a**(1/b))

def raised_power(a**b)
