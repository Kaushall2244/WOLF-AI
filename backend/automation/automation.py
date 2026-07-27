from automation.keyboard import press, type_text
from automation.mouse import (
    click,
    double_click,
    right_click,
    scroll_down,
    scroll_up,
)


class Automation:

    def execute(self, command: str):

        command = command.lower()

        if "double click" in command:
            double_click()
            return "Done."

        if "right click" in command:
            right_click()
            return "Done."

        if "click" in command:
            click()
            return "Done."

        if "scroll up" in command:
            scroll_up()
            return "Scrolling up."

        if "scroll down" in command:
            scroll_down()
            return "Scrolling down."

        if command.startswith("type "):

            text = command.replace("type ", "")

            type_text(text)

            return f"Typed '{text}'."

        if "press enter" in command:
            press("enter")
            return "Pressed Enter."

        if "press escape" in command:
            press("esc")
            return "Pressed Escape."

        if "press tab" in command:
            press("tab")
            return "Pressed Tab."

        if "press space" in command:
            press("space")
            return "Pressed Space."

        return None