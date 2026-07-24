from core.skills import apps
from core.skills import system
from core.skills import chat
from core.ai import AI
from core.profile import Profile

profile = Profile()
ai = AI()


class SkillManager:

    def execute(self, result):

        intent = result["intent"]

        # -------------------------
        # Save User Name
        # -------------------------
        if intent == "SAVE_NAME":

            profile.set("name", result["name"])

            return f"I'll remember that. Your name is {result['name']}."

        # -------------------------
        # Get User Name
        # -------------------------
        elif intent == "GET_NAME":

            name = profile.get("name")

            if name:
                return f"Your name is {name}."

            return "I don't know your name yet."

        # -------------------------
        # Open Applications
        # -------------------------
        elif intent == "OPEN_APP":

            return apps.execute(result["command"])

        # -------------------------
        # System Information
        # -------------------------
        elif intent == "SYSTEM_INFO":

            return system.execute(result["command"])

        # -------------------------
        # Built-in Chat
        # -------------------------
        elif intent in (
            "GREETING",
            "THANKS",
            "WHO_ARE_YOU",
            "HOW_ARE_YOU",
        ):

            return chat.execute(intent)

        # -------------------------
        # Exit
        # -------------------------
        elif intent == "EXIT":

            return "Goodbye."

        # -------------------------
        # AI Fallback (Gemma)
        # -------------------------
        elif intent == "UNKNOWN":

            return ai.ask(result["command"])

        # -------------------------
        # Unknown Intent
        # -------------------------
        return "I'm not sure how to handle that."