# File:: TimePickerController.py

from datetime import timedelta
from dateutil.parser import parse
from PyQt4.QtCore import Qt, QObject, QTimer, SIGNAL

from timepicker.TimePickerView import TimePickerDialog

import pytz

def _(val):
    """
    Used for i18n
    """
    return val

class TimePickerController(QObject):
    """
    Controls the timepicker view, responding the the UI signals.
    """
    def __init__(self, model, view=None, parent=None):
        super(TimePickerController, self).__init__(parent)

        self.model = model
        self.view = view

        if self.view == None:
            self.view = TimePickerDialog(parent)

        self.view.connect(self.view, 
                          SIGNAL("SET_TIME"), 
                          self.time_selected_event)

        self.view.connect(self.view, SIGNAL("CANCEL"), self.close) 
        self.view.hide()

    def time_selected_event(self):
        self.close_with_signal(SIGNAL("SET_TIME"), self.time)

    @property
    def time(self):
        if self.view.meridian == "PM":
            i_hour = int(self.hour)
            if i_hour < 12:
                i_hour += 12

            return str(i_hour) + ":" + self.minute
        else:
            return self.hour + ":" + self.minute

    @time.setter
    def time(self, value):
        self.hour = parse(value).hour
        self.minute = parse(value).minute

        # This should happen in the view when time is set
        self.view.enable_hour_buttons(True)
        self.view.enable_minute_buttons(True)
        self.view.select_hour(self.view.hour)
        self.view.select_minute(self.view.minute)
        self.view.enable_ok_button(True)

    @property
    def hour(self):
        return self.view.hour

    @hour.setter
    def hour(self, value):
        if value > 12:
            value -= 12
            self.view.meridian = "PM"
        else:
            self.view.meridian = "AM"

        self.view.hour = str(value)

    @property
    def minute(self):
        return self.view.minute

    @minute.setter
    def minute(self, value):
        self.view.minute = str(value)

    def show(self):
        self.view.show()

    def close(self):
        self.view.hide()

    def close_with_signal(self, signal, value = None):
        """
        Hide the view dialog, stop the timer and emit the signal
        passed in +signal+
        """
        self.close()
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
            view = TimePickerDialog(self)
            self.time_picker = TimePickerController(model, view, parent=self)
            self.setWindowModality(Qt.WindowModal)

            self.setWindowTitle('Example')
            view.show()
            self.show()

            self.time_picker.time = "04:15"

    import sys
    APPLICATION = QApplication(sys.argv)
    EXAMPLE = IntegrationTest(Model())
    EXAMPLE.resize(1024, 480)
    APPLICATION.exec_()
