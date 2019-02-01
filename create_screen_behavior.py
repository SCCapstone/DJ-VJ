"""
Runs a simple behavioral test.
As the user, I wish to be able to load the program,
click on "Create Show",
and have the Create Show screen load
This is automated using the pyautogui python package
"""
import pyautogui
import djvj.djvj_GUI as gui

if __name__ == '__main__':
    print("Start Test")
    gui.IntroScreen()
    print("Click on Create Show")
    pyautogui.click(x=461, y=620, clicks=1, button='left')
    pyautogui.alert("Show created!")
