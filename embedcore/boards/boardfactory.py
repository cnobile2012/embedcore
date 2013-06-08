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
from embedcore.boards import BoardsException
from embedcore.boards.rpi import RaspberryPiCore
from embedcore.boards.beagleboard import BeagleBoneCore


# mro: BoardFactory -> RaspberryPiCore -> BeagleBoneCore -> BoardsBase -> object
class BoardFactory(RaspberryPiCore, BeagleBoneCore):
    """
    This class determines which board is in use. It runs the __init__ method
    from all subclasses till one succeeds.
    """

    def __init__(self):
        for klass in self.__class__.__bases__:
            try:
                klass.__init__(self)
                klass._getBoardRevision(self)
            except BoardsException, e:
                pass
            else:
                break

            msg = "None of the implemented boards were detected."
            raise BoardsException(msg)
