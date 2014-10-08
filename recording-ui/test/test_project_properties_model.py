
# -*- coding: latin-1 -*-

import time
import unittest
import pytz
from dateutil.parser import parse
from datetime import datetime

from project_properties.ProjectPropertiesModel import ProjectPropertiesModel

def setup():
    pass

def teardown():
    pass

class RecordingControllerTest(unittest.TestCase):
    def setUp(self):
        """
        """
        self.ppm = ProjectPropertiesModel()

        self.uuid = 'abcdefghijklmnopqrstuvwxyz123',

        # Create a mock project
        self.project = {'uuid': self.uuid,
                   'project_name': 'mock project',
                   'client_name': 'mock client'
                   }

        self.start_time = u'2014-05-29T17:00:01+01:00' 
        self.end_time = u'2014-05-29T23:00:00+01:00'

        self.booking = {u'start_time': self.start_time,
                u'created_at': u'2014-05-29T16:15:52+01:00', 
                u'updated_at': u'2014-05-29T16:15:52+01:00', 
                u'availability_notes': None, 
                u'facility_studio': 2, 
                u'end_time': self.end_time,
                u'date': u'2014-05-29', 
                u'project_id': u'66174572f3ba12a82914a00fefb61c4e097a5cabb2711359285fdf4082665f1dadfe5aed', 
                u'id': 32}

    def tearDown(self):
        """
        """
        pass

    def test_empty_init(self):
        ppm = ProjectPropertiesModel()
        assert ppm != None

    def test_init_with_project(self):
        ppm = ProjectPropertiesModel(self.project)
        assert ppm != None
        assert ppm.uuid == self.uuid
        assert ppm.project_name == 'mock project'
        assert ppm.client_name == 'mock client'

    def test_current_time(self):
        pass

    def test_init_with_project_and_booking(self):
        ppm = ProjectPropertiesModel(self.project, self.booking)
        assert ppm != None
        assert ppm.uuid == self.uuid
        assert ppm.start_time == parse(self.start_time).replace(tzinfo=pytz.utc)
        assert ppm.end_time == parse(self.end_time).replace(tzinfo=pytz.utc)

    def test_start_time_with_utc(self):
        self.ppm.start_time = self.start_time
        assert self.ppm.start_time == parse(self.start_time).replace(tzinfo=pytz.utc)

    def test_start_time_without_utc(self):
        self.ppm.start_time = u'2014-05-29T17:00:01'
        assert self.ppm.start_time == parse(self.start_time).replace(tzinfo=pytz.utc)

    def test_end_time_with_utc(self):
        self.ppm.end_time = self.end_time
        assert self.ppm.end_time == parse(self.end_time).replace(tzinfo=pytz.utc)

    def test_end_time_without_utc(self):
        self.ppm.end_time = u'2014-05-29T23:00:00'
        assert self.ppm.end_time == parse(self.end_time).replace(tzinfo=pytz.utc)
 
    def test_date(self):
        pass

    def test_studio_id(self):
        pass

    def test_current_time(self):
        # How do I mock datetime?
        pass

    def test_booking_is_active(self):
        ppm = ProjectPropertiesModel(self.project, self.booking)

        # Check the mock is correct
        ppm.current_time = lambda: parse(u'2014-05-29T17:00:01').replace(tzinfo=pytz.utc)
        assert ppm.current_time() == parse(u'2014-05-29T17:00:01').replace(tzinfo=pytz.utc)
        assert ppm.current_time() == parse(u'2014-05-29T17:00:01+01:00').replace(tzinfo=pytz.utc)

        ppm.current_time = lambda: parse(u'2014-05-29T17:00:00').replace(tzinfo=pytz.utc)
        assert ppm.booking_is_active() == False
        ppm.current_time = lambda: parse(u'2014-05-29T17:00:02').replace(tzinfo=pytz.utc)
        assert ppm.booking_is_active() == True
        ppm.current_time = lambda: parse(u'2014-05-29T23:00:02').replace(tzinfo=pytz.utc)
        assert ppm.booking_is_active() == False

        ppm.current_time = lambda: parse(u'2014-05-29T17:00:00+01:00').replace(tzinfo=pytz.utc)
        assert ppm.booking_is_active() == False
        ppm.current_time = lambda: parse(u'2014-05-29T17:00:02+01:00').replace(tzinfo=pytz.utc)
        assert ppm.booking_is_active() == True
        ppm.current_time = lambda: parse(u'2014-05-29T23:00:02+01:00').replace(tzinfo=pytz.utc)
        assert ppm.booking_is_active() == False

        ppm.current_time = lambda: parse(u'2014-05-29T17:00:02+10:00').replace(tzinfo=pytz.utc)
        assert ppm.booking_is_active() == True

        ppm.current_time = lambda: parse(u'2014-05-29T17:00:02-10:00').replace(tzinfo=pytz.utc)
        assert ppm.booking_is_active() == True

    def test_verify(self):
        pass

    def test_create_project(self):
        pass

    def test_create_booking(self):
        pass

    #def test_example(self):
        #"""

        #"""
        #try:
            #uuid = self._create_project_helper()

            #r = self.rdb_proxy.get_current_booking()
            #assert len(r) == 0

            #self._create_booking_helper(uuid, 
                    #time.strftime("%H:%M:%S"), 
                    #time.strftime("23:59:59") )

            #r = self.rdb_proxy.get_current_booking()
            #assert len(r) == 1

        #finally:
            #self.rdb_proxy.delete_project(uuid)


def main():
        unittest.main()

if __name__ == '__main__':
        main()
