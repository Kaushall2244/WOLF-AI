import subprocess
from pathlib import Path


class Screenshot:

    def capture(self):

        output = Path("screen.png")

        try:
            subprocess.run(
                ["grim", str(output)],
                check=True
            )

            return str(output)

        except Exception as e:  # noqa: BLE001
            return f"Screenshot failed: {e}"