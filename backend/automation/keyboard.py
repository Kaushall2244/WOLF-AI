import subprocess


def type_text(text: str):

    subprocess.run(
        [
            "ydotool",
            "type",
            text
        ]
    )


def press(key: str):

    keys = {
        "enter": "28",
        "esc": "1",
        "space": "57",
        "tab": "15",
        "backspace": "14",
    }

    code = keys.get(key.lower())

    if code:

        subprocess.run(
            [
                "ydotool",
                "key",
                f"{code}:1",
                f"{code}:0"
            ]
        )


def hotkey(*keys):

    keymap = {
        "ctrl": "29",
        "shift": "42",
        "alt": "56",
        "super": "125",
        "c": "46",
        "v": "47",
        "x": "45",
        "a": "30",
        "s": "31",
        "z": "44",
        "y": "21",
    }

    sequence = []

    for key in keys:

        code = keymap.get(key.lower())

        if code:

            sequence.append(f"{code}:1")

    for key in reversed(keys):

        code = keymap.get(key.lower())

        if code:

            sequence.append(f"{code}:0")

    subprocess.run(
        [
            "ydotool",
            "key",
            *sequence
        ]
    )