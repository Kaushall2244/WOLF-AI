from core.speech import speak, listen
from core.brain import Brain
from core.router import execute


brain = Brain()


def start():

    speak("WOLF Online.")

    while True:

        command = listen()

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