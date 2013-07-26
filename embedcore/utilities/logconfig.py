#
# utilities/logconfig.py
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
This package sets up basic logging.

by: Carl J. Nobile

email: carl.nobile@gmail.com
"""
__docformat__ = "restructuredtext en"


import logging


class LoggingConfig(object):
    """
    This class sets up basic logging.

    This class can be overridden and redefine the configLogging method to
    setup a different logger.
    """
    DEFAULT_LOG_FORMAT = ("%(asctime)s %(module)s %(funcName)s "
                          "[line:%(lineno)d] %(levelname)s %(message)s")

    def __init__(self, level=logging.WARNING):
        """
        Sets the default log format and level, then creates the logger.
        """
        self.__format = self.DEFAULT_LOG_FORMAT
        self.__level = level
        self.log = self.configLogging()

    def setLogFormat(self, format=None):
        """
        Set the format string.

        :Parameters:
          format: `str`
            A string compliant with the logging package used to format the
            message.
        """
        self.__format = format

    def setLogLevel(self, level):
        """
        Set the logging level.

        :Parameters:
          level: `int`
            An integer indicating the level the logger should run at.
        """
        self.__level = level

    def configLogging(self):
        """
        Run the basicConfig and set the DEBUG level.

        Returns:
          The logger object.
        """
        logging.basicConfig(format=self.__format)
        log = logging.getLogger()
        log.setLevel(self.__level)
        return log
