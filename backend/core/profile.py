import json
import os
from database.db import db


class Profile:

    def __init__(self):
        root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        self.path = os.path.join(root, "config", "profile.json")

        if not os.path.exists(self.path):
            os.makedirs(os.path.dirname(self.path), exist_ok=True)
            with open(self.path, "w", encoding="utf-8") as f:
                json.dump({}, f, indent=4)

    def load(self):
        if os.path.exists(self.path):
            with open(self.path, "r", encoding="utf-8") as f:
                return json.load(f)
        return {}

    def save(self, data):
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

    def set(self, key, value):
        data = self.load()
        data[key] = value
        self.save(data)
        db.set_profile(key, str(value))

    def get(self, key, default=None):
        val = db.get_profile(key)
        if val is not None:
            return val
        data = self.load()
        return data.get(key, default)