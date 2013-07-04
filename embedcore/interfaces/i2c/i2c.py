#
# interfaces/i2c/i2c.py
#
"""
This package is a redesign of the Adafruit Raspberry-Pi-Python-Code library.
Which can be gotten here:
    https://github.com/adafruit/Adafruit-Raspberry-Pi-Python-Code

My implimentation can be installed using PIP or easy_install and uses the
standard python package management.

$ sudo nano /etc/modules

Add:
----
i2c-bcm2708
i2c-dev

$ sudo modprobe i2c-dev
$ i2cdetect -y busnum

Where busnum is either 0 or 1 depending on the RPi version.
"""
__docformat__ = "restructuredtext en"


import smbus

from embedcore.boards.boardfactory import BoardFactory
from embedcore.utilities import Utilities


class I2CException(Exception): pass


class I2C(BoardFactory, Utilities):
    """
    This class implements the interface for the I2C protocol.
    """
    def __init__(self, address, busnum=-1, debug=False):
        """
        Alternatively, you can hard-code the bus version below:
        self.bus = smbus.SMBus(0); # Force I2C0 (early 256MB Pi's)
        self.bus = smbus.SMBus(1); # Force I2C1 (512MB Pi's)
        """
        super(I2C, self).__init__()
        self.address = address
        self.bus = smbus.SMBus(busnum >= 0 and busnum or self.getI2CPort())
        self.debug = debug

    def readByteData(self, reg, signed=False):
        """
        Read an 8-bit value from a specific register/address.


        """
        try:
            result = self.bus.read_byte_data(self.address, reg)

            if signed and result > 127:
                result -= 256

            if self.debug:
                print ("I2C: Device {0:#04x} returned {0:#04x} from reg "
                       "{0:#04x}").format(self.address, result & 0xFF, reg)

            return result
        except IOError as err:
            return self._errMsg()

    def writeByteData(self, reg, value):
        """
        Writes an 8-bit value to the specified register/address.
        """
        try:
            self.bus.write_byte_data(self.address, reg, value)

            if self.debug:
                print ("I2C: Wrote {0:#04x} to register "
                       "{0:#04x}").format(value, reg)
        except IOError as err:
            return self._errMsg()

    def readWordData(self, reg, signed=False, reverse=False):
        """
        Read a 16-bit value from a specific register/address.


        """
        try:
            hiByte = self.readByteData(reg, signed=signed)
            loByte = self.readByteData(reg+1) #, signed=signed)

            if reverse:
                result = (loByte << 8) + hiByte
            else:
                result = (hiByte << 8) + loByte

            if self.debug:
                print ("I2C: Device {0:#04x} returned {0:#06x} from reg "
                       "{0:#04x}").format(self.address, result & 0xFFFF, reg)

            return result
        except IOError as err:
            return self._errMsg()

    def writeWordData(self, reg, value):
        """
        Writes a 16-bit value to the specified register/address pair.
        """
        try:
            self.bus.write_word_data(self.address, reg, value)

            if self.debug:
                print ("I2C: Wrote {0:#04x} to register pair "
                       "{0:#04x},{0:#04x}").format(value, reg, reg+1)
        except IOError as err:
            return self._errMsg()

    def readBlockData(self, reg, length):
        """
        Read a list of bytes from the I2C device.
        """
        try:
            results = self.bus.read_i2c_block_data(self.address, reg, length)

            if self.debug:
                print ("I2C: Device {0:#04x} returned the following from reg "
                       "{0:#04x}").format(self.address, reg)
                print results

            return results
        except IOError as err:
            return self._errMsg()

    def writeBlockData(self, reg, block):
        """
        Writes an array of bytes using I2C format.
        """
        try:
            if self.debug:
                print "I2C: Writing block to register {0:#04x}:".format(reg)
                print block

            self.bus.write_i2c_block_data(self.address, reg, block)
        except IOError as err:
            return self._errMsg()

    def _errMsg(self):
        print ("Error accessing {0:#04x}: Check your "
               "I2C address").format(self.address)
        return -1
