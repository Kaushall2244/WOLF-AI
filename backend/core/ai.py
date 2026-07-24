import ollama
from core.profile import Profile

profile = Profile()


class AI:

    def __init__(self):

        self.model = "gemma3:4b"

    def ask(self, prompt):

        name = profile.get("name") or "User"

        system_prompt = f"""
You are WOLF.

You are an offline Linux AI assistant created by Wolfii.

The user's name is {name}.

Be concise and helpful.
"""

        response = ollama.chat(

            model=self.model,

            messages=[

                {
                    "role": "system",
                    "content": system_prompt
                },

                {
                    "role": "user",
                    "content": prompt
                }

            ]

        )

        return response["message"]["content"]

    def vision(self, image_path, prompt):

        response = ollama.chat(

            model=self.model,

            messages=[

                {
                    "role": "user",
                    "content": prompt,
                    "images": [image_path]
                }

            ]

        )

        return response["message"]["content"]