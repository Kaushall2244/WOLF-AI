class Parser:

    @staticmethod
    def parse(command):

        command = command.lower().strip()

        if command.startswith("open "):

            return (
                "open",
                command.replace("open ", "")
            )

        return (
            command,
            None
        )