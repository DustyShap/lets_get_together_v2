import os
import sys
import csv
import unittest
import pytest
import mock

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))

from together.together import Together

class TogetherFaker(unittest.TestCase):

    def setUp(self):
        self.together = Together('faker')

    def test_faker_names_setup(self):
        with mock.patch('builtins.input', return_value='6'):
            self.together.set_faker_names_length()
            assert self.together.faker_names_amount == 6

            #Test names populate
            self.together.set_faker_names_list()
            assert len(self.together.name_list) == 6


class TogetherTest(unittest.TestCase):

    def setUp(self):
        self.together = Together('test_list.txt')
        self.together.load_input_file()
        self.together.file_read_to_list()

    def test_it_loads_input_file(self):
        with open(self.together.input) as f:
            assert 'Tim' == list(f)[1].strip()

    def test_it_loads_file_into_list(self):
        assert type(self.together.name_list) == list
        assert len(self.together.name_list) == 5

    def test_it_chooses_group_size(self):
        with mock.patch('builtins.input', return_value='6'):
            self.together.set_group_size()
            assert self.together.group_size == 6
            assert type(self.together.group_size) == int

    def test_it_processes_the_list(self):
        self.together.file_read_to_list()
        self.together.group_size = 2
        self.together.process_list()
        assert self.together.group_size == len(max(self.together.output_list, key=len))

    def test_it_dedupes_the_list(self):
        self.together.file_read_to_list()
        self.together.name_list.append('Tim')
        self.together.group_size = 2
        self.together.process_list()
        assert self.together.group_size != len(self.together.name_list)

# class LocationTests(unittest.TestCase):
#     def setUp(self):
#         self.together = Together('test_list.txt')
#
#     def tearDown(self):
#         self.name_file.close()
#
#     def test_to_see_if_file_exists(self):
#         self.assertTrue(self.name_file)
#
#     def test_to_see_if_groups_by_unique_city(self):
#         self.assertEqual(NUM_CITIES, len(group_by_location('names.txt').keys()))
#
#     def test_to_ensure_group_size(self):
#         oversize = False
#         #Assert that any of the groups generated didn't exceed group number
#         records = group_by_location('names.txt')
#         # self.assertTrue(get_group_size(records,GROUP_SIZE) <= GROUP_SIZE)
#         lists = get_group_size(records, GROUP_SIZE)
#         for list in lists:
#             for i in list:
#                 if len(i) > GROUP_SIZE:
#                     oversize = True
#         self.assertFalse(oversize)
