import random


class Personality:

    greetings = [
        "Hello Wolf!",
        "Hi! Ready when you are.",
        "Welcome back!",
        "Good to see you again."
    ]

    thanks = [
        "You're welcome!",
        "Anytime.",
        "Happy to help.",
        "Always."
    ]

    unknown = [
        "I didn't understand that.",
        "Could you repeat that?",
        "I'm still learning.",
        "Can you say that differently?"
    ]

    who = [
        "I'm WOLF, your desktop AI.",
        "I'm your personal assistant.",
        "I can control your computer and help with tasks."
    ]

    mood = [
        "Everything is running smoothly.",
        "All systems operational.",
        "Ready for your next command."
    ]

    @staticmethod
    def greeting():
        return random.choice(Personality.greetings)

    @staticmethod
    def thanks():
        return random.choice(Personality.thanks)

    @staticmethod
    def unknown_reply():
        return random.choice(Personality.unknown)

    @staticmethod
    def who_am_i():
        return random.choice(Personality.who)

    @staticmethod
    def how_are_you():
        return random.choice(Personality.mood)