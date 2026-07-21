import os
import datetime


def execute(command):

    if "time" in command:

        now = datetime.datetime.now()

        return f"It is {now.strftime('%I:%M %p')}"

    elif "firefox" in command:

        os.system("firefox &")

        return "Opening Firefox"

    elif "terminal" in command:

        os.system("foot &")

        return "Opening Terminal"

    elif "calculator" in command:

        os.system("qalculate-gtk &")

        return "Opening Calculator"

    return "I don't know that command yet."