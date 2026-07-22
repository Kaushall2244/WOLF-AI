import json
from pathlib import Path


class Config:

    def __init__(self):

        project_root = Path(__file__).resolve().parents[2]

        self.path = project_root / "config" / "settings.json"

        if not self.path.exists():
            raise FileNotFoundError(
                f"settings.json not found:\n{self.path}"
            )

        with open(self.path, "r", encoding="utf-8") as file:
            self.data = json.load(file)

    def get(self, key, default=None):

        value = self.data

        for part in key.split("."):

            if isinstance(value, dict):
                value = value.get(part)
            else:
                return default

            if value is None:
                return default

        return value


config = Config()