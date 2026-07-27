import subprocess


def click():

    subprocess.run(
        [
            "ydotool",
            "click",
            "0xC0"
        ]
    )


def double_click():

    click()
    click()


def right_click():

    subprocess.run(
        [
            "ydotool",
            "click",
            "0xC1"
        ]
    )


def scroll_up():

    subprocess.run(
        [
            "ydotool",
            "click",
            "0x900"
        ]
    )


def scroll_down():

    subprocess.run(
        [
            "ydotool",
            "click",
            "0x901"
        ]
    )


def move(x: int, y: int):

    subprocess.run(
        [
            "ydotool",
            "mousemove",
            "--absolute",
            str(x),
            str(y)
        ]
    )