import shutil
import subprocess
import pyautogui

pyautogui.FAILSAFE = False


def click():
    if shutil.which("ydotool"):
        try:
            subprocess.run(["ydotool", "click", "0xC0"])
            return
        except Exception:
            pass
    pyautogui.click()


def double_click():
    click()
    click()


def right_click():
    if shutil.which("ydotool"):
        try:
            subprocess.run(["ydotool", "click", "0xC1"])
            return
        except Exception:
            pass
    pyautogui.rightClick()


def scroll_up(clicks: int = 5):
    if shutil.which("ydotool"):
        try:
            subprocess.run(["ydotool", "click", "0x900"])
            return
        except Exception:
            pass
    pyautogui.scroll(clicks * 100)


def scroll_down(clicks: int = 5):
    if shutil.which("ydotool"):
        try:
            subprocess.run(["ydotool", "click", "0x901"])
            return
        except Exception:
            pass
    pyautogui.scroll(-clicks * 100)


def move(x: int, y: int):
    if shutil.which("ydotool"):
        try:
            subprocess.run(["ydotool", "mousemove", "--absolute", str(x), str(y)])
            return
        except Exception:
            pass
    pyautogui.moveTo(x, y)