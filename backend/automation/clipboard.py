import subprocess


def copy(text: str):

    subprocess.run(
        [
            "wl-copy"
        ],
        input=text,
        text=True
    )


def paste():

    result = subprocess.run(  # noqa: PLW1510
        [
            "wl-paste"
        ],
        capture_output=True,
        text=True
    )

    return result.stdout


def clear():

    subprocess.run(
        [
            "wl-copy"
        ],
        input="",
        text=True
    )