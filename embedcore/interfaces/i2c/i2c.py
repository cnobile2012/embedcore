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

Where busnum is either 0 or 1.
"""
__docformat__ = "restructuredtext en"


import smbus

from embedcore.boards.boardfactory import BoardFactory


class I2CException(Exception): pass


class I2C(BoardFactory):
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

    def write8Bits(self, reg, value):
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

    def write16Bits(self, reg, value):
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

    def writeList(self, reg, list):
        """
        Writes an array of bytes using I2C format.
        """
        try:
            if self.debug:
                print "I2C: Writing list to register {0:#04x}:".format(reg)
                print list

            self.bus.write_i2c_block_data(self.address, reg, list)
        except IOError as err:
            return self._errMsg()

    def readList(self, reg, length):
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

    def readU8Bits(self, reg):
        """
        Read an unsigned byte from the I2C device.
        """
        try:
            result = self.bus.read_byte_data(self.address, reg)

            if self.debug:
                print ("I2C: Device {0:#04x} returned {0:#04x} from reg "
                       "{0:#04x}").format(self.address, result & 0xFF, reg)

            return result
        except IOError as err:
            return self._errMsg()

    def readS8Bits(self, reg):
        """
        Reads a signed byte from the I2C device.
        """
        try:
            result = self.bus.read_byte_data(self.address, reg)
            if result > 127: result -= 256

            if self.debug:
                print ("I2C: Device {0:#04x} returned {0:#04x} from "
                       "reg {0:#04x}").format(self.address, result & 0xFF, reg)

            return result
        except IOError as err:
            return self._errMsg()

    def readU16Bits(self, reg):
        """
        Reads an unsigned 16-bit value from the I2C device.
        """
        try:
            hibyte = self.readU8(reg)
            lobyte = self.readU8(reg+1)
            result = (hibyte << 8) + lobyte

            if self.debug:
                print ("I2C: Device {0:#04x} returned {0:#06x} from reg "
                       "{0:#04x}").format(self.address, result & 0xFFFF, reg)

            return result
        except IOError as err:
            return self._errMsg()

    def readS16Bits(self, reg):
        """
        Reads a signed 16-bit value from the I2C device.
        """
        try:
            hibyte = self.readS8(reg)
            lobyte = self.readU8(reg+1)
            result = (hibyte << 8) + lobyte

            if self.debug:
                print ("I2C: Device {0:#04x} returned {0:#x%06x} from reg "
                       "{0:#04x}").format(self.address, result & 0xFFFF, reg)

            return result
        except IOError as err:
            return self._errMsg()

    def readU16BitsReverse(self, reg):
        """
        Reads an unsigned 16-bit value from the I2C device with reverse byte
        order.
        """
        try:
            lobyte = self.readU8(reg)
            hibyte = self.readU8(reg+1)
            result = (hibyte << 8) + lobyte

            if self.debug:
                print ("I2C: Device {0:#04x} returned {0:#06x} from reg "
                       "{0:#04x}").format(self.address, result & 0xFFFF, reg)
            return result
        except IOError as err:
            return self._errMsg()

    def readS16BitsReverse(self, reg):
        """
        Reads a signed 16-bit value from the I2C device with reverse byte order.
        """
        try:
            lobyte = self.readS8(reg)
            hibyte = self.readU8(reg+1)
            result = (hibyte << 8) + lobyte

            if self.debug:
                print ("I2C: Device {0:#04x} returned {0:#06x} from reg "
                       "{0:#04x}").format(self.address, result & 0xFFFF, reg)

            return result
        except IOError as err:
            return self._errMsg()

    def _errMsg(self):
        print ("Error accessing {0:#04x}: Check your "
               "I2C address").format(self.address)
        return -1
