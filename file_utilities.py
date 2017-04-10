import json


def open_json(filepath):
    with open(filepath) as f:
        notes = json.load(f)
    return notes

def write_json(data, filepath):
    with open(filepath, "w") as f:
        json.dump(data, f)

def find_labels(word):
    for i,flavor in enumerate(flavor_table):
        if word in flavor_table[i].values():
            if flavor_table[i]['level_3'] == word:
                return flavor_table[i].values()
            elif flavor_table[i]['level_2'] == word:
                return [flavor_table[i]['level_1'], flavor_table[i]['level_2']]
            else:
                return [flavor_table[i]['level_1']]

