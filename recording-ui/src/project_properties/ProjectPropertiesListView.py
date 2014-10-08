###############################################################################
# File:: ProjectPropertiesListView.py
#
# Notes :
# Contains the following classes :
#   ProjectPropertiesListView

###############################################################################


# TODO: Refactor out parse and datetime
import pytz
from dateutil.parser import parse
from datetime import datetime, timedelta

from PyQt4.QtGui import QDialog, QTableWidgetItem, QPushButton, QIcon
from PyQt4.QtCore import pyqtSignature, QObject, Qt, SIGNAL, QTime, QSize

from UI.CenterDialog import CenterDialog
from UI.ProjectProperties import Ui_ProjectProperties
from UI.ProjectListDialog import Ui_ProjectListDialog
from UI.SharedMessageDialog import SharedMessageDialog

from sunra.presenters import QTimePresenter, TimePresenter

def _(val):
    return val

###############################################################################
# ProjectPropertiesListView
###############################################################################
class ProjectPropertiesListView(QDialog, Ui_ProjectListDialog, CenterDialog, SharedMessageDialog):
    """
    This is a dialog which shows todays current and pending projects and
    allows the user to either select a project, OR if there is no project
    which is scheduled for recording *now*, to create a new project.
    """
    def __init__(self, parent=None):
        super(ProjectPropertiesListView, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.center()

    def add_item(self, row, col, text, centre=False):
        """
        Add a textual item to the table widget.

        Params::
        row -- row
        col -- col
        text -- text
        """
        item = QTableWidgetItem(str(text))
        if centre:
            item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        #item.setStyleSheet("{ margin-bottom: 10; }")
        self.tableWidget.setItem(row, col, item)

    def add_projects(self, projects):
        """
        Takes the list (actually a dict) of projects and displays
        them in the table

        TODO: Refactor tableWidget into a custom class to clean up the
        View.
        """
        row = -1

        self.tableWidget.clear()

        self.tableWidget.setHorizontalHeaderLabels([_("Project Name"),
            _("Client Name"), _("Start Time"), _("End Time"), _("# Use")])

        for ind, width in enumerate([150, 150, 85, 85, 150]):
            self.tableWidget.setColumnWidth(ind, width)

        for project in projects:
            for booking in project['bookings']:
                # ~~Don't display bookings which have already finished.~~
                if parse(booking['end_time']) < datetime.now(pytz.utc):
                    continue

                row += 1
                self.tableWidget.setRowCount(row+1)

                self.add_item(row, 0, project['project_name'])
                self.add_item(row, 1, project['client_name'])

                self.add_item(row, 2,
                        TimePresenter(booking['start_time']), True)
                self.add_item(row, 3,
                        TimePresenter(booking['end_time']), True)

                button = QPushButton("Select Project", self.tableWidget)

                button.setIcon(QIcon('images/media-record.png'))
                button.setIconSize(QSize(24, 24))
                button.setStyleSheet("outline: none;")
                button.clicked.connect(lambda fa, p=project, b=booking:
                        self.use_project(p, b))

                self.tableWidget.setCellWidget(row, 4, button)

                # Highlight & Select the current row if its scheduled
                # for now. Also disables the create project button if
                # there is a scheduled booking.
                self.hs_current(row, booking)

    def hs_current(self, row, booking):
        """
        Highlight & Select the current row if its scheduled
        for now. Also disables the create project button if
        there is a scheduled booking.
        """

        r_txt=_("There is a project scheduled for recording NOW. If you wish "\
                "to add to this recording, click the 'SELECT PROJECT' Button "\
                "above.")

        if datetime.now(pytz.utc) > parse(booking['start_time']):
            if datetime.now(pytz.utc) < parse(booking['end_time']):
                self.tableWidget.selectRow(row)
                self.tableWidget.cellWidget(row, 4).setFocus()

                # Because there is a current project scheduled we cant
                # create a new project.
                self.create_project_button.setEnabled(False)

                self.help_red.setStyleSheet("color: pink")
                self.help_red.setText(r_txt)

    def use_project(self, project, booking):
        """
        Connected to the dynamic buttons for project selection. Emits a
        ProjectSelected signal with the relevant project and booking detail.
        """
        self.emit(SIGNAL("ProjectSelected"), (project, booking))

                # What the hell am I doing creating a model in the view?
                # Grrrrrrr!
                # ProjectPropertiesModel(project, booking))

    @pyqtSignature("")
    def on_create_project_button_clicked(self):
        """
        Show the empty form view.
        """
        self.emit(SIGNAL("NewProject"))

    @pyqtSignature("")
    def on_cancelButton_clicked(self):
        """
        Respondes a click from the canel button and emits a cancelled signal.
        """
        self.emit(SIGNAL("Cancelled"))

