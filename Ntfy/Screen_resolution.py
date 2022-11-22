import pyautogui

def Screen(Name_Screen: str) -> "Image":
    screen = pyautogui.screenshot(Name_Screen+'.png')
    return screen

if __name__ == "__main__":
    Screen()