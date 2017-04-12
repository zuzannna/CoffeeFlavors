from unittest import TestCase
import file_utilities as u


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
