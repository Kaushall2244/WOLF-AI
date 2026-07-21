from rich.table import Table
from rich.panel import Panel
from rich.layout import Layout
from rich.progress_bar import ProgressBar
from rich.console import Group

import shutil
import socket
import psutil
import time

def cpu_panel():

    cpu = psutil.cpu_percent()

    return Panel(
        Group(
            f"CPU Usage : {cpu}%",
            ProgressBar(total=100, completed=cpu)
        ),
        title="CPU"
    )

def ram_panel():

    ram = psutil.virtual_memory()

    percent = ram.percent

    return Panel(
        Group(
            f"RAM : {percent}%",
            ProgressBar(total=100, completed=percent)
        ),
        title="Memory"
    )

def disk_panel():

    disk = shutil.disk_usage("/")

    used = disk.used/(1024**3)

    total = disk.total/(1024**3)

    percent = used/total*100

    return Panel(
        Group(
            f"{used:.1f} GB / {total:.1f} GB",
            ProgressBar(total=100, completed=percent)
        ),
        title="Disk"
    )

def battery_panel():

    battery = psutil.sensors_battery()

    if battery:

        return Panel(
            f"🔋 {battery.percent}%",
            title="Battery"
        )

    return Panel("Desktop", title="Battery")

def network_panel():

    try:

        socket.create_connection(("8.8.8.8",53),2)

        return Panel("🟢 Online",title="Network")

    except:

        return Panel("🔴 Offline",title="Network")
    
def dashboard():

    layout = Layout()

    layout.split_column(

        Layout(name="top",size=3),

        Layout(name="middle"),

        Layout(name="bottom",size=3)

    )

    layout["top"].update(

        Panel(
            "[cyan bold]JARVIS OS[/cyan bold]"
        )

    )

    table = Table.grid(expand=True)

    table.add_column()

    table.add_column()

    table.add_column()

    table.add_row(

        cpu_panel(),

        ram_panel(),

        battery_panel()

    )

    table.add_row(

        disk_panel(),

        network_panel(),

        Panel(time.strftime("%I:%M:%S %p"),title="Time")

    )

    layout["middle"].update(table)

    layout["bottom"].update(

        Panel(
            "Press CTRL+C to quit",
            title="Status"
        )

    )

    return layout
