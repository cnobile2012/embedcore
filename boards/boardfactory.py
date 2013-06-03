#
# boards/boardfactory.py
#
"""
Generates the correct base class depending on the board that is plugged in.

by: Carl J. Nobile

email: carl.nobile@gmail.com
"""
__docformat__ = "restructuredtext en"


from boards import BoardsException
from boards.rpi import RaspberryPiCore, RaspberryPiException
from boards.beagleboard import BeagleBoneCore, BeagleBoneException


class BoardFactory(RaspberryPiCore, BeagleBoneCore):
    """
    This class determines which board is in use. It runs the __init__ method
    from all subclasses till one succeeds.
    """
    __EXCLUDE = ("object", "BoardFactory", "BoardsBase",)

    def __init__(self):
        subs = [klass for klass in self.__class__.__mro__
                if klass.__name__ not in self.__EXCLUDE]

        for klass in subs:
            try:
                klass.__init__(self)
            except BoardsException, e:
                continue

            break
