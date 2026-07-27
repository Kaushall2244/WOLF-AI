from vision.screenshot import Screenshot

from core.ai import AI

shot = Screenshot()
ai = AI()


def execute(prompt):

    image = shot.capture()

    return ai.vision(image, prompt)