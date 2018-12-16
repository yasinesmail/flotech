
class JugAction:

    @staticmethod
    def fill(jug):
        jug.full()


    @staticmethod
    def empty(jug):
        jug.empty()


    @staticmethod
    def transfer(jugSrc, jugDst):

        waterInSrc = jugSrc.water_in_jug
        dstCapacity = jugDst.jug_capacity()

        if waterInSrc >= dstCapacity:
            waterToTransfer = dstCapacity
        else:
            waterToTransfer = waterInSrc

        jugSrc.remove_water(waterToTransfer)
        jugDst.add_water(waterToTransfer)
