from PIL import Image, ImageDraw, ImageFont

from read_json import read_json
from create_stream_panel import create_stream_panel

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    stream_data_dicts = read_json()
    for stream_data_dict in stream_data_dicts:
        panel = create_stream_panel(stream_data_dict)
        panel.save(f'{stream_data_dict["title"]}.png')
