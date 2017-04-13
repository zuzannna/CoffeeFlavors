import io, os
import json
from nltk.stem.porter import PorterStemmer
from spacy.en import English
from file_utilities import open_json, write_json

"""
These are some helper functions for NLP analysis for the Coffee
Flavors project. 
"""

def tokenizer_lemmatizer(text, parser, stopwords=[]):
    """
    Take a unicode string of text and return a list containing the 
    lemmatized tokens
    
    :param: unicode, parser, list of unicode strings
    
    :returns: list of lemmatized tokens

    :rvalue: unicode
    """
    parsed_data = parser(text)
    list_of_lemmatized_tokens = \
        [token.lemma_ for token in parsed_data if not str(token) \
        in stopwords]

    return list_of_lemmatized_tokens


def stemmer(tokenized_text):
    """
    Take a unicode string of text and return a list containing the 
    stemmed tokens

    :param: list of unicode

    :returns: list

    :rvalue: unicode
    """
    stemmer = PorterStemmer()
    return [stemmer.stem(plural) for plural in tokenized_text]


def list_bigrams(text, parser):
    """
    Take a unicode string of text and return a list containing the 
    bigrams

    :param: list of unicode

    :returns: list

    :rvalue: unicode
    """
    list_of_tokens = spacy_tokenizer(text, parser)
    list_of_bigrams = []

    for i in range(1, len(list_of_tokens)):
        list_of_bigrams.append(list_of_tokens[i-1] \
            + " " + list_of_tokens[i])

    return list_of_bigrams


if __name__ == '__main__':
    """
    Take a unicode list of strings and return a list containing the 
    stemmed and lemmatized tokens

    :param: list of unicode

    :returns: list

    :rvalue: unicode
    """
    spacy_parser = English()
    list_of_tasting_notes = open_json("tasting_notes.json")
    print \
    "Read {} tasting notes from json.".format(len(list_of_tasting_notes))

    lemmatized_notes = \
        [tokenizer_lemmatizer(
            tasting_notes, spacy_parser, 
            stopwords=[',', '.', '!', ';', ':', '?','and','a','-'])
         for tasting_notes in list_of_tasting_notes]

    print "Created lemmatized notes. Example:", lemmatized_notes[0]

    write_json(data=lemmatized_notes, filepath="lemmatized_notes.json")

    print "Wrote notes to file."