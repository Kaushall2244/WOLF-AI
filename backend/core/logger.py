from pathlib import Path
from datetime import datetime


class Logger:

    def __init__(self):

        project_root = Path(__file__).resolve().parents[2]

        self.logfile = project_root / "logs" / "wolf.log"

    def log(self, level: str, message: str):

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        line = f"[{timestamp}] [{level}] {message}\n"

        with open(self.logfile, "a", encoding="utf-8") as file:

            file.write(line)


logger = Logger()