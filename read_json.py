import json
from pathlib import Path


def read_json(path: Path = Path("data/data.json")):
    json_file = path.read_text()
    data_dict = json.loads(json_file)
    return data_dict
