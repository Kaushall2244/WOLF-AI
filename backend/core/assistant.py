from core.speech import speak, listen
from core.brain import Brain
from core.router import execute
from core.memory import Memory
from core.config import config
from core.logger import logger

memory = Memory()
brain = Brain()

def start():

    logger.log("INFO", "Assistant Started")
    assistant_name = config.get("assistant_name", "WOLF")

    speak(f"{assistant_name} Online.")

    while True:
        command = listen()

        if not command:
            continue

        logger.log("USER", command)
        
        result = brain.analyze(command)
        logger.log("INTENT", result.get("intent", "UNKNOWN"))
        
        memory.remember_command(command)

        response = execute(result)
        logger.log("WOLF", str(response))

        print(f"\n{assistant_name} : {response}")
        speak(str(response))

        if result.get("intent") == "EXIT":
            break