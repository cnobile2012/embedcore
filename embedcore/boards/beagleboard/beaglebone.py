#
# boards/beagleboard/beaglebone.py
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
    __REV_REGEX = re.compile(r'.*ARMv7.*(?P<rev>rev 2) \(v7l\).*')
    BB_REVISIONS = {'rev 2': ('A5C', 512, 0)}
    DEFAULT_REV = "A5C"

    def __init__(self):
        super(BeagleBoneCore, self).__init__()
        self.boardRev = self.DEFAULT_REV

        # Allow this class to be called directly.
        if BoardBase in self.__class__.__bases__:
            self._getBoardRevision()
            self._boardHook()

    def _getBoardRevision(self):
        """
        Gets the version number of the BeagleBone board. We only check for the
        CPU type and make the assumption this is correct.
        *** TODO *** Fix this
        """
        try:
            with open('/proc/cpuinfo', 'r') as f:
                m = self.__REV_REGEX.search(''.join(f.readlines()))

                if m is None:
                    raise BeagleBoneException("Possibly not a BeagleBone.")
        except Exception as e:
            raise e

        self.model, self.memory, self.i2cPort = \
                       self.BB_REVISIONS[m.group('rev')]
        self.boardRev = self.model

    def _boardHook(self):
        """
        Sets up any board specific code like GPIO mappings, etc.
        """
        pass
