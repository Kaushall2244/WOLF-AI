import speech_recognition as sr
import pyttsx3

from core.config import config

recognizer = sr.Recognizer()

engine = pyttsx3.init()

engine.setProperty(
    "rate",
    config.get("voice.rate", 170)
)

engine.setProperty(
    "volume",
    config.get("voice.volume", 1.0)
)


def speak(text):

    print(f"\n[{config.get('assistant_name')}] {text}")

    engine.say(text)
    engine.runAndWait()


def listen():

    with sr.Microphone() as source:

        recognizer.adjust_for_ambient_noise(source, duration=0.5)

        print("\n[MIC] Listening...")

        audio = recognizer.listen(source)

    try:

        command = recognizer.recognize_google(audio)

        print(f"[YOU] {command}")

        return command.lower()

    except sr.UnknownValueError:

        return ""

    except sr.RequestError:

        return ""