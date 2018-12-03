import os
import sys
import unittest
import pytest

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))

from together.together import Together

@pytest.fixture
def together_name():
    return Together()
