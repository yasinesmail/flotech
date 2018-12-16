import unittest
from unittest.mock import MagicMock
from unittest.mock import Mock

from Jug import Jug
from JugStates import JugStates

class JugTest(unittest.TestCase):

    #def setUp(self):
        #self.jug = new Jug(5)

    #def tearDown(self):
        #self.jug.dispose()

    def test_Initialize(self):
        jug = Jug(5)
        assert jug.state is JugStates.EMPTY
        assert jug.water_in_jug == 0
        assert jug.jug_size == 5

    def test_InitInstance(self):
        jug = Jug.getInstance(10)
        assert jug.state is JugStates.EMPTY
        assert jug.water_in_jug == 0
        assert jug.jug_size == 10

    def test_InitInstanceError(self):
        with self.assertRaises(Exception) as cm:
            jug = Jug.getInstance(0)

        the_exception = cm.exception
        assert str(the_exception) == 'Jug size should be greater zero.'

    def test_JugCapcityAtStart(self):
        jug = Jug.getInstance(8)
        assert jug.jug_capacity() == 8

    def test_JugCapcityAtFull(self):
        jug = Jug.getInstance(8)
        jug.full()
        assert jug.jug_capacity() == 0

    def test_JugCapcityAtHalf(self):
        jug = Jug.getInstance(8)
        jug.add_water(4)
        assert jug.jug_capacity() == 4

    def test_JugCapcityAddMoreThanCapacity(self):
        jug = Jug.getInstance(8)
        jug.add_water(10)
        assert jug.jug_capacity() == 0

    def test_AddWaterPartial(self):
        jug = Jug.getInstance(8)
        jug.add_water(2)
        assert jug.jug_capacity() == 6
        assert jug.water_in_jug == 2
        assert jug.state is JugStates.PARTIAL

    def test_AddWaterFull(self):
        jug = Jug.getInstance(8)
        jug.add_water(12)
        assert jug.jug_capacity() == 0
        assert jug.water_in_jug == 8
        assert jug.state is JugStates.FULL

    def test_AddWaterException_ZeroWaterAdded(self):
        jug = Jug.getInstance(8)
        with self.assertRaises(Exception) as cm:
            jug.add_water(0)
        the_exception = cm.exception
        assert str(the_exception) == 'No water amount specified to add.'

    def test_AddWaterException_JugIsFull(self):
        jug = Jug.getInstance(8)
        jug.add_water(8)
        with self.assertRaises(Exception) as cm:
            jug.add_water(2)
        the_exception = cm.exception
        assert str(the_exception) == 'Jug is full, no more water can be added.'

    def test_RemoveWaterPartial(self):
        jug = Jug.getInstance(8)
        jug.full()

        jug.remove_water(2)
        assert jug.jug_capacity() == 2
        assert jug.water_in_jug == 6
        assert jug.state is JugStates.PARTIAL

    def test_RemoveWaterFull(self):
        jug = Jug.getInstance(8)
        jug.full()

        jug.remove_water(12)
        assert jug.jug_capacity() == 8
        assert jug.water_in_jug == 0
        assert jug.state is JugStates.EMPTY

    def test_RemoveWaterException_ZeroWaterAdded(self):
        jug = Jug.getInstance(8)
        with self.assertRaises(Exception) as cm:
            jug.remove_water(0)
        the_exception = cm.exception
        assert str(the_exception) == 'No water amount specified to remove.'

    def test_RemoveWaterException_JugIsEmpty(self):
        jug = Jug.getInstance(8)
        with self.assertRaises(Exception) as cm:
            jug.remove_water(2)
        the_exception = cm.exception
        assert str(the_exception) == 'Jug is empty, no more water can be removed.'


if __name__ == '__main__':
    unittest.main()
