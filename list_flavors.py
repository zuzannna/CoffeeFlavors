import json
from file_utilities import open_json, write_json
from text_tokenize_lemmatize import tokenizer_lemmatizer, stemmer
from spacy.en import English
from unidecode import unidecode
spacy_parser = English()

def list_flavors(flavor_table, level):

  """
  Calling the function in the terminal (python list_flavors.py) reads in the scaa_flavor_wheel.json file containing coffee flavors wheel and creates flavor_table.json saved in the current directory for further processing.

  flavor_table is a list of dictionaries containing information specific 
  to each level of coffee flavor wheel such that when you call e.g. 
  flavor_table[42] the output will be {u'level_1': u'Fruity', u'level_2': u'Other Fruit', u'level_3': u'Apple'}. This way, when looking for 
  "Apple" it is easy to find other tags associated with it from higher
  levels.

  Calling list_flavors(flavor_table, 1) from another function will query the flavor_table to return a list of strings with tags from a particular level
    (in this example, level 1: ['Nutty/Cocoa', 'Sour/Fermented',...,'Fruity']).


  input: list of dictionaries, int 
  output: list of str

  """

  key_str = 'level_{}'.format(level)
  return list(set([ f[key_str] for f in flavor_table if f[key_str] ]))

if __name__ == '__main__':
   flavor_dict = open_json('scaa_flavor_wheel.json')

   flavor_table = []

   for level_1 in flavor_dict['children']:
       for level_2 in level_1['children']:
           if 'children' in level_2.keys():
               for level_3 in level_2['children']:

                   level_1_flavor = stemmer(tokenizer_lemmatizer(level_1['flavor'],
                    spacy_parser, stopwords=[',', '.', '!', ';', ':', '?','and','a']))
                   level_2_flavor = stemmer(tokenizer_lemmatizer(level_2['flavor'],
                    spacy_parser, stopwords=[',', '.', '!', ';', ':', '?','and','a']))
                   level_3_flavor = stemmer(tokenizer_lemmatizer(level_3['flavor'],
                    spacy_parser, stopwords=[',', '.', '!', ';', ':', '?','and','a']))
                   
                   flavor_table.append({ 'level_1': str(level_1_flavor[0]), 
                    'level_2': str(level_2_flavor[0]), 'level_3': str(level_3_flavor[0])})
           else:
              level_1_flavor = stemmer(tokenizer_lemmatizer(level_1['flavor'],
                    spacy_parser, stopwords=[',', '.', '!', ';', ':', '?','and','a']))
              level_2_flavor = stemmer(tokenizer_lemmatizer(level_2['flavor'],
                    spacy_parser, stopwords=[',', '.', '!', ';', ':', '?','and','a']))
              flavor_table.append({ 'level_1': str(level_1_flavor[0]), 
                'level_2': str(level_2_flavor[0]), 'level_3':None})

   write_json(data=flavor_table, filepath="flavor_table.json")
   print "Wrote flavor wheel to file."