#!/usr/bin/env python

import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *

from project_properties.ProjectPropertiesController \
        import ProjectPropertiesController
from recording_window.RecordingController import RecordingController

# TODO: Use the Global from sunra.config
from config import Config
from sunra.recording_db_proxy import  RecordingDBProxy
from sunra.recording_service_proxy import  RecordingServiceProxy

class SunraRecorder():
    """

    """
    def __init__(self):
        self.qt_app = QApplication(sys.argv)
        self.pp_controller = ProjectPropertiesController()

        rs_proxy = RecordingServiceProxy(Config())
        rdb_proxy = RecordingDBProxy(Config())
        self.rw_controller = RecordingController(rs_proxy, rdb_proxy)

        self.qt_app.connect(self.pp_controller,
                SIGNAL("ShowRecorder"), self.show_recorder)
        self.qt_app.connect(self.pp_controller,
                SIGNAL("Cancelled"), self.quit)
        self.qt_app.connect(self.pp_controller,
                SIGNAL("Cancelled"), self.quit)

    def start(self):
        self.pp_controller.show()
        self.qt_app.exec_()

    def show_recorder(self, model):
        """
        Responds to a ShowRecorder signal from the ProjectPropertiesController

        """
        self.rw_controller.show(model)

    def quit(self):
        quit()

if __name__ == '__main__':
    recording_app = SunraRecorder()
    recording_app.start()
