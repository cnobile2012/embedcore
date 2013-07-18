#
# 
#
"""
This package provides some bit twiddling functions

by: Carl J. Nobile

email: carl.nobile@gmail.com
"""
__docformat__ = "restructuredtext en"


class Utilities(object):

    def reverseByteOrder(self, data):
        """
        Reverses the byte order of an int (16-bit) or long (32-bit) value.
        """
        # Courtesy Vishal Sapre
        byteCount = len(hex(data)[2:].replace('L','')[::2])
        val = 0

        for i in range(byteCount):
            val = (val << 8) | (data & 0xff)
            data >>= 8

        return val
