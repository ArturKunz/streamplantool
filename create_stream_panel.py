from PIL import Image
from pydantic import validate_arguments


@validate_arguments
def create_stream_panel(stream_data: dict):
    background = create_background()
    panel = background
    return panel


def create_background():
    background = Image.new('RGB', (800, 400), color=(226, 237, 255))
    return background
