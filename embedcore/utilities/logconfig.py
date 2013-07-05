#
# utilities/logging.py
#
"""
This package setup basic logging.

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

    def __init__(self, level= logging.WARNING):
        self.__format = self.DEFAULT_LOG_FORMAT
        self.__level = level
        self.log = self.configLogging()

    def setLogFormat(self, format=None):
        """
        Set the format string.
        """
        self.__format = format

    def setLogLevel(self, level):
        """
        Set the logging level.
        """
        self.__level = level

    def configLogging(self):
        """
        Run the basicConfig and set the DEBUG level.
        """
        logging.basicConfig(format=self.__format)
        log = logging.getLogger()
        log.setLevel(self.__level)
        return log
