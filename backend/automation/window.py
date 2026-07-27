import subprocess


def active_window():

    result = subprocess.run(
        [
            "hyprctl",
            "activewindow"
        ],
        capture_output=True,
        text=True
    )

    return result.stdout


def close_window():

    subprocess.run(
        [
            "hyprctl",
            "dispatch",
            "killactive"
        ]
    )

    return "Closed active window."


def fullscreen():

    subprocess.run(
        [
            "hyprctl",
            "dispatch",
            "fullscreen",
            "1"
        ]
    )

    return "Fullscreen enabled."


def focus(direction):

    subprocess.run(
        [
            "hyprctl",
            "dispatch",
            "movefocus",
            direction
        ]
    )