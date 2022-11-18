import pyautogui

def Screen(A):
    screen = pyautogui.screenshot(A+'.png')
    return screen