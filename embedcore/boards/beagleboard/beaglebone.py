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

    def __init__(self):
        super(BeagleBoneCore, self).__init__()

        # Allow this class to be called directly.
        if BoardBase in self.__class__.__bases__:
            self._getBoardRevision()
            self._boardHook()

    def _getBoardRevision(self):
        raise BeagleBoneException("Possibly not a BeagleBone.")

    def _boardHook(self):
        """
        Sets up any board specific code like GPIO mappings, etc.
        """
        pass
