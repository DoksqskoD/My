import pyautogui
import requests


def Screen(A):
    screen = pyautogui.screenshot(A+'.png')
    print(screen)
