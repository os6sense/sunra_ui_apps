# -*- coding: latin-1 -*-

import time
import unittest
import pytz
from dateutil.parser import parse
from datetime import datetime

from project_properties.ProjectPropertiesModel import ProjectPropertiesModel
from autostop.AutoStopController import AutoStopController

import sys
from PyQt4.QtGui import QWidget, QApplication

from collections import defaultdict

class MockView(object):
    """
        VERY simple mock. Check the value of called['method_name']
        to examine how many times the method was called.
    """
    def __getattr__(self, name):
        def _missing(*args, **kwargs):
            self.called[name] += 1
        return _missing

    def __init__(self):
        self.called = defaultdict(int)

class AutoStopControllerTest(unittest.TestCase):
    def setUp(self):
        """
        """
        self.start_time = u'2014-05-29T17:00:01+01:00' 
        self.end_time = u'2014-05-29T23:00:00+01:00'

        self.model = ProjectPropertiesModel()

        self.model.current_time = parse(u'2014-05-29T17:54:55+01:00').\
                    replace(tzinfo=pytz.utc)
        self.model.start_time = parse(self.start_time).\
                    replace(tzinfo=pytz.utc)
        self.model.end_time = parse(self.end_time).\
                    replace(tzinfo=pytz.utc)

        self.view = MockView()

        self.uuid = 'abcdefghijklmnopqrstuvwxyz123',

        
        self.project = {'uuid': self.uuid,
                   'project_name': 'mock project',
                   'client_name': 'mock client'
                   }

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

    def test_init(self):
        controller = AutoStopController(self.model, self.view)
        assert controller != None
        assert controller.model == self.model
        assert controller.view == self.view

        # We can't test the live timer due to not having the appriate 
        # handle on a QApplicaiton. 
        assert controller.timer == None

    def test_check_time_no_warning(self):
        """
        Test that check_time does not attempt to show the dialog 
        if there is no need to do so. No need to do so is any period less than
        10 minutes before the  end of the booking (this may become configurable)
        """
        controller = AutoStopController(self.model, self.view)

        self.model.current_time = parse(u'2014-05-29T17:30:00+01:00').\
                    replace(tzinfo=pytz.utc)
        controller.check_time()

        self.model.current_time = parse(u'2014-05-29T10:30:00+01:00').\
                    replace(tzinfo=pytz.utc)
        controller.check_time()

        self.model.current_time = parse(u'2014-05-29T10:30:00+01:00').\
                    replace(tzinfo=pytz.utc)
        controller.check_time()

        assert self.view.called['show'] == 0
        assert self.view.called['hide'] == 0
        assert self.view.called['update_countdown'] == 0

    def test_check_time_with_warning(self):
        """
            Test that the warning dialog would be displayed if we are in the 
            period of 10 minutes before the booking is due to end.
        """
        controller = AutoStopController(self.model, self.view)

        self.model.current_time = parse(u'2014-05-29T22:55:00+01:00').\
                    replace(tzinfo=pytz.utc)
        controller.check_time()

        self.model.current_time = parse(u'2014-05-29T22:50:01+01:00').\
                    replace(tzinfo=pytz.utc)
        controller.check_time()

        self.model.current_time = parse(u'2014-05-29T22:59:59+01:00').\
                    replace(tzinfo=pytz.utc)
        controller.check_time()

        assert self.view.called['show'] == 3 
        assert self.view.called['hide'] == 0
        assert self.view.called['update_countdown'] == 3 

    def test_check_time_with_in_grace(self):
        """ Test that the dialog is still displayed within the grace period
        AFTER A BOOKING HAS ENDED. 
        """
        controller = AutoStopController(self.model, self.view)

        self.model.current_time = parse(u'2014-05-29T23:04:55+01:00').\
                    replace(tzinfo=pytz.utc)
        controller.check_time()

        assert self.view.called['show'] == 1
        assert self.view.called['hide'] == 0
        assert self.view.called['update_countdown'] == 1

    def test_check_time_after_grace(self):
        """ Test that the dialog is hidden after the grace period ends.
        """
        controller = AutoStopController(self.model, self.view)

        self.model.current_time = parse(u'2014-05-29T23:05:01+01:00').\
                    replace(tzinfo=pytz.utc)
        controller.check_time()

        assert self.view.called['hide'] == 1

def main():
        unittest.main()

if __name__ == '__main__':
        main()
