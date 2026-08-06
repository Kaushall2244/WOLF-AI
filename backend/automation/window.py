import shutil
import subprocess
import pyautogui

pyautogui.FAILSAFE = False


def active_window():
    if shutil.which("hyprctl"):
        try:
            res = subprocess.run(["hyprctl", "activewindow"], capture_output=True, text=True)
            if res.stdout.strip():
                return res.stdout
        except Exception:
            pass

    try:
        import pygetwindow as gw
        win = gw.getActiveWindow()
        if win:
            return win.title
    except Exception:
        pass
    return "Active Window"


def close_window():
    if shutil.which("hyprctl"):
        try:
            subprocess.run(["hyprctl", "dispatch", "killactive"])
            return "Closed active window."
        except Exception:
            pass

    pyautogui.hotkey("alt", "f4")
    return "Closed active window."


def fullscreen():
    if shutil.which("hyprctl"):
        try:
            subprocess.run(["hyprctl", "dispatch", "fullscreen", "1"])
            return "Fullscreen enabled."
        except Exception:
            pass

    pyautogui.press("f11")
    return "Toggled fullscreen."


def focus(direction):
    if shutil.which("hyprctl"):
        try:
            subprocess.run(["hyprctl", "dispatch", "movefocus", direction])
            return f"Moved focus {direction}."
        except Exception:
            pass

    if direction.lower() in ("right", "left"):
        pyautogui.hotkey("alt", "tab")
    elif direction.lower() == "up":
        pyautogui.hotkey("win", "up")
    elif direction.lower() == "down":
        pyautogui.hotkey("win", "down")
    return f"Moved focus {direction}."