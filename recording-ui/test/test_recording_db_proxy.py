
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

class DBproxyTest(unittest.TestCase):
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

    #def test_delete(self):
        #pass

    #def test_get_todays_bookings(self):
        #r = self.rdb_proxy.get_todays_bookings()
        #assert r.count > 1


    def test_create_project(self):
        """
        Test that we can create a project.
        """
        uuid = self._create_project_helper()

        assert uuid > 0
        self.rdb_proxy.delete_project(uuid)

    def test_create_booking(self):
        uuid = self._create_project_helper()
        assert uuid > 0

        booking_id = self._create_booking_helper(uuid, 
                time.strftime("%H:%M:%S"), 
                time.strftime("23:%M:%S") )

        assert booking_id > 0
        self.rdb_proxy.delete_project(uuid)

    def _create_project_helper(self):
        """
        Helper to DRY up the tests. Creates a project with a generic name
        for client and project.
        """
        client_name = "test_client_from_py"
        project_name = "test_project_from_py"
        return self.rdb_proxy.create_project(client_name, project_name)

    def _create_booking_helper(self, uuid, start_time, end_time):
        bd = BookingDetail(
                time.strftime("%d/%m/%Y"), 
                start_time,
                end_time,
                self.config.studio_id
        )

        return self.rdb_proxy.create_booking(uuid, bd)


