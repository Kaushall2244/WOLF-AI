import speech_recognition as sr
import pyttsx3

recognizer = sr.Recognizer()

engine = pyttsx3.init()


def speak(text):

    print(f"\n[JARVIS] {text}")

    engine.say(text)

    engine.runAndWait()


def listen():

    with sr.Microphone() as source:

        recognizer.adjust_for_ambient_noise(source, duration=0.5)

        print("\n[MIC] Listening...")

        audio = recognizer.listen(source)

    try:

        command = recognizer.recognize_google(audio)

        print(f"[USER] {command}")

        return command.lower()

    except sr.UnknownValueError:

        return ""

    except sr.RequestError:

        return ""