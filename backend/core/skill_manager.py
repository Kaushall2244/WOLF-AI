from core.skills import apps
from core.skills import system
from core.skills import chat


class SkillManager:

    def execute(self, result):

        intent = result["intent"]

        if intent == "OPEN_APP":
            response = apps.execute(result["command"])
            return response

        if intent == "SYSTEM_INFO":
            return system.execute(result["command"])

        if intent in (
            "GREETING",
            "THANKS",
            "WHO_ARE_YOU",
            "HOW_ARE_YOU",
        ):
            return chat.execute(intent)

        if intent == "EXIT":
            return "Goodbye."

        return "I don't understand."