

from PyQt4.QtGui import QDialog, QIcon, QTableWidgetItem, QMessageBox
from PyQt4.QtCore import pyqtSignature, QObject, QTimer, SIGNAL, Qt
from UI.CenterDialog import CenterDialog
from UI.ReallyExit import Ui_ExitDialog

class ExitDialog(QDialog, Ui_ExitDialog):
  """
    Really Exit - A minor window class to make it more explicit as
    to what is going on when the user wishes to exit.
        """
  REALLYEXIT = 0
  RETURNTORECORDING = 1

  EXITSTATUS = 0

  def __init__(self, parent=None):
    super(ExitDialog, self).__init__(parent)
    self.setupUi(self)
#    self.center()
    size =  self.geometry()
    self.move((parent.width()-size.width())/2, (parent.height()-size.height())/2)
    self.setWindowFlags(Qt.WindowStaysOnTopHint)

  @pyqtSignature("")
  def on_returnButton_clicked(self):
    # note - will trigger closeEvent
    self.EXITSTATUS = self.RETURNTORECORDING
    self.close()

  @pyqtSignature("")
  def on_exitButton_clicked(self):
    # note - will trigger closeEvent
    self.EXITSTATUS = self.REALLYEXIT
    self.close()

