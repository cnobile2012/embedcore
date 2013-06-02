#
# rpi/__init__.py
#
"""
Raspberry PI specific code.

by: Carl J. Nobile

email: carl.nobile@gmail.com
"""
__docformat__ = "restructuredtext en"


import re


class RaspberryPiException(Exception): pass


class RaspberryPiCore(object):
    REVISIONS = {'0x2': ('B1', 256, 0), '0x3': ('B1+', 256, 0),
                 '0x4': ('B2', 256, 1), '0x5': ('B2', 256, 1),
                 '0x6': ('B2', 256, 1), '0x7': ('A', 256, 1),
                 '0x8': ('A', 256, 1), '0x9': ('A', 256, 1),
                 '0xd': ('B2', 512, 1), '0xe': ('B2', 512, 1),
                 '0xf': ('B2', 512, 1),
                 }
    DEFAULT_REV = "0x0"

    def __init__(self):
        self.boardRev = self.DEFAULT_REV
        self.model = ""
        self.memory = 0
        self.i2cPort = 0
        self._getBoardRevision()

    def _getBoardRevision(self):
        """
        Gets the version number of the Raspberry Pi board.

        See Frank Carver's blog at http://raspberryalphaomega.org.uk/?p=428
        for the details on how to detect RPi versions.
        """
        try:
            with open('/proc/cmdline', 'r') as f:
                m = re.search('bcm2708.boardrev=(0x[0123456789abcdef]*) ',
                              f.readline())

                if m is None:
                    raise RaspberryPiException("Possibly not a Raspberry Pi.")

                self.boardRev = m.group(1)
        except Exception, e:
            raise e

        self.model, self.memory, self.i2cPort = self.REVISIONS[self.boardRev]

    def getBoardRevision(self):
        return self.boardRev

    def getModel(self):
        return self.model

    def getMaxMemory(self):
        return self.memory

    def getI2CPort(self):
        return self.i2cPort
