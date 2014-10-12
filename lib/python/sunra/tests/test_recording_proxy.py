
# -*- coding: latin-1 -*-

import time
import unittest
from nose.tools import *
from sunra.config import Global
from sunra.recording_proxy import RecordingDBProxy, BookingDetail

def setup():
    pass

def teardown():
    pass

class DBproxyTest(unittest.TestCase):
    def setUp(self):
        """
        Create an instance of the proxy for reuse.
        """
        self.config = Global()
        self.rdb_proxy = RecordingDBProxy(self.config)
        self.client_name = "test_client_from_py"
        self.project_name = "test_project_from_py"

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

            assert len(r) == 0, "Bookings found when no bookings expected"

            self._create_booking_helper(uuid, 
                    time.strftime("%H:%M:%S"), 
                    time.strftime("23:59:59") )

            r = self.rdb_proxy.get_current_booking()
            assert len(r) == 1
        finally:
            self.rdb_proxy.delete_project(uuid)

    def test_find_projects(self):
        try:
            uuid = self._create_project_helper()
            r = self.rdb_proxy.find_projects("garbage", "klfejwkl")
            assert len(r) == 0, "Project found when no project expected"

            r = self.rdb_proxy.find_projects(self.client_name, self.project_name)
            assert len(r) == 1, "No Project Found When 1 Expected"
            assert r[0]['uuid']== uuid, "UUID of found project does not match"
        finally:
            self.rdb_proxy.delete_project(uuid)


    def test_get_todays_bookings(self):
        """
        ensure that we can list todays bookings.
        """
        try:
            uuid = self._create_project_helper()
            self._create_booking_helper(uuid,
                    time.strftime("%H:%M:%S"),
                    time.strftime("23:%M:%S"))

            assert self.rdb_proxy.get_todays_bookings().count > 1
        finally:
            self.rdb_proxy.delete_project(uuid)


    def test_create_project(self):
        """
        Test that we can create a project.
        """
        try:
            uuid = self._create_project_helper()
            assert uuid > 0

            self.rdb_proxy.delete_project(uuid)
        finally:
            self.rdb_proxy.delete_project(uuid)

    def test_create_booking(self):
        try:
            uuid = self._create_project_helper()
            assert uuid > 0

            booking_id = self._create_booking_helper(uuid,
                    time.strftime("%H:%M:%S"),
                    time.strftime("23:%M:%S"))

            assert booking_id > 0
        finally:
            self.rdb_proxy.delete_project(uuid)


    def test_recordings(self):
        pass

    def test_bookings(self):
        try:
            bookings = self.rdb_proxy.bookings()
            assert bookings.count > 0
            assert len(bookings[-1]['pagination']) > 0
        finally:
            pass

    def test_mark_for_upload(self):
        self.rdb_proxy.mark_for_upload(1, True)

    def test_mark_for_copy(self):
        self.rdb_proxy.mark_for_copy(1, True)

    def test_mark_for_encryption(self):
        self.rdb_proxy.mark_for_encryption(1, True)

    def test_mark_encrypted(self):
        self.rdb_proxy.mark_encrypted(1, True)

    def test_mark_fixed(self):
        self.rdb_proxy.mark_fixed(1, True)

    def _create_project_helper(self):
        """
        Helper to DRY up the tests. Creates a project with a generic name
        for client and project.
        """

        uuid, errors = self.rdb_proxy.create_project(
                self.client_name, self.project_name)
        return uuid

    def _create_booking_helper(self, uuid, start_time, end_time):
        bd = BookingDetail(
                time.strftime("%d/%m/%Y"), 
                start_time,
                end_time,
                self.config.studio_id
        )

        return self.rdb_proxy.create_booking(uuid, bd)


