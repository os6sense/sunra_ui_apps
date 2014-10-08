
from PyQt4.QtGui import QDialog, QIcon, QTableWidgetItem, QMessageBox
from PyQt4.QtCore import pyqtSignature, QObject, QTimer, SIGNAL, Qt

from UI.CenterDialog import CenterDialog
from UI.AutoStopDialog import Ui_AutoStopDialog
from UI.SharedMessageDialog import SharedMessageDialog

from sunra.presenters import TimePresenter

class AutoStopDialog(QDialog, Ui_AutoStopDialog, SharedMessageDialog):
    def __init__(self, parent=None):
        super(AutoStopDialog, self).__init__(parent)
        self.setupUi(self)

        self.hide()
        self.extend_value = 5

        size = self.geometry()
        self.move((parent.width()-size.width())/2,
                (parent.height()-size.height())/2)

        self.setWindowFlags(Qt.WindowStaysOnTopHint)

    @pyqtSignature("")
    def on_extendButton_clicked(self):
        self.emit(SIGNAL("EXTENDBOOKING"), self.extend_value)

    @pyqtSignature("")
    def on_stopButton_clicked(self):
        self.emit(SIGNAL("STOPRECORDING"))

    @pyqtSignature("")
    def on_radioButton_1_clicked(self):
        self.extend_value = 5

    @pyqtSignature("")
    def on_radioButton_2_clicked(self):
        self.extend_value = 10

    @pyqtSignature("")
    def on_radioButton_3_clicked(self):
        self.extend_value = 20

    def set_end_time(self, time):
        self.end_time_label.setText(TimePresenter(time))

    def update_countdown(self, time):
        remaining = "%02d:%02d" % (time/60, time%60)
        self.countdown_label.setText(remaining)
