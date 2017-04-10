import json


def open_json(filepath):
    with open(filepath) as f:
        notes = json.load(f)
    return notes

def write_json(data, filepath):
    with open(filepath, "w") as f:
        json.dump(data, f)

