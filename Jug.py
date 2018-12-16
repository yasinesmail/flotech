
from JugStates import JugStates

class Jug:

    __slots__ = ['_jug_size', '_water_in_jug', '_state']

    def __init__(self, jugSize):
        if jugSize <= 0:
            raise Exception('Jug size should be greater zero.')

        self._jug_size = jugSize
        self._water_in_jug = 0
        self._state = JugStates.EMPTY

    @staticmethod
    def getInstance(jugSize):
        return Jug(jugSize)


    @property
    def jug_size(self):
        return self._jug_size


    @property
    def water_in_jug(self):
        return self._water_in_jug


    @property
    def state(self):
        return self._state


    def jug_capacity(self):
        return self.jug_size - self.water_in_jug


    def empty(self):
        self._water_in_jug = 0
        self._state = JugStates.EMPTY


    def full(self):
        self._water_in_jug = self.jug_size
        self._state = JugStates.FULL


    def add_water(self, waterAmount):
        if not waterAmount:
            raise Exception('No water amount specified to add.')

        if self._state is JugStates.FULL:
            raise Exception('Jug is full, no more water can be added.')

        waterCapacityLeftInJug = self.jug_capacity()
        if waterAmount >= waterCapacityLeftInJug:
            self.full()
        else:
            self._water_in_jug += waterAmount
            self._state = JugStates.PARTIAL


    def remove_water(self, waterAmount):
        if not waterAmount:
            raise Exception('No water amount specified to remove.')

        if self._state is JugStates.EMPTY:
            raise Exception('Jug is empty, no more water can be removed.')

        waterInJug = self.water_in_jug
        if waterAmount >= waterInJug:
            self.empty()
        else:
            self._water_in_jug = waterInJug - waterAmount
            self._state = JugStates.PARTIAL
