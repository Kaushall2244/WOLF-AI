import shutil
import subprocess
from pathlib import Path


class Screenshot:

    def capture(self):
        output = Path(__file__).parent.parent / "screen.png"

        # 1. Try mss (Cross-platform)
        try:
            import mss
            with mss.mss() as sct:
                sct.shot(mon=1, output=str(output))
            return str(output.resolve())
        except Exception:
            pass

        # 2. Try PIL ImageGrab (Cross-platform)
        try:
            from PIL import ImageGrab
            img = ImageGrab.grab()
            img.save(str(output))
            return str(output.resolve())
        except Exception:
            pass

        # 3. Try pyautogui (Cross-platform X11 / Windows)
        try:
            import pyautogui
            img = pyautogui.screenshot()
            img.save(str(output))
            return str(output.resolve())
        except Exception:
            pass

        # 4. Fallback for Linux Wayland (grim)
        if shutil.which("grim"):
            try:
                subprocess.run(["grim", str(output)], check=True)
                return str(output.resolve())
            except Exception:
                pass

        raise RuntimeError("Failed to capture screenshot across all available methods.")