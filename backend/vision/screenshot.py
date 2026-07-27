import subprocess
from pathlib import Path


class Screenshot:

    def capture(self):

        output = Path(__file__).parent.parent / "screen.png"

        subprocess.run(
            [
                "grim",
                str(output)
            ],
            check=True
        )

        return str(output.resolve())