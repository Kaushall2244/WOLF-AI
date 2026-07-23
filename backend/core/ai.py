import requests


class AI:

    def __init__(self):
        self.url = "http://localhost:11434/api/generate"
        self.model = "gemma3:4b"

    def ask(self, prompt):

        prompt = f"""
        You are WOLF.
        
        You are a futuristic Linux AI operating system.
        
        Be concise.
        Be friendly.
        Answer in under 4 sentences.
        Never mention you are ChatGPT.
        Always refer to yourself as WOLF.
        
        User:
        {prompt}
        """

        try:

            response = requests.post(

                self.url,

                json={
                    "model": self.model,
                    "prompt": prompt,
                    "stream": False
                }

            )

            data = response.json()

            return data["response"]

        except Exception:

            return "I couldn't reach my AI brain."