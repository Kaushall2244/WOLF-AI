import json
from pathlib import Path
from database.db import db

MEMORY_FILE = Path(__file__).parent.parent / "config" / "memory.json"


def load_memory():
    if MEMORY_FILE.exists():
        with open(MEMORY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}


def save_memory(memory):
    MEMORY_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump(memory, f, indent=4)


class Memory:

    def __init__(self):
        self.last_app = None
        self.last_command = None

    def remember_app(self, app):
        self.last_app = app
        db.remember("favorite_apps", app, "used")

    def remember_command(self, cmd):
        self.last_command = cmd
        db.log_history(command=cmd)

    def get_last_app(self):
        return self.last_app

    def get_last_command(self):
        return self.last_command

    def store_long_term(self, category: str, key: str, value: str):
        db.remember(category, key, value)

    def recall_long_term(self, category: str = None, key: str = None):
        return db.recall(category, key)