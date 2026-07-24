from pathlib import Path
from mss import mss


class Screenshot:

    def capture(self, filename="screen.png"):

        output = Path(filename).resolve()

        with mss() as sct:

            sct.grab(sct.monitors[1])

            sct.shot(
                mon=1,
                output=str(output)
            )

        return str(output)