import ollama


class AI:

    def ask(self, prompt: str):

        response = ollama.chat(

            model="gemma3:4b",

            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are WOLF, an intelligent Linux desktop assistant. "
                        "Be friendly, concise, and helpful."
                    )
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]

        )

        return response["message"]["content"]