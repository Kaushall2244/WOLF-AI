import ollama

from core.profile import Profile

profile = Profile()


class AI:
    def __init__(self):
        self.model = "gemma3:4b"

    def ask(self, prompt):
        try:
            name = profile.get("name") or "User"

            system_prompt = f"""
You are WOLF.
You are an offline AI assistant and desktop companion.
The user's name is {name}.
Be concise, smart, direct, and helpful.
"""

            response = ollama.chat(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": prompt},
                ],
            )

            return response["message"]["content"]

        except Exception as e:
            return f"[Ollama AI Offline/Error]: {e}. Please ensure Ollama is installed and running with model '{self.model}'."

    def vision(self, image_path, prompt):
        try:
            response = ollama.chat(
                model=self.model,
                messages=[
                    {
                        "role": "user",
                        "content": prompt,
                        "images": [image_path],
                    }
                ],
            )

            return response["message"]["content"]

        except Exception as e:
            return f"[Vision Error]: {e}. Make sure Ollama vision model is available."

