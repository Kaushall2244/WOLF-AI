from core.system import System


def execute(command):

    command = command.lower()

    if "cpu" in command:
        return f"CPU Usage is {System.cpu()}%"

    if "ram" in command or "memory" in command:
        used, total = System.ram()
        return f"RAM Usage is {used} GB out of {total} GB"

    if "battery" in command:
        battery = System.battery()

        if battery is None:
            return "Battery information unavailable."

        return f"Battery is at {battery}%"

    if "time" in command:
        return f"The current time is {System.time()}"

    return "Unknown system request."