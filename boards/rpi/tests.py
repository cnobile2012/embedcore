#!/usr/bin/env python
#
# rpi/tests.py
#
"""
Test Raspberry Pi board code.

Unit test for the Raspberry Pi board API.

by: Carl J. Nobile

email: carl.nobile@gmail.com
"""
__docformat__ = "restructuredtext en"


import unittest


from boards.rpi import RaspberryPiException, RaspberryPiCore


class TestRaspberryPi(unittest.TestCase):
    """
    Tests for the Raspberry Pi board API.
    """
    #versions = RaspberryPiCore.REVISIONS.keys()

    def __init__(self, name):
        """
        :Parameters:
          name : str
            Unit test name.
        """
        super(TestRaspberryPi, self).__init__(name)
        self._revision = None
        self._rpc = None

    def setUp(self):
        self._revision = RaspberryPiCore.DEFAULT_REV
        self._rpc = RaspberryPiCore()

    def tearDown(self):
        self._rpc = None

    def test_getBoardRevision(self):
        try:
            self._revision = self._rpc.getBoardRevision()
        except RaspberryPiException, e:
            self.assertRaises(e)

        self.assertTrue(self._revision in RaspberryPiCore.RPI_REVISIONS.keys())

    def test_getModel(self):
        model = self._rpc.getModel()
        models = [x for x, y, z in set(RaspberryPiCore.RPI_REVISIONS.values())]
        self.assertTrue(model in models)

    def test_getMaxMemory(self):
        memory = self._rpc.getMaxMemory()
        memories = [y for x, y, z in set(
            RaspberryPiCore.RPI_REVISIONS.values())]
        self.assertTrue(memory in memories)

    def test_getI2CPort(self):
        port = self._rpc.getI2CPort()
        ports = [z for x, y, z in set(RaspberryPiCore.RPI_REVISIONS.values())]
        self.assertTrue(port in ports)

if __name__ == '__main__':
    unittest.main()
