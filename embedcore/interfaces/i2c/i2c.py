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
import logging

from embedcore.boards.boardfactory import BoardFactory
from embedcore.utilities import Utilities, LoggingConfig


class I2CException(Exception): pass


class I2C(BoardFactory, LoggingConfig, Utilities):
    """
    This class implements the interface for the I2C protocol.
    """
    _ERROR_MSG = "Error accessing {0:#04x}: Check your I2C address, {}"

    def __init__(self, address, busnum=-1, debug=False):
        """
        Alternatively, you can hard-code the bus version below:
        self.bus = smbus.SMBus(0); # Force I2C0 (early 256MB Pi's)
        self.bus = smbus.SMBus(1); # Force I2C1 (512MB Pi's)
        """
        BoardFactory.__init__(self)
        LoggingConfig.__init__(
            self, level=debug and logging.DEBUG or logging.WARNING)
        self.address = address
        self.bus = smbus.SMBus(busnum >= 0 and busnum or self.getI2CPort())
        self.debug = debug

    def readByteData(self, cmd, signed=False):
        """
        Read an 8-bit data from a register with a specific command.


        """
        try:
            result = self.bus.read_byte_data(self.address, cmd)

            if signed and result > 127:
                result -= 256

            self.log.debug("I2C: Device 0x%02x returned 0x%02x from cmd 0x%02x",
                           self.address, result & 0xFF, cmd)
        except IOError as err:
            raise I2CException(self._ERROR_MSG.format(self.address, err))

        return result

    def writeByteData(self, cmd, value):
        """
        Writes an 8-bit data to .
        """
        try:
            self.bus.write_byte_data(self.address, cmd, value)
            self.log.debug("I2C: Wrote 0x%02x to register 0x%02x", value, cmd)
        except IOError as err:
            raise I2CException(self._ERROR_MSG.format(self.address, err))

    def readWordData(self, cmd, signed=False, reverse=False):
        """
        Read 16-bit data from a specific register/address.


        """
        try:
            hiByte = self.readByteData(cmd, signed=signed)
            loByte = self.readByteData(cmd+1) #, signed=signed)

            if reverse:
                result = (loByte << 8) + hiByte
            else:
                result = (hiByte << 8) + loByte

            self.log.debug("I2C: Device 0x%02x returned 0x%04x from cmd 0x%02x",
                           self.address, result & 0xFFFF, cmd)
        except IOError as err:
            raise I2CException(self._ERROR_MSG.format(self.address, err))

        return result

    def writeWordData(self, cmd, value):
        """
        Writes a 16-bit data to the specified register/address pair.
        """
        try:
            self.bus.write_word_data(self.address, cmd, value)
            self.log.debug("I2C: Wrote 0x%02x to register pair 0x%02x,0x%02x",
                           value, cmd, cmd+1)
        except IOError as err:
            raise I2CException(self._ERROR_MSG.format(self.address, err))

    def readNBytesData(self, cmd, length):
        """
        Read a list of bytes from the I2C device.
        """
        #if length > 32: length = 32

        try:
            results = self.bus.read_i2c_block_data(self.address, cmd, length)
            self.log.debug("I2C: Device 0x%02x returned the following from cmd "
                           "0x%02x\n%s", self.address, cmd, results
        except IOError as err:
            raise I2CException(self._ERROR_MSG.format(self.address, err))

        return results

    def writeBlockData(self, cmd, block):
        """
        Writes an array of bytes using I2C format.
        """
        try:
            self.bus.write_i2c_block_data(self.address, cmd, block)
            self.log.debug("I2C: Writing block to register 0x%02x: %s",
                           cmd, block)
        except IOError as err:
            raise I2CException(self._ERROR_MSG.format(self.address, err))
