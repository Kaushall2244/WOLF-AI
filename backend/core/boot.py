from rich.console import Console
from rich.progress import track
import time

console = Console()


def boot():
    console.print()

    console.print("[bold cyan]Initializing JARVIS CORE[/]")

    modules = [
        "Voice Engine",
        "Microphone",
        "AI Core",
        "System Monitor",
        "Network",
        "Command Router",
    ]

    for module in track(modules):
        time.sleep(0.4)

    console.print("[bold green]System Ready[/]")