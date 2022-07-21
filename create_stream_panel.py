from typing import Tuple
from PIL import Image, ImageDraw, ImageFont
from pydantic import validate_arguments


@validate_arguments
def create_stream_panel(stream_data: dict):
    background = create_background()
    paste_text(background, text=stream_data["title"], position=(60, 10))
    paste_text(background, text=stream_data["datetime"], position=(60, 70))
    panel = background
    return panel


@validate_arguments
def create_background():
    background = Image.new('RGB', (800, 400), color=(226, 237, 255))
    return background


@validate_arguments(config=dict(arbitrary_types_allowed=True))
def paste_text(image: Image.Image, text: str, position: Tuple[int, int]):
    draw = ImageDraw.Draw(image)
    fnt = ImageFont.truetype(
        'data/fonts/LeagueGothic-Regular-VariableFont_wdth.ttf', 60)

    draw.text(position, text=text,
              font=fnt, fill=(0, 0, 0))
