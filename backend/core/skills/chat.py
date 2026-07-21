from core.personality import Personality


def execute(intent):

    if intent == "GREETING":
        return Personality.greeting()

    if intent == "THANKS":
        return Personality.thanks()

    if intent == "WHO_ARE_YOU":
        return Personality.who_am_i()

    if intent == "HOW_ARE_YOU":
        return Personality.how_are_you()

    return Personality.unknown_reply()