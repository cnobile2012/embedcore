#
# boards/boardfactory.py
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
Generates the correct base class depending on the board that is plugged in.

by: Carl J. Nobile

email: carl.nobile@gmail.com
"""
__docformat__ = "restructuredtext en"


import sys, traceback
from embedcore.boards import BoardException
from embedcore.boards.rpi import RaspberryPiCore
from embedcore.boards.beagleboard import BeagleBoneCore


# mro: BoardFactory -> RaspberryPiCore -> BeagleBoneCore -> BoardBase -> object
class BoardFactory(RaspberryPiCore, BeagleBoneCore):
    """
    This class determines which board is in use. It runs the __init__ method
    from all subclasses till one succeeds.
    """

    def __init__(self):
        for klass in self.__class__.__bases__:
            try:
                klass.__init__(self)
                klass._getBoardRevision(self)
                klass._boardHook(self)
            except BoardException as e:
                # Look for an exception on a specific board then loop to test
                # the next board. If all boards raise an exception the loop
                # will fall through and a general BoardException will be raised.
                continue
            else:
                break

            msg = "None of the implemented boards were detected."
            raise BoardException(msg)
