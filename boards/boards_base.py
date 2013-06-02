#
# boards/boards_base.py
#
"""
Abstract boards base class.

by: Carl J. Nobile

email: carl.nobile@gmail.com
"""
__docformat__ = "restructuredtext en"


class BoardsBase(object):
    __ERROR_TEXT = "The method {} must be implemented."

    def __init__(self):
        self.boardRev = ""
        self.model = ""
        self.memory = 0
        self.i2cPort = -1

    def _getBoardRevision(self):
        """
        Gets the version number of the Raspberry Pi board.

        See Frank Carver's blog at http://raspberryalphaomega.org.uk/?p=428
        for the details on how to detect RPi versions.
        """
        raise NotImplementedError(
            self.__ERROR_TEXT.format(self._getBoardRevision.im_func.__name__))

    def getBoardRevision(self):
        return self.boardRev

    def getModel(self):
        return self.model

    def getMaxMemory(self):
        return self.memory

    def getI2CPort(self):
        return self.i2cPort
