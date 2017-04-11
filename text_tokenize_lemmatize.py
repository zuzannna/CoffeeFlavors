import io, os
import json

#import nltk
from nltk.stem.porter import PorterStemmer



from spacy.en import English
from stop_words import get_stop_words

from file_utilities import open_json, write_json


def spacy_sent_word_tokenizer(text, parser):
    """
    Take a unicode string of text and return a list of sentences, each containing a list of tokens
    Output: list of lists
    """
    parsed_data = parser(text)
    tokenized_sents = [[parsed_data[i].string for i in range(span.start, span.end)] for span in parsed_data.sents]

    return tokenized_sents


def tokenizer(text, parser):
    """
    Take a unicode string of text and return a list containing the tokens
    Output: list of single tokens
    """
    parsed_data = parser(text)
    list_of_tokens = [token for token in parsed_data]

    return list_of_tokens


def tokenizer_lemmatizer(text, parser, stopwords=[]):
    """
    Take a unicode string of text and return a list containing the lemmatized tokens
    Output: list of lemmatized tokens
    """
    parsed_data = parser(text)
    list_of_lemmatized_tokens = \
        [token.lemma_ for token in parsed_data if not str(token) in stopwords]

    return list_of_lemmatized_tokens


def stemmer(tokenized_text):
    """
    Take a unicode string of text and return a list containing the stemmed tokens
    Output: list of stemmed tokens
    """
    stemmer = PorterStemmer()
    return [stemmer.stem(plural) for plural in tokenized_text]


def list_bigrams(text, parser):
    list_of_tokens = spacy_tokenizer(text, parser)
    list_of_bigrams = []

    for i in range(1, len(list_of_tokens)):
        list_of_bigrams.append(list_of_tokens[i-1] + " " + list_of_tokens[i])

    return list_of_bigrams


if __name__ == '__main__':
    spacy_parser = English()

    list_of_tasting_notes = open_json("tasting_notes.json")
    print "Read {} tasting notes from json.".format(len(list_of_tasting_notes))

    lemmatized_notes = \
        [tokenizer_lemmatizer(
            tasting_notes, spacy_parser, stopwords=[',', '.', '!', ';', ':', '?','and','a','-'])
         for tasting_notes in list_of_tasting_notes]

    print "Created lemmatized notes. Example:", lemmatized_notes[0]

    write_json(data=lemmatized_notes, filepath="lemmatized_notes.json")

    print "Wrote notes to file."