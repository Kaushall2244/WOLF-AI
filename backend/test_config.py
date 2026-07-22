from core.config import config

print("----------------")

print("Assistant :", config.get("assistant_name"))

print("Wake Word :", config.get("wake_word"))

print("Voice Rate:", config.get("voice.rate"))

print("Theme     :", config.get("theme"))

print("----------------")