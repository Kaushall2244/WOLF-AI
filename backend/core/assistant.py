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

    speak(f"{config.get('assistant_name')} Online.")

    while True:

        command = listen()

        command = listen()

        logger.log("USER", command)
        
        result = brain.analyze(command)
        
        logger.log("INTENT", result["intent"])
        
        response = execute(result)
        
        logger.log("WOLF", response)

        if not command:
            continue

        memory.remember_command(command)

        print(f"\nYOU  : {command}")

        result = brain.analyze(command)

        print(result)

        response = execute(result)

        print(f"{config.get('assistant_name')} : {response}")

        speak(response)

        if result["intent"] == "EXIT":
            break