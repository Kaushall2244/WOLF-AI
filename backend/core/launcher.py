import os
import sys
import shutil
import subprocess

WINDOWS_APPS = {
    "firefox": "start firefox",
    "chrome": "start chrome",
    "edge": "start msedge",
    "steam": "start steam",
    "discord": "start discord",
    "code": "code",
    "vscode": "code",
    "terminal": "start wt",
    "cmd": "start cmd",
    "powershell": "start powershell",
    "files": "explorer",
    "explorer": "explorer",
    "calculator": "calc",
    "notepad": "notepad",
}

LINUX_APPS = {
    "firefox": ["firefox"],
    "chrome": ["google-chrome-stable", "google-chrome", "chromium", "chromium-browser"],
    "steam": ["steam"],
    "discord": ["discord"],
    "code": ["code", "vscodium"],
    "vscode": ["code", "vscodium"],
    "terminal": ["kitty", "foot", "alacritty", "gnome-terminal", "konsole", "xterm"],
    "files": ["thunar", "nautilus", "dolphin", "pcmanfm"],
    "minecraft": ["sklauncher", "minecraft-launcher"],
    "calculator": ["qalculate-gtk", "gnome-calculator", "kcalc"],
}


def open_app(command: str):
    command = command.lower()

    if sys.platform == "win32":
        for app, executable in WINDOWS_APPS.items():
            if app in command:
                try:
                    os.system(executable)
                    return {"message": f"Opening {app}.", "app": app}
                except Exception as e:
                    return f"Failed to open {app}: {e}"
    else:
        for app, binaries in LINUX_APPS.items():
            if app in command:
                for bin_name in binaries:
                    if shutil.which(bin_name):
                        try:
                            subprocess.Popen([bin_name])
                            return {"message": f"Opening {app}.", "app": app}
                        except Exception:
                            continue
                # Fallback directly to first binary name
                try:
                    subprocess.Popen([binaries[0]])
                    return {"message": f"Opening {app}.", "app": app}
                except Exception as e:
                    return f"Failed to open {app}: {e}"

    return "I don't know which application you want to open."