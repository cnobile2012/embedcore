#!/usr/bin/env python
#
# boards/tests.py
#
"""
Test board factory code.

Unit test for the board factory code.

by: Carl J. Nobile

email: carl.nobile@gmail.com
"""
__docformat__ = "restructuredtext en"


import unittest

from embedcore.boards.boardsfactory import BoardFactory


class TestBoardFactory(unittest.TestCase):
    """
    Tests for the board factory.
    """

    def __init__(self, name):
        super(TestBoardFactory, self).__init__(name)
        self._bf = None

    def setUp(self):
        self._bf = BoardFactory()

    def tearDown(self):
        self._bf = None





if __name__ == '__main__':
    unittest.main()
