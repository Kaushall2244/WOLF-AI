import shutil
import subprocess
import pyperclip


def copy(text: str):
    try:
        pyperclip.copy(text)
    except Exception:
        if shutil.which("wl-copy"):
            subprocess.run(["wl-copy"], input=text, text=True)


def paste():
    try:
        return pyperclip.paste()
    except Exception:
        if shutil.which("wl-paste"):
            res = subprocess.run(["wl-paste"], capture_output=True, text=True)
            return res.stdout
    return ""


def clear():
    try:
        pyperclip.copy("")
    except Exception:
        if shutil.which("wl-copy"):
            subprocess.run(["wl-copy"], input="", text=True)