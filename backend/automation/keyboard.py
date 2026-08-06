import shutil
import subprocess
import pyautogui

pyautogui.FAILSAFE = False


def type_text(text: str):
    if shutil.which("ydotool"):
        try:
            subprocess.run(["ydotool", "type", text])
            return
        except Exception:
            pass

    pyautogui.write(text, interval=0.02)


def press(key: str):
    if shutil.which("ydotool"):
        keys = {"enter": "28", "esc": "1", "space": "57", "tab": "15", "backspace": "14"}
        code = keys.get(key.lower())
        if code:
            try:
                subprocess.run(["ydotool", "key", f"{code}:1", f"{code}:0"])
                return
            except Exception:
                pass

    key_map = {
        "enter": "enter",
        "esc": "escape",
        "escape": "escape",
        "space": "space",
        "tab": "tab",
        "backspace": "backspace",
    }
    target_key = key_map.get(key.lower(), key.lower())
    pyautogui.press(target_key)


def hotkey(*keys):
    pyautogui.hotkey(*[k.lower() for k in keys])