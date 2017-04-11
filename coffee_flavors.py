import json
from file_utilities import open_json, write_json, find_labels
from text_tokenize_lemmatize import tokenizer_lemmatizer, stemmer
from spacy.en import English

"""
Wrapper function that called from the terminal will ask for an input 
(a sentence / coffee review) and after comparing it to the flavor table 
will return a list of tags.

:params: str 

:returns: list of lists

:rvalue: str 

"""


spacy_parser = English()

if __name__ == '__main__':
	
	flavor_table = open_json(filepath='flavor_table.json')
	flavor_table_processed = \
	open_json(filepath='flavor_table_processed.json')

	tags = []
	sentence = raw_input()

	tokenized_sentence = tokenizer_lemmatizer(
	            unicode(sentence), spacy_parser, stopwords=
	            [',', '.', '!', ';', ':', '?','and','a','-'])
	stemmed_tokenized_sentence = stemmer(tokenized_sentence)


	for word in stemmed_tokenized_sentence:   
	    tags.append(find_labels(word, flavor_table, 
	    	flavor_table_processed))
	tags = filter(None, tags)

	print tags