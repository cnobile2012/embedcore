#
# beagleboard/beaglebone.py
#
"""
BeagleBone Board specific code.

by: Carl J. Nobile

email: carl.nobile@gmail.com
"""
__docformat__ = "restructuredtext en"


import re

from embedcore.boards import BoardsException
from embedcore.boards.boards_base import BoardsBase


class BeagleBoneException(BoardsException): pass


class BeagleBoneCore(BoardsBase):

    def __init__(self):
        super(BeagleBoneCore, self).__init__()

        # Allow this class to be called directly.
        if BoardsBase in self.__class__.__bases__:
            self._getBoardRevision()
            self._boardHook()

    def _getBoardRevision(self):
        raise BeagleBoneException("Possibly not a BeagleBone.")

    def _boardHook(self):
        """
        Sets up any board specific code like GPIO mappings, etc.
        """
        pass
