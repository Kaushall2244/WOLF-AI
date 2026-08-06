import datetime
from core.launcher import open_app


def execute(command):

    if "time" in command:
        now = datetime.datetime.now()
        return f"It is {now.strftime('%I:%M %p')}"

    res = open_app(command)
    if isinstance(res, dict) and "message" in res:
        return res["message"]
    elif isinstance(res, str) and not res.startswith("I don't know"):
        return res

    return "I don't know that command yet."