from unittest import TestCase
import file_utilities as u
from coffee_flavors import coffee_flavors as coffee
from text_tokenize_lemmatize as text_

#################################
# Tests for CoffeeFlavors library
#################################

class TestUtilities(TestCase):

    def test_find_labels(self):

        flavor_table_ = [{u'level_1': u'Roasted', 
        u'level_2': u'Pipe Tobacco', u'level_3': None}]
        expected_output = [u'Roasted']
        actual_output = u.find_labels('Roasted', flavor_table_, 
        flavor_table_)
        self.assertEqual(expected_output, actual_output)


    def test_coffee_flavors(self):

        text = 'blackberries with hints of pineapple'
        expected_output = [[u'Fruity', u'Berry', u'Blackberry'],
        [u'Fruity', u'Other Fruit', u'Pineapple']]
        actual_output = coffee.coffee_flavors(text)
        self.assertEqual(expected_output, actual_output)


    def test_tokenizer_lemmatizer(self):
        
        spacy_parser = English()
        stopwords=[',', '.', '!', ';', ':', '?','and','a','-']
        text = 'blackberries with hints of pineapple'
        expected_output = [u'blackberry', u'with', u'hint', 
        u'of', u'pineapple']
        actual_output = text_.tokenizer_lemmatizer(unicode(text),
            spacy_parser, stopwords=stopwords)

    def test_stemmer(self):
        
        tokens = [u'Fruity', u'Other Fruit', u'Pineapple']
        expected_output = [u'Fruiti', u'Other Fruit', u'Pineappl']
        actual_output = text_.stemmer(tokens)
        self.assertEqual(expected_output, actual_output)
