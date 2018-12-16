
import unittest
from unittest.mock import MagicMock
from unittest.mock import Mock

from Jug import Jug
from JugStates import JugStates
from JugAction import JugAction

class JugActionTest(unittest.TestCase):

    def test_TranserAllWaterFromSrcToDst(self):

        jugSrc = Jug(5)
        jugSrc.add_water(5)
        jugDst = Jug(8)

        JugAction.transfer(jugSrc, jugDst)
        assert jugSrc.water_in_jug == 0
        assert jugSrc.state is JugStates.EMPTY
        assert jugDst.water_in_jug == 5
        assert jugDst.state is JugStates.PARTIAL


    def test_TranserPartWaterFromSrcToDst(self):

        jugSrc = Jug(5)
        jugSrc.add_water(5)
        jugDst = Jug(2)

        JugAction.transfer(jugSrc, jugDst)
        assert jugSrc.water_in_jug == 3
        assert jugSrc.state is JugStates.PARTIAL
        assert jugDst.water_in_jug == 2
        assert jugDst.state is JugStates.FULL


    def test_TranserEqualtWaterFromSrcToDst(self):

        jugSrc = Jug(5)
        jugSrc.add_water(5)
        jugDst = Jug(5)

        JugAction.transfer(jugSrc, jugDst)
        assert jugSrc.water_in_jug == 0
        assert jugSrc.state is JugStates.EMPTY
        assert jugDst.water_in_jug == 5
        assert jugDst.state is JugStates.FULL


    def test_Fill(self):

        jug = Jug(5)
        JugAction.fill(jug)

        assert jug.water_in_jug == 5
        assert jug.state is JugStates.FULL


    def test_Empty(self):

        jug = Jug(5)
        JugAction.empty(jug)

        assert jug.water_in_jug == 0
        assert jug.state is JugStates.EMPTY
