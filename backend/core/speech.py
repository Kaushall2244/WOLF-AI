import speech_recognition as sr
import pyttsx3

from core.config import config

recognizer = sr.Recognizer()

try:
    engine = pyttsx3.init()
    engine.setProperty("rate", config.get("voice.rate", 170))
    engine.setProperty("volume", config.get("voice.volume", 1.0))
except Exception:
    engine = None


def speak(text):
    print(f"\n[{config.get('assistant_name', 'WOLF')}] {text}")
    if engine:
        try:
            engine.say(text)
            engine.runAndWait()
        except Exception:
            pass


def listen():
    if not config.get("speech.enabled", True):
        try:
            return input("\n[YOU] > ").strip().lower()
        except (KeyboardInterrupt, EOFError):
            return "exit"

    try:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            print("\n[MIC] Listening...")
            audio = recognizer.listen(source, timeout=config.get("speech.timeout", 5))

        command = recognizer.recognize_google(audio)
        print(f"[YOU] {command}")
        return command.lower()
    except Exception:
        # Fallback to console input if voice recognition fails or mic unavailable
        try:
            user_input = input("\n[YOU] (mic fallback) > ").strip()
            return user_input.lower()
        except (KeyboardInterrupt, EOFError):
            return "exit"