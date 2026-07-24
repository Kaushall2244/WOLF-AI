import json
import os


class Profile:

    def __init__(self):

        root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

        self.path = os.path.join(root, "config", "profile.json")

        if not os.path.exists(self.path):

            with open(self.path, "w") as f:

                json.dump({}, f, indent=4)

    def load(self):

        with open(self.path) as f:

            return json.load(f)

    def save(self, data):

        with open(self.path, "w") as f:

            json.dump(data, f, indent=4)

    def set(self, key, value):

        data = self.load()

        data[key] = value

        self.save(data)

    def get(self, key):

        data = self.load()

        return data.get(key)