from datetime import datetime
import psutil


class System:

    @staticmethod
    def cpu():
        return psutil.cpu_percent(interval=0.5)

    @staticmethod
    def ram():
        ram = psutil.virtual_memory()

        return (
            round(ram.used / (1024**3), 2),
            round(ram.total / (1024**3), 2)
        )

    @staticmethod
    def battery():
        battery = psutil.sensors_battery()

        if battery:
            return battery.percent

        return None

    @staticmethod
    def time():
        return datetime.now().strftime("%I:%M:%S %p")