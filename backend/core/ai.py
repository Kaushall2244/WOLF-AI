import ollama


class AI:

    def __init__(self):
        self.model = "gemma3:4b"

    def ask(self, prompt: str):

        try:

            response = ollama.chat(
                model=self.model,
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "You are WOLF, an intelligent offline AI assistant created by Wolfii. "
                            "You run on Linux and help with programming, automation, engineering, gaming, and daily tasks. "
                            "Be confident, concise, and conversational. "
                            "If you don't know something, say so instead of making it up."
                        )
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )

            return response["message"]["content"]

        except Exception as e:
            return f"AI Error: {e}"