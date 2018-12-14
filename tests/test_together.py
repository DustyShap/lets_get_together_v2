# pylint: disable=missing-docstring,wrong-import-position,invalid-name,redefined-outer-name

import os
import sys
import pytest
import mock

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))

from together.together import Together

@pytest.fixture
def together():
    together = Together('test_list.txt')
    together.load_input_file()
    together.file_read_to_list()
    return together

@pytest.fixture
def faker_together():
    return Together('faker')


def test_it_loads_input_file(together):
    with open(together.input) as f:
        assert list(f)[1].strip() == 'Tim'

def test_it_loads_file_into_list(together):
    assert isinstance(together.name_list, list)
    assert len(together.name_list) == 5

def test_faker_names_setup(faker_together):
    with mock.patch('builtins.input', return_value='6'):
        faker_together.set_faker_names_length()
        assert faker_together.faker_names_amount == 6
        faker_together.set_faker_names_list()
        assert len(faker_together.name_list) == 6

def test_it_chooses_group_size(together):
    with mock.patch('builtins.input', return_value='6'):
        together.set_group_size()
        assert together.group_size == 6
        assert isinstance(together.group_size,int)

def test_it_processes_the_list(together):
    together.file_read_to_list()
    together.group_size = 2
    together.process_list()
    assert together.group_size == len(max(together.output_list, key=len))

def test_it_dedupes_the_list(together):
    together.file_read_to_list()
    together.name_list.append('Tim')
    together.group_size = 2
    together.process_list()
    assert together.group_size != len(together.name_list)
