import os
import sys
import csv
import unittest
import pytest
import mock

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))

from together.together import Together

class TogetherTest(unittest.TestCase):

    def setUp(self):
        self.together = Together('test_list.csv')
        self.together.load_input_file()
        self.together.csv_read_to_list()

    def test_it_loads_input_file(self):
        with open(self.together.input_file) as f:
            t = csv.reader(f)
        assert '_csv.reader' in str(t)

    def test_it_loads_file_into_list(self):
        assert type(self.together.name_list) == list
        assert len(self.together.name_list) == 5

    def test_it_chooses_group_size(self):
        with mock.patch('builtins.input', return_value='6'):
            self.together.set_group_size()
            assert self.together.group_size == 6
            assert type(self.together.group_size) == int

    def test_it_processes_the_list(self):
        self.together.csv_read_to_list()
        self.together.group_size = 2
        self.together.process_list()
        assert self.together.group_size == len(max(self.together.output_list, key=len))

    def test_it_dedupes_the_list(self):
        self.together.csv_read_to_list()
        self.together.name_list.append('Tim')
        self.together.group_size = 2
        self.together.process_list()
        assert self.together.group_size != len(self.together.name_list)


    def test_it_writes_list_to_csv(self):
        self.together.csv_read_to_list()
        self.together.group_size = 2
        self.together.process_list()
        self.together.write_list_to_csv()
        assert os.path.isfile('{}.output'.format(self.together.input_file))
        os.remove('{}.output'.format(self.together.input_file))
