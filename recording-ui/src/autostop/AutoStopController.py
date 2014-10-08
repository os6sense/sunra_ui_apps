# File:: AutoStopController.py

from datetime import timedelta
from dateutil.parser import parse
from PyQt4.QtCore import Qt, QObject, QTimer, SIGNAL

from autostop.AutoStopView import AutoStopDialog

import pytz

def _(val):
    """
    Used for i18n
    """
    return val

class UIConfig(object):
    """ Config object - temporary """
    grace = 5 * 60
    start_countdown = 10 * 60

class AutoStopController(QObject):
    """
    Controls the recording view, responding the the UI signals.
    """
    def __init__(self, model, view=None, parent=None):
        super(AutoStopController, self).__init__(parent)
        self.model = model

        # Status is the information we have about the recoring state
        # it should be updated externally.
        self.status = None

        self.view = view
        if self.view == None:
            self.view = AutoStopDialog(parent)

        self.timer = None
        if parent != None:
            self.timer = QTimer()
            self.start_autostop_timer()

        self.view.connect(self.view,
                SIGNAL("EXTENDBOOKING"), self.extend_booking)

        self.view.connect(self.view,
                SIGNAL("STOPRECORDING"),
                self.stop_recording)

    def start_autostop_timer(self):
        """
        Starts a timer which will call the update_status method every second
        in order to update the UI with details of the current recording
        status.
        """
        self.timer.timeout.connect(self.check_time)
        self.timer.start(1000)

    # conditions under which stop recording should be sent
    # 1) current_time > end_time + grace
    # 2) stop_recording button has been pressed

    def check_time(self):
        """ Check if the booking will end within the timeperiod """
        if self.model == None:
            return

        if self.status != None: # Only show if a recording is in progress
            if not self.status['is_recording']:
                self.view.hide()
                return

        ct_delta = (self.model.end_time -
                self.model.current_time) + timedelta(0, UIConfig.grace)

        if ct_delta.total_seconds() <= 0:
            self.close_with_signal(SIGNAL("STOPRECORDING"))
            return

        #print self.model.current_time
        #print (self.model.end_time - timedelta(0, UIConfig.start_countdown))
        if self.model.current_time > \
                (self.model.end_time - timedelta(0, UIConfig.start_countdown)):
            self.view.set_end_time(self.model.end_time)
            self.view.show()
            self.view.update_countdown(ct_delta.total_seconds())

    def extend_booking(self, value):
        """ Confirm extension and if confirmed call close_with_signal """
        confirm = self.view.showQuestion("Extend Booking?",
                "You are about to extend this booking by %d minutes. "
                "Proceed?" % value)

        if confirm:
            # DO we want to prevent the dialog from being reshown
            # for a period of time? This causes problems under certain
            # conditions though. e.g. 1 minute remaining and they extend for
            # 5 minutes
            self.close_with_signal(SIGNAL("EXTENDBOOKING"), value)

    def stop_recording(self):
        """ signal call back, calls close with signal """
        self.close_with_signal(SIGNAL("STOPRECORDING"))

    def close_with_signal(self, signal, value = None):
        """
        Hide the view dialog, stop the timer and emit the signal
        passed in +signal+
        """
        self.view.hide()
        self.emit(signal, value)

if __name__ == "__main__":
    from PyQt4.QtGui import QWidget, QApplication
    class Model(object):
        """ Mock """
        pass

    class IntegrationTest(QWidget):
        """ Test the controller and view """
        def __init__(self, model):
            super(IntegrationTest, self).__init__()

            self.model = model
            model.current_time = parse(u'2014-05-29T17:54:55+01:00').\
                    replace(tzinfo=pytz.utc)
            model.start_time = parse(u'2014-05-29T17:00:00+01:00').\
                    replace(tzinfo=pytz.utc)
            model.end_time = parse(u'2014-05-29T18:00:00+01:00').\
                    replace(tzinfo=pytz.utc)

            view = AutoStopDialog(self)
            self.auto_stop = AutoStopController(model, view, parent=self)

            self.setWindowModality(Qt.WindowModal)

            self.setWindowTitle('Example')
            self.timer = QTimer()
            self.timer.timeout.connect(self.inc_time)
            self.timer.start(1000)
            self.show()

        def inc_time(self):
            """ Increment the mock timer """
            self.model.current_time = self.model.current_time + timedelta(0, 1)

    import sys
    APPLICATION = QApplication(sys.argv)
    EXAMPLE = IntegrationTest(Model())
    EXAMPLE.resize(640, 480)
    APPLICATION.exec_()
