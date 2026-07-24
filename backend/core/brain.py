class Brain:

    def analyze(self, command: str):

        command = command.lower().strip()

        # ----------------------------
        # OPEN APPLICATION
        # ----------------------------

        if any(word in command for word in (
            "open",
            "launch",
            "start",
            "run",
        )):
            return {
                "intent": "OPEN_APP",
                "command": command,
            }

        # ----------------------------
        # SYSTEM INFO
        # ----------------------------

        if any(word in command for word in (
            "cpu",
            "processor",
            "ram",
            "memory",
            "battery",
            "time",
            "disk",
            "storage",
        )):
            return {
                "intent": "SYSTEM_INFO",
                "command": command,
            }

        # ----------------------------
        # GREETING
        # ----------------------------

        if any(word in command for word in (
            "hello",
            "hi",
            "hey",
            "good morning",
            "good evening",
        )):
            return {
                "intent": "GREETING",
            }
        
        
        # ----------------------------
        # WHO ARE YOU
        # ----------------------------
        
        if any(word in command for word in (
            "who are you",
            "what are you",
        )):
            return {
                "intent": "WHO_ARE_YOU"
            }
        
        # ----------------------------
        # HOW ARE YOU
        # ----------------------------
        
        if any(word in command for word in (
            "how are you",
            "how are things",
        )):
            return {
                "intent": "HOW_ARE_YOU"
            }

        # ----------------------------
        # THANKS
        # ----------------------------

        if any(word in command for word in (
            "thanks",
            "thank you",
        )):
            return {
                "intent": "THANKS",
            }

        # ----------------------------
        # EXIT
        # ----------------------------

        if any(word in command for word in (
            "exit",
            "quit",
            "bye",
            "goodbye",
            "shutdown wolf",
        )):
            return {
                "intent": "EXIT",
            }


        # -----------------------
        # Save User Name
        # -----------------------
        
        if "my name is" in command:
        
            return {
                "intent": "SAVE_NAME",
                "name": command.replace("my name is", "").strip()
            }
        
        
        # -----------------------
        # Get User Name
        # -----------------------
        
        if "what is my name" in command or "who am i" in command:
        
            return {
                "intent": "GET_NAME"
            }

        # ----------------------------
        # UNKNOWN
        # ----------------------------

        return {
            "intent": "UNKNOWN",
            "command": command,
        }