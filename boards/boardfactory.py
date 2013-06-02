#
# boards/boardfactory.py
#
"""
Generates the correct base class depending on the board that is plugged in.

by: Carl J. Nobile

email: carl.nobile@gmail.com
"""
__docformat__ = "restructuredtext en"


from boards.rpi import RaspberryPiCore, RaspberryPiException
from boards.beagleboard import BeagleBoneCore, BeagleBoneException


class BoardFactory(RaspberryPiCore, BeagleBoneCore):
    """
    This class determines which board is in use. It runs the _getBoardRevision
    method from all subclasses till one succeeds.
    """
    def __init__(self):
        pass

