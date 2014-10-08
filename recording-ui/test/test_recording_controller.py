
# -*- coding: latin-1 -*-

import time
import unittest
from nose.tools import *
from config import Config
from recording_db_proxy import RecordingDBProxy, BookingDetail

def setup():
    pass

def teardown():
    pass

class RecordingControllerTest(unittest.TestCase):
    def setUp(self):
        """
        Create an instance of the proxy for reuse.
        """
        self.config = Config()
        self.rdb_proxy = RecordingDBProxy(self.config)

    def tearDown(self):
        """
        """
        pass

    def test_get_current_booking(self):
        """

        """
        try:
            uuid = self._create_project_helper()

            r = self.rdb_proxy.get_current_booking()
            assert len(r) == 0

            self._create_booking_helper(uuid, 
                    time.strftime("%H:%M:%S"), 
                    time.strftime("23:59:59") )

            r = self.rdb_proxy.get_current_booking()
            assert len(r) == 1

        finally:
            self.rdb_proxy.delete_project(uuid)



