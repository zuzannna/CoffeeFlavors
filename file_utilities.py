import json

"""
These are some helper functions for Coffee Flavor project.
"""

def open_json(filepath):
    """
    Returns open .json file in python as a list.

    :param: .json file path

    :returns: list

    :rvalue: str
    """
    with open(filepath) as f:
        notes = json.load(f)
    return notes


def write_json(data, filepath):
    """
    Writes .json file from data dump.

    :param: data, .json file path

    :returns: .json file

    """
    with open(filepath, "w") as f:
        json.dump(data, f)


def find_labels(word, flavor_table, flavor_table_processed):
    
    """
    Searches flavor_table_processed containing tokenized, lemmatized 
    and stemmed words to find appropriate tags and returns 
    corresponding non processed tags from flavor_table. 

    :param: str, list of dictionaries, list of dictionaries

    :returns: list of lists

    :rvalue: str
    """

    # First check if word is in the flavor wheel at all
    flavors = open_json('flavors.json')

    if word in flavors:
        
        # If the searched word is in the list containing all words
        # from the flavor wheel proceed to find the match and 
        # its parents

        for i,flavor in enumerate(flavor_table):
            if word in flavor_table_processed[i].values():
                if flavor_table_processed[i]['level_3'] and \
                word in flavor_table_processed[i]['level_3']: 
                #'None' returns a false in a conditional statement 
                # so we need to use this
                    return flavor_table[i].values()
                elif word in flavor_table_processed[i]['level_2']:
                    return [flavor_table[i]['level_1'], \
                    flavor_table[i]['level_2']]
                else:
                    return [flavor_table[i]['level_1']]

