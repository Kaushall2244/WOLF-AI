import subprocess

APPS = {
    "firefox": "firefox",
    "chrome": "google-chrome-stable",
    "steam": "steam",
    "discord": "discord",
    "code": "code",
    "terminal": "kitty",
    "files": "thunar",
    "minecraft": "sklauncher",
}


def open_app(command: str):

    command = command.lower()

    for app, executable in APPS.items():

        if app in command:

            try:

                subprocess.Popen([executable])

                return {
                    "message": f"Opening {app}.",
                    "app": app
                }

            except Exception as e:

                return f"Failed to open {app}: {e}"

    return "I don't know which application you want."