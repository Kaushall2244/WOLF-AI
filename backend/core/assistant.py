from core.speech import speak, listen
from core.brain import Brain
from core.router import execute
from core.memory import Memory

memory = Memory()


brain = Brain()


def start():

    speak("WOLF Online.")

    while True:

        command = listen()
        
        memory.remember_command(command)

        if not command:
            continue

        print(f"\nYOU : {command}")

        result = brain.analyze(command)

        print(result)

        response = execute(result)

        print(f"WOLF : {response}")

        speak(response)

        if result["intent"] == "EXIT":
            break