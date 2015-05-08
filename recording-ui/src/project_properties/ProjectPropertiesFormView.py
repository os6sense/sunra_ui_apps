###############################################################################
# File:: ProjectPropertiesFormView.py
#
# Notes :
# Contains the following classes :
#   ProjectPropertiesFormView

###############################################################################

# TODO: Refactor out parse and datetime
import pytz
from dateutil.parser import parse
from datetime import datetime, timedelta

from PyQt4.QtGui import QDialog, QTableWidgetItem, QPushButton
from PyQt4.QtCore import pyqtSignature, QObject, Qt, SIGNAL, QTime, QSize

from UI.CenterDialog import CenterDialog
from UI.ProjectProperties import Ui_ProjectProperties
from UI.ProjectListDialog import Ui_ProjectListDialog
from UI.SharedMessageDialog import SharedMessageDialog

from sunra.presenters import QTimePresenter, TimePresenter



from timepicker.TimePickerController import TimePickerController

from i18n.translate import _

###############################################################################
# ProjectPropertiesFormView
###############################################################################
class ProjectPropertiesFormView(QDialog, Ui_ProjectProperties, CenterDialog, SharedMessageDialog):
    """
    This is the main form view for creating new projects and as such is
    a simple dialog window which accepts client and project names,
    and a start and end time for a booking.
    """
    def __init__(self, parent=None):
        super(ProjectPropertiesFormView, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.center()

        self.leClientName.setFocus()

        self.start_time_picker = TimePickerController(None, parent=self)
        self.start_time_picker.connect(self.start_time_picker,
                SIGNAL("SET_TIME"), self.on_start_time_changed)

        self.end_time_picker = TimePickerController(None, parent=self)
        self.end_time_picker.connect(self.end_time_picker,
                SIGNAL("SET_TIME"), self.on_end_time_changed)

        self.start_time_picker.connect(self.start_time_picker,
                SIGNAL("CANCEL"), self.on_time_cancelled)

        self.end_time_picker.connect(self.end_time_picker,
                SIGNAL("CANCEL"), self.on_time_cancelled)

    # projectName
    def _pn_get(self):
        """ get ProjectName."""
        return str(self.leProjectTitle.text())
    def _pn_set(self, value):
        """ set projectName """
        self.leProjectTitle.setText(str(value))
    project_title = property(_pn_get, _pn_set)

    # clientName
    def _cn_set(self, value):
        """ set clientName """
        self.leClientName.setText(str(value))
    def _cn_get(self):
        """ get clientName """
        return str(self.leClientName.text())
    client_name = property(_cn_get, _cn_set)

    # startTime
    def _st_set(self, value):
        """ set startTime """
        self.start_time.setTime(QTimePresenter(value))
    def _st_get(self):
        """ get startTime """
        self.start_time.setDate(datetime.now())
        return self.start_time.dateTime().toPyDateTime()

    startTime = property(_st_get, _st_set)

    #endTime
    def _et_set(self, value):
        """ set endTime """
        self.end_time.setTime(QTimePresenter(value))
    def _et_get(self):
        """ get endTime """
        self.end_time.setDate(datetime.now())
        return self.end_time.dateTime().toPyDateTime()
    endTime = property(_et_get, _et_set)

    def show(self):
        """
        Show the form
        """
        super(ProjectPropertiesFormView, self).show()

    def update_view(self, model):
        """
        Update the view based upon the supplied model.
        """
        self.project_title = model.project_name
        self.client_name = model.client_name
        self.startTime = model.start_time
        self.endTime = model.end_time

    def on_set_start_time_clicked(self):
        self.start_time_picker.show()
        self.cancelButton.hide()
        self.create_project_button.hide()

    def on_time_cancelled(self):
        self.cancelButton.show()
        self.create_project_button.show()

    def on_set_end_time_clicked(self):
        self.end_time_picker.show()
        self.cancelButton.hide()
        self.create_project_button.hide()

    @pyqtSignature("")
    def on_create_project_button_clicked(self):
        """
        emit a signal .
        """
        self.emit(SIGNAL("CreateProject"))

    @pyqtSignature("")
    def on_cancelButton_clicked(self):
        """
        Respondes a click from the canel button and emits a cancelled signal.
        """
        self.emit(SIGNAL("Cancelled"))

    def on_start_time_changed(self, time):
        py_time = parse(time)
        if py_time > self.endTime:
            self.start_time.setTime(self.end_time.time())
        else:
            self.startTime = QTime(py_time.hour, py_time.minute)

    def on_end_time_changed(self, time):
        py_time = parse(time)
        if py_time < self.startTime:
            self.end_time.setTime(self.start_time.time())
        else:
            self.endTime = QTime(py_time.hour, py_time.minute)

