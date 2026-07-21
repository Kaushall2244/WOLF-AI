import random

RESPONSES = {

    "GREETING": [
        "Hello!",
        "Hey!",
        "Hi there!",
        "Hello, Wolf.",
        "Good to see you."
    ],

    "THANKS": [
        "You're welcome.",
        "Anytime.",
        "Happy to help.",
        "No problem."
    ],

    "WHO_ARE_YOU": [
        "I'm WOLF, your Linux AI assistant.",
        "I'm WOLF. I help control your computer.",
        "I'm your personal desktop AI."
    ],

    "HOW_ARE_YOU": [
        "I'm running perfectly.",
        "All systems are operational.",
        "Doing great. Ready for your next command."
    ]
}


def reply(intent):

    if intent in RESPONSES:
        return random.choice(RESPONSES[intent])

    return None