#
# boards/beagleboard/beaglebone.py
#
"""
BeagleBone Board specific code.

by: Carl J. Nobile

email: carl.nobile@gmail.com
"""
__docformat__ = "restructuredtext en"


import re

from embedcore.boards import BoardException
from embedcore.boards.boardbase import BoardBase


class BeagleBoneException(BoardException): pass


class BeagleBoneCore(BoardBase):

    def __init__(self):
        super(BeagleBoneCore, self).__init__()

        # Allow this class to be called directly.
        if BoardBase in self.__class__.__bases__:
            self._getBoardRevision()
            self._boardHook()

    def _getBoardRevision(self):
        raise BeagleBoneException("Possibly not a BeagleBone.")

    def _boardHook(self):
        """
        Sets up any board specific code like GPIO mappings, etc.
        """
        pass
