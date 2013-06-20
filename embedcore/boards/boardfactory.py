#
# boards/boardfactory.py
#
"""
Generates the correct base class depending on the board that is plugged in.

by: Carl J. Nobile

email: carl.nobile@gmail.com
"""
__docformat__ = "restructuredtext en"


import sys, traceback
from embedcore.boards import BoardException
from embedcore.boards.rpi import RaspberryPiCore
from embedcore.boards.beagleboard import BeagleBoneCore


# mro: BoardFactory -> RaspberryPiCore -> BeagleBoneCore -> BoardBase -> object
class BoardFactory(RaspberryPiCore, BeagleBoneCore):
    """
    This class determines which board is in use. It runs the __init__ method
    from all subclasses till one succeeds.
    """
    __SUBCLASSES = (RaspberryPiCore, BeagleBoneCore,)

    def __init__(self):
        for klass in self.__SUBCLASSES:
            try:
                klass.__init__(self)
                klass._getBoardRevision(self)
                klass._boardHook(self)
            except BoardException as e:
                # Look for an exception on a specific board then loop to test
                # the next board. If all boards raise an exception the loop
                # will fall through and a general BoardException will be raised.
                continue
            else:
                break

            msg = "None of the implemented boards were detected."
            raise BoardException(msg)
