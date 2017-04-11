import json


def open_json(filepath):
    with open(filepath) as f:
        notes = json.load(f)
    return notes

def write_json(data, filepath):
    with open(filepath, "w") as f:
        json.dump(data, f)

def find_labels(word, flavor_table, flavor_table_processed):
    for i,flavor in enumerate(flavor_table):
        if word in flavor_table_processed[i].values():
            if flavor_table_processed[i]['level_3'] and \
            word in flavor_table_processed[i]['level_3']: 
                #'None' returns a false in a conditional statement 
                # so we need to use this
                return flavor_table[i].values()
            elif word in flavor_table_processed[i]['level_2']:
                return [flavor_table[i]['level_1'], flavor_table[i]['level_2']]
            else:
                return [flavor_table[i]['level_1']]

