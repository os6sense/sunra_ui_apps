#!/usr/bin/env python

"""
File:: media_ui.py

"""
import sys

from PyQt4.QtGui import QApplication
from PyQt4.QtCore import SIGNAL

from sunra.config import Global, Uploader
from sunra.recording_db_proxy import RecordingDBProxy
from uploader_service_proxy import UploaderServiceProxy

from password_dialog.PasswordController import PasswordController
from media_dialog.MediaController import MediaController

class SunraMediaUI(object):
    """
        Provides a UI to allow for recordings to be either uploaded to the
        webserver or copied to USB.
    """
    def __init__(self):
        self.qt_app = QApplication(sys.argv)

        self.rdb_proxy = RecordingDBProxy(Global())

        self.uploader_proxy = UploaderServiceProxy(Uploader())

        self.media_controller = MediaController(self.rdb_proxy, Global())

        self.password_controller = PasswordController()

        self.qt_app.connect(self.password_controller,
                SIGNAL("CANCELLED"), self.quit)

        self.qt_app.connect(self.password_controller,
                SIGNAL("AUTHORISED"), self.show)

        self.qt_app.connect(self.media_controller,
                SIGNAL("MARKFORCOPY"), self.mark_for_copy)

        self.qt_app.connect(self.media_controller,
                SIGNAL("MARKFORUPLOAD"), self.mark_for_upload)

    def start(self):
        """ Start the main qt_app loop. """
#        self.password_controller.show()
        self.show()

        try:
            self.qt_app.exec_()
        except Exception, e:
            print e

    def quit(self):
        """ Quit the application."""
        quit()

    def show(self):
        """ Hide the password dialog and show the main UI."""
        self.password_controller.hide()
        self.media_controller.show()

    def unmark_all(self):
        """ Not Yet Implemented, unmark recording_formats """
        print "UNMARK"

    def _mark_for(self, recording_ids, selected_formats, method):
        """ DRY helper method that checks if a format has been selected and
            then calls the mark method if it has."""
        for recording_id in recording_ids:
            formats = self.rdb_proxy.formats(recording_id)
            del formats[-1] # strip pagination line
            for fmt in formats:
                if fmt['format'] in selected_formats:
                    method(fmt['id'], True)

    def  mark_for_copy(self, recording_ids, selected_formats):
        """ given a list of recording ids and another list containing strings
            for the formats (e.g. MP3, MP4) mark the recording_ids that are
            in the selected formats list for copying to a USB drive.

            e.g if recording_id 1 has a recording_format record for MP3,
                if the selected_formats list contains ["MP3"] the
                recording_format will be marked for copying.
        """
        self._mark_for(recording_ids, selected_formats,
                   self.rdb_proxy.mark_for_copy)

    def  mark_for_upload(self, recording_ids, selected_formats, immediate):
        """ given a list of recording ids and another list containing strings
            for the formats (e.g. MP3, MP4) mark the recording_ids that are
            in the selected formats list for uploading to the webserver.

            e.g if recording_id 1 has a recording_format record for MP3,
                if the selected_formats list contains ["MP3"] the
                recording_format will be marked for upload.
        """
        self._mark_for(recording_ids, selected_formats,
                   self.rdb_proxy.mark_for_upload)

        if immediate:
            # call the manual_upload method on the local recording service
            # to begin the upload immediately
            self.uploader_proxy.manual_start()

        self.media_controller.confirm_upload_marking(immediate)



if __name__ == '__main__':
    media_app = SunraMediaUI()
    media_app.start()
