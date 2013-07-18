#
# boards/rpi/raspberrypi.py
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.
#
"""
Raspberry PI specific code.

by: Carl J. Nobile

email: carl.nobile@gmail.com
"""
__docformat__ = "restructuredtext en"


import re

from embedcore.boards import BoardException
from embedcore.boards.boardbase import BoardBase


class RaspberryPiException(BoardException): pass


class RaspberryPiCore(BoardBase):
    RPI_REVISIONS = {'0x2': ('B1', 256, 0), '0x3': ('B1+', 256, 0),
                     '0x4': ('B2', 256, 1), '0x5': ('B2', 256, 1),
                     '0x6': ('B2', 256, 1), '0x7': ('A', 256, 1),
                     '0x8': ('A', 256, 1), '0x9': ('A', 256, 1),
                     '0xd': ('B2', 512, 1), '0xe': ('B2', 512, 1),
                     '0xf': ('B2', 512, 1),
                     }
    DEFAULT_REV = "0x0"

    def __init__(self):
        super(RaspberryPiCore, self).__init__()
        self.boardRev = self.DEFAULT_REV

        # Allow this class to be called directly.
        if BoardBase in self.__class__.__bases__:
            self._getBoardRevision()
            self._boardHook()

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
        except Exception as e:
            raise e

        self.model, self.memory, self.i2cPort = \
                    self.RPI_REVISIONS[self.boardRev]

    def _boardHook(self):
        """
        Sets up any board specific code like GPIO mappings, etc.
        """
        pass
