from vision.screenshot import Screenshot
from core.ai import AI

camera = Screenshot()
ai = AI()


def execute():

    image = camera.capture()

    return ai.vision(
        image,
        "Describe everything visible on this screen."
    )