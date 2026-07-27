from automation.automation import Automation

from core.ai import AI
from core.profile import Profile
from core.skills import apps, chat, system, vision

automation = Automation()
ai = AI()
profile = Profile()


class SkillManager:
    def execute(self, result):

        intent = result.get("intent", "")

        # -------------------------
        # Open Applications
        # -------------------------
        if intent == "OPEN_APP":
            return apps.execute(result["command"])

        # -------------------------
        # System Information
        # -------------------------
        elif intent == "SYSTEM_INFO":
            return system.execute(result["command"])

        # -------------------------
        # Save User Name
        # -------------------------
        elif intent == "SAVE_NAME":
            profile.set("name", result["name"])

            return f"I'll remember that. Your name is {result['name']}."

        # -------------------------
        # Recall User Name
        # -------------------------
        elif intent == "GET_NAME":
            name = profile.get("name")

            if name:
                return f"Your name is {name}."

            return "I don't know your name yet."

        # -------------------------
        # Built-in Conversation
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
            return "Goodbye! Have a great day."

        # -------------------------
        # AI Fallback
        # -------------------------
        elif intent == "UNKNOWN":
            return ai.ask(result["command"])

        # -------------------------
        # VISION
        # -------------------------

        elif intent == "VISION":
            return vision.execute(result["command"])

        # --------------------------
        # AUTOMATION
        # --------------------------

        elif intent == "AUTOMATION":
            return automation.execute(result["command"])

        # -------------------------
        # Default
        # -------------------------
        return "I'm not sure how to help with that."
