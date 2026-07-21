import json
from pathlib import Path

MEMORY_FILE = Path("memory.json")


def load_memory():
    if MEMORY_FILE.exists():
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)

    return {}


def save_memory(memory):
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=4)

class Memory:

    def __init__(self):
        self.last_app = None
        self.last_command = None

    def remember_app(self, app):
        self.last_app = app

    def remember_command(self, cmd):
        self.last_command = cmd

    def get_last_app(self):
        return self.last_app

    def get_last_command(self):
        return self.last_command