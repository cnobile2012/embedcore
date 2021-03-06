#!/usr/bin/env python
#
# beagleboard/tests.py
#
"""
Test BeagleBone board code.

Unit test for the BeagleBone board API.

by: Carl J. Nobile

email: carl.nobile@gmail.com
"""
__docformat__ = "restructuredtext en"


import unittest


from embedcore.boards.beagleboard import BeagleBoneException, BeagleBoneCore


NOT_BB = "Not a BeagleBone, therefore no tests will be run."

def testForThisBoard():
    bb = None

    try:
        bb = BeagleBoneCore()
    except BeagleBoneException:
        pass

    return bb


@unittest.skipUnless(testForThisBoard(), NOT_BB)
class TestBeagleBone(unittest.TestCase):
    """
    Tests for the BeagleBone board API.
    """

    def __init__(self, name):
        """
        :Parameters:
          name : str
            Unit test name.
        """
        super(TestBeagleBone, self).__init__(name)
        self._revision = None
        self._bb = None

    def setUp(self):
        self._revision = BeagleBoneCore.DEFAULT_REV
        self._bb = BeagleBoneCore()

    def tearDown(self):
        self._bb = None

    def test_getBoardRevision(self):
        try:
            self._revision = self._bb.getBoardRevision()
        except BeagleBoneException as e:
            self.assertRaises(e)

        models = [x for x, y, z in set(BeagleBoneCore.BB_REVISIONS.values())]
        #self.assertTrue(self._revision in BeagleBoneCore.BB_REVISIONS.values())
        self.assertTrue(self._revision in models)

    def test_getModel(self):
        model = self._bb.getModel()
        models = [x for x, y, z in set(BeagleBoneCore.BB_REVISIONS.values())]
        self.assertTrue(model in models)

    def test_getMaxMemory(self):
        memory = self._bb.getMaxMemory()
        memories = [y for x, y, z in set(BeagleBoneCore.BB_REVISIONS.values())]
        self.assertTrue(memory in memories)

    def test_getI2CPort(self):
        port = self._bb.getI2CPort()
        ports = [z for x, y, z in set(BeagleBoneCore.BB_REVISIONS.values())]
        self.assertTrue(port in ports)


if __name__ == '__main__':
    unittest.main()
