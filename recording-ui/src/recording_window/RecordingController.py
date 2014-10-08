# File:: recording_window.py

import pytz
from datetime import datetime

from PyQt4.QtGui import QMessageBox
from PyQt4.QtCore import pyqtSignature, Qt, QObject, QTimer, SIGNAL

from studio_light_controller import StudioLightController

from exit_dialog import ExitDialog
from recording_window.RecordingView import RecordingView
from autostop.AutoStopController import AutoStopController

def _(val):
    """
    Used for i18n
    """
    return val

class RecordingController(QObject):
    """
    Controls the recording view, responding the the UI signals.
    """
    def __init__(self, rs_proxy, rdb_proxy):
        super(RecordingController, self).__init__(None)

        self.proxy = rs_proxy
        self.rdb_proxy = rdb_proxy

        self._model = None
        self.status = None

        self.timer = QTimer()
        self.start_status_timer()

        # TODO: This should come from the config
        self.view = RecordingView("http://localhost:8090/livehq.flv")

        self.autostop = AutoStopController(self._model, parent=self.view)
        self.connect(self.autostop,
                SIGNAL("STOPRECORDING"), self.stop)
        self.connect(self.autostop,
                SIGNAL("EXTENDBOOKING"), self.extend_booking)
        self.connect(self.view,
                SIGNAL("RecordingButtonPressed"), self.change_recording_state)
        self.connect(self.view,
                SIGNAL("CloseEvent"), self.handle_close)

    def _get_model(self):
        """ get the model """
        return self._model
    def _set_model(self, value):
        """ set the model """
        self._model = value
        self.autostop.model = value

    model = property(_get_model, _set_model)

    def extend_booking(self, value=0):
        self._model.extend_booking(self.rdb_proxy, value)
        self.view.update_from_model(self._model)

    def start_status_timer(self):
        """
        Starts a timer which will call the update_status method every second
        in order to update the UI with details of the current recording
        status.
        """
        self.timer.timeout.connect(self.update_status)
        self.timer.start(1000)

    def show(self, model):
        """
        Sets to internal model to that passed in model, then displays the view.
        """
        self.model = model
        self.view.update_from_model(model)
        self.view.update_groups(self._get_groups())

        self.view.show()

    def booking_is_active(self):
        """
        Test if the booking is is scheduled for NOW and is valid for recording.
        """
        if self.model:
            return self.model.booking_is_active()

        return False

    def update_status(self):
        """
        Called from the timer. Gets the status via the proxy and updates the
        UI based on the results.
        """
        self.status = self.proxy.status()
        self.view.update_status(self.status)

        self.view.enable_ui(self.booking_is_active())

        if self.model:
            if self.model.end_time < datetime.now(pytz.utc):
                self.view.setWindowTitle(
                        "SESSION HAS ENDED, CANNOT ADD RECORDINGS.")
                self.view.set_recording_prompt("SESSION HAS ENDED")

            if self.model.start_time > datetime.now(pytz.utc):
                self.view.set_recording_prompt("SESSION HAS NOT YET STARTED.")
                self.view.setWindowTitle("SESSION HAS NOT YET STARTED.")

        # Recording State
        if self.status['is_recording']:
            self.view.set_ui_started()
        else:
            self.view.set_ui_stopped()
        self.autostop.status = self.status

        self.view.update_time(str(datetime.now()))

    def change_recording_state(self, skip_dialog=False):
        """
        Called in response to a RecordingButtonPressed signal from the UI
        """
        if self.status['is_recording']:
            prompt = QMessageBox.question(self.view, "Stop Recording?",
                    "Do you REALLY want to STOP the current recording?",
                    "Yes", "No",
                    "", 1, 0)

            if prompt == 1:
                return

            self.stop()
        else:
            self.start()

    def start(self):
        """
        Call the proxy to start recording.
        """
        self.proxy.start()

    def stop(self):
        """
        Call the proxys stop method to stop the recording, update the group
        list.
        """
        self.proxy.stop()
        self.view.update_groups(self._get_groups())

    def _get_groups(self):
        """
        Helper, return the list of recordings for the project from the
        proxy.
        """
        return self.rdb_proxy.recordings(self.model.uuid, self.model.booking_id)

    def handle_close(self, event):
        """ Message dialog asking do you really want to quit """

        quit_wt = _("Warning")

        quit_text = "You Cannot Exit The Application While Recording Is " \
                  "In Progress. Please Stop The Recording If You Wish To Exit"

        if self.status['is_recording']:
          QMessageBox.warning(self.view, quit_wt, quit_text)
          event.ignore()
          return

        exitDialog = ExitDialog(self.view)
        exitDialog.exec_()

        if exitDialog.EXITSTATUS == exitDialog.RETURNTORECORDING: # cancel
            event.ignore()
        elif exitDialog.EXITSTATUS == exitDialog.REALLYEXIT:  # really exit
            quit()
