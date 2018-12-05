import os
import sys
import csv
import unittest
import pytest
import mock
# import unittest.mock

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))

from together.together import Together

class TogetherTest(unittest.TestCase):

    def setUp(self):
        self.together = Together('test_list.csv')

    def test_it_loads_input_file(self):
        with open(self.together.input_file) as f:
            t = csv.reader(f)
        assert '_csv.reader' in str(t)

    def test_it_loads_file_into_list(self):
        self.together.csv_read_to_list()
        assert type(self.together.name_list) == list
        assert len(self.together.name_list) == 5

    def test_it_chooses_group_size(self):
        with mock.patch('builtins.input', return_value='6'):
            self.together.set_group_size()
            assert self.together.group_size == 6
            assert type(self.together.group_size) == int
