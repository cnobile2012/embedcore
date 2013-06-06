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

from boards import BoardsException
from boards.boards_base import BoardsBase


class BeagleBoneException(BoardsException): pass


class BeagleBoneCore(BoardsBase):

    def __init__(self):
        super(BeagleBoneCore, self).__init__()

        # Allow this class to be called directly.
        if BoardFactory not in self.mro():
            self._getBoardRevision()

    def _getBoardRevision(self):
        print "BeagleBoneException"
        raise BeagleBoneException("Possibly not a BeagleBone.")
