from core.launcher import open_app
from core.system import System
from core.chat import reply


def execute(result):

    intent = result["intent"]

    if intent == "OPEN_APP":
        return open_app(result["command"])

    if intent == "SYSTEM_INFO":

        command = result["command"]

        if "cpu" in command:
            return f"CPU Usage is {System.cpu()} percent."

        if "ram" in command or "memory" in command:
            used, total = System.ram()
            return f"RAM usage is {used} GB out of {total} GB."

        if "battery" in command:
            battery = System.battery()

            if battery is None:
                return "Battery information is unavailable."

            return f"Battery is at {battery} percent."

        if "time" in command:
            return f"The time is {System.time()}."

    if intent in (
        "GREETING",
        "THANKS",
        "WHO_ARE_YOU",
        "HOW_ARE_YOU",
    ):
        return reply(intent)

    if intent == "EXIT":
        return "Goodbye."

    return "Sorry, I didn't understand that."