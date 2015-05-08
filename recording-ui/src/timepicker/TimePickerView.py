# File:: TimePickerView.py
""" A Simple TimePicker Dialog to set the start and end times of groups """

from PyQt4.QtGui import QDialog, QIcon
from PyQt4.QtCore import pyqtSignature, QObject, SIGNAL, Qt

#from UI.CenterDialog import CenterDialog
from UI.TimePickerDialog import Ui_TimePickerDialog
from UI.SharedMessageDialog import SharedMessageDialog

#from sunra.presenters import TimePresener

class TimePickerDialog(QDialog, Ui_TimePickerDialog, SharedMessageDialog):
    """ A Simple TimePicker Dialog to set the start and end times of groups """

    BG_COLOR = "rgb(84, 84, 84)"

    def __init__(self, parent=None):
        super(TimePickerDialog, self).__init__(parent)
        self.setupUi(self)

        self.meridian = ''

        self.hour = ''
        self.minute = ''

        size = self.geometry()
        self.move((parent.width()-size.width())/2,
                (parent.height()-size.height())/2)

        self.setWindowFlags(Qt.WindowStaysOnTopHint)

        self.hour_button_loop(lambda fn, i: self.enable_button(fn, False))
        self.enable_minute_buttons(False)

        self.enable_button(self.ok_button, False)

    def on_ok_button_clicked(self):
        self.emit(SIGNAL("SET_TIME"))

    def on_cancel_button_clicked(self):
        self.emit(SIGNAL("CANCEL"))

    def on_am_button_clicked(self):
        """ Respond to a clicked event for the PM button """
        self.select_am_pm(self.am_button, self.pm_button, "AM")

    def on_pm_button_clicked(self):
        """ Respond to a clicked event for the AM button """
        self.select_am_pm(self.pm_button, self.am_button, "PM")

    def on_hour_button_01_clicked(self):
        self.hour_button_clicked(self.hour_button_01)

    def on_hour_button_02_clicked(self):
        self.hour_button_clicked(self.hour_button_02)

    def on_hour_button_03_clicked(self):
        self.hour_button_clicked(self.hour_button_03)
   
    def on_hour_button_04_clicked(self):
        self.hour_button_clicked(self.hour_button_04)

    def on_hour_button_05_clicked(self):
        self.hour_button_clicked(self.hour_button_05)

    def on_hour_button_06_clicked(self):
        self.hour_button_clicked(self.hour_button_06)

    def on_hour_button_07_clicked(self):
        self.hour_button_clicked(self.hour_button_07)

    def on_hour_button_08_clicked(self):
        self.hour_button_clicked(self.hour_button_08)

    def on_hour_button_09_clicked(self):
        self.hour_button_clicked(self.hour_button_09)

    def on_hour_button_10_clicked(self):
        self.hour_button_clicked(self.hour_button_10)

    def on_hour_button_11_clicked(self):
        self.hour_button_clicked(self.hour_button_11)

    def on_hour_button_12_clicked(self):
        self.hour_button_clicked(self.hour_button_12)

    def on_minute_button_00_clicked(self):
        self.minute_button_clicked(self.minute_button_00)

    def on_minute_button_15_clicked(self):
        self.minute_button_clicked(self.minute_button_15)

    def on_minute_button_30_clicked(self):
        self.minute_button_clicked(self.minute_button_30)

    def on_minute_button_45_clicked(self):
        self.minute_button_clicked(self.minute_button_45)

    def minute_button_clicked(self, btn):
        self.unselect_button(self.minute_button_00)
        self.unselect_button(self.minute_button_15)
        self.unselect_button(self.minute_button_30)
        self.unselect_button(self.minute_button_45)
        self.set_button_selected(btn)
        self.minute = str(btn.text())
        self.enable_ok_button(True)

    def enable_ok_button(self, b_val):
        self.enable_button(self.ok_button, b_val)

    def select_am_pm(self, on_btn, off_btn, meridian_label):
        self.set_am_or_pm_button_selected(on_btn, off_btn)
        self.set_am_pm_labels(meridian_label)
        self.enable_hour_buttons(True)
        self.meridian = meridian_label
        self.select_hour(self.hour)
        self.select_minute(self.minute)

    def select_hour(self, hour):
        """ Select whichever hour button was last selected """
        if hour != '':
            btn = getattr(self, "hour_button_" + 
                    ('0' if hour[0] != '0' and int(hour) < 10 else '') + hour)
            self.set_button_selected(btn)

    def select_minute(self, minute):
        """ Select whichever minute button was last selected """
        if minute != '':
            btn = getattr(self, "minute_button_" + minute)
            self.set_button_selected(btn)

    def hour_button_clicked(self, btn):
        """ Functions applicable if _any_ hour button is clicked. """
        self.hour_button_loop(lambda fn, i: self.unselect_button(fn))
        self.set_button_selected(btn)
        self.set_button_selected(self.minute_button_00)
        self.enable_minute_buttons(True)
        self.hour = str(btn.text())
        self.select_minute(self.minute)

    def enable_hour_buttons(self, b_val):
        """ Enable or disable hour buttons """
        enable = lambda fn, i: self.enable_button(fn, b_val)
        self.hour_button_loop(enable)

    def enable_minute_buttons(self, b_val):
        """ Enable or disable the buttons for specifying the minutes """
        self.enable_button(self.minute_button_00, b_val)
        self.enable_button(self.minute_button_15, b_val)
        self.enable_button(self.minute_button_30, b_val)
        self.enable_button(self.minute_button_45, b_val)

    def enable_button(self, fn, b_val):
        """ Enable or disable a button. An enabled button has its enabled
            property set to True, its Flast property set to False, and
            its stylesheet colors changed to make it visable. A disabled button
            is the opposite.
        """
        fn.setEnabled(b_val)
        fn.setFlat(not b_val)

        if b_val:
            fn.setStyleSheet("background: {0}; \
                              color: white;".format(self.BG_COLOR))
        else:
            fn.setStyleSheet("background-color: {0}; \
                              color: {0};".format(self.BG_COLOR))

    def set_am_or_pm_button_selected(self, btn, unsel_btn):
        self.set_button_selected(btn)
        self.unselect_button(unsel_btn)

    def set_button_selected(self, btn):
        btn.setStyleSheet("background-color: white; color: black;")

    def unselect_button(self, btn):
        btn.setStyleSheet("background: rgb(84, 84, 84); color: white;")

    def hour_button_loop(self, l):
        """ Take a lambda and call it with each hour button and the integer value """
        for i in range(1, 13):
            f_name = 'hour_button_' + ('0' if i < 10 else '') + str(i)
            l(getattr(self, f_name), i)

    def set_am_pm_labels(self, t):
        l = lambda fn, i: fn.setText(('0' if t == "AM" and i < 10 else '') + str(i))
        self.hour_button_loop(l)
        self.hour_button_12.setText('00' if t == "AM" else '12')

