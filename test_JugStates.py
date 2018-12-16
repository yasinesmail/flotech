import unittest
from unittest.mock import MagicMock
from unittest.mock import Mock

from JugStates import JugStates

class JugStatesTest(unittest.TestCase):

    def test_JugStatesCount(self):
        numOfStates = list(JugStates)
        assert len(numOfStates) == 3

    def test_JugCheckStates(self):
        assert JugStates.EMPTY.value == 0
        assert JugStates.FULL.value == 1
        assert JugStates.PARTIAL.value == 2
