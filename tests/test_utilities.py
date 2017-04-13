import unittest
import sys, os, os.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")
import src.file_utilities as u
import coffee_flavors as coffee
import src.text_tokenize_lemmatize as t
from spacy.en import English



#################################
# Tests for CoffeeFlavors library
#################################

class TestUtilities(unittest.TestCase):

    def test_find_labels(self):

        flavor_table_ = [{u'level_1': u'sweet', u'level_2': u'brown',
         u'level_3': u'molass'}]
        expected_output = [u'sweet', u'brown', u'molass']
        text = 'molass'
        actual_output = u.find_labels(text, 
            flavor_table=flavor_table_, 
            flavor_table_processed=flavor_table_)
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
        actual_output = t.tokenizer_lemmatizer(unicode(text),
            spacy_parser, stopwords=stopwords)

    def test_stemmer(self):
        
        tokens = [u'Fruity', u'Other Fruit', u'Pineapple']
        expected_output = [u'Fruiti', u'Other Fruit', u'Pineappl']
        actual_output = t.stemmer(tokens)
        self.assertEqual(expected_output, actual_output)


if __name__ == '__main__':
    unittest.main()
