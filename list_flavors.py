import json
from file_utilities import open_json, write_json
from text_tokenize_lemmatize import tokenizer_lemmatizer, stemmer
from spacy.en import English
spacy_parser = English()

def list_flavors(flavor_table, level):

  """
  :usage: Calling the function in the terminal (python list_flavors.py) 
  reads in the scaa_flavor_wheel.json file containing coffee flavors 
  wheel and creates flavor_table.json and flavor_table_processed.json 
  saved in the current directory for further processing.

  Calling list_flavors(flavor_table, 1) from another function will 
  query the flavor_table to return a list of strings with tags from the
  particular level (in this example, 
  level 1: ['Nutty/Cocoa', 'Sour/Fermented',...,'Fruity']).

  

  flavor_table is a list of dictionaries containing information specific 
  to each level of coffee flavor wheel such that when you call e.g. 
  flavor_table[42] the output will be {u'level_1': u'Fruity', 
  u'level_2': u'Other Fruit', u'level_3': u'Apple'}. This way, when 
  looking for "Apple" [level 3] it is easy to find other tags 
  associated with it from higher levels.

  flavor_table_processed is the same as flavor_table except that it 
  contains entries which were tokenized, lemmatized and stemmed. 

  :param: list of dictionaries, int (level of flavor wheel)

  :returns: list of dictionaries
  
  :rvalue: unicode

  """

  key_str = 'level_{}'.format(level)
  return list(set([ f[key_str] for f in flavor_table if f[key_str] ]))

if __name__ == '__main__':
   flavor_dict = open_json('scaa_flavor_wheel.json')

   flavor_table_processed = []
   flavor_table = []

   for level_1 in flavor_dict['children']:
       for level_2 in level_1['children']:
           if 'children' in level_2.keys():
               for level_3 in level_2['children']:

                   level_1_flavor_processed = \
                   stemmer(tokenizer_lemmatizer(level_1['flavor'],
                    spacy_parser,\
                     stopwords=[',', '.', '!', ';', ':', '?','and','a']))
                   level_2_flavor_processed = \
                   stemmer(tokenizer_lemmatizer(level_2['flavor'],
                    spacy_parser,\
                     stopwords=[',', '.', '!', ';', ':', '?','and','a']))
                   level_3_flavor_processed = \
                   stemmer(tokenizer_lemmatizer(level_3['flavor'],
                    spacy_parser,\
                     stopwords=[',', '.', '!', ';', ':', '?','and','a']))
                   
                   flavor_table_processed.append\
                   ({ 'level_1': str(level_1_flavor_processed[0]), 
                    'level_2': str(level_2_flavor_processed[0]), 
                    'level_3': str(level_3_flavor_processed[0])})

                   flavor_table.append({ 'level_1': level_1['flavor'], 
                    'level_2': level_2['flavor'], 
                    'level_3': level_3['flavor']})
           else:
              flavor_table.append({ 'level_1': level_1['flavor'], 
                    'level_2': level_2['flavor'], 'level_3': None})

              level_1_flavor_processed = \
              stemmer(tokenizer_lemmatizer(level_1['flavor'],
                spacy_parser, \
                stopwords=[',', '.', '!', ';', ':', '?','and','a']))
              level_2_flavor_processed = \
              stemmer(tokenizer_lemmatizer(level_2['flavor'],
                spacy_parser, \
                stopwords=[',', '.', '!', ';', ':', '?','and','a']))
              
              flavor_table_processed.append\
              ({ 'level_1': str(level_1_flavor_processed[0]), 
                'level_2': str(level_2_flavor_processed[0]),
                 'level_3': None})

   write_json(data=flavor_table_processed, 
    filepath="flavor_table_processed.json")
   write_json(data=flavor_table, filepath="flavor_table.json")

   print "Wrote flavor wheel to file."