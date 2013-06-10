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

from embedcore.boards import BoardException
from embedcore.boards.boardfactory import BoardFactory


class TestBoardFactory(unittest.TestCase):
    """
    Tests for the board factory.
    """
    

    def __init__(self, name):
        super(TestBoardFactory, self).__init__(name)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test__init__(self):
        try:
            bf = BoardFactory()
        except Exception as e:
            # This tests the condition where no boards are found.
            self.assertRaises(BoardException)
        else:
            # This tests that an implimented boards was found.
            self.assertNotEqual(bf, None)


if __name__ == '__main__':
    unittest.main()
