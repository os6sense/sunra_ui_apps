

from PyQt4.QtGui import QDialog, QIcon, QTableWidgetItem, QMessageBox
from PyQt4.QtCore import pyqtSignature, QObject, QTimer, SIGNAL, Qt

from UI.CenterDialog import CenterDialog
from UI.password_dialog import Ui_Dialog

class PasswordDialog(QDialog, Ui_Dialog, CenterDialog):
  """
  """
  def __init__(self, parent=None):
      super(PasswordDialog, self).__init__(parent)
      self.setupUi(self)
      self.center()
      size =  self.geometry()
      self.setWindowFlags(Qt.WindowStaysOnTopHint)

  @pyqtSignature("")
  def on_cancelButton_clicked(self):
      self.close()

  @pyqtSignature("")
  def on_okButton_clicked(self):
      self.emit(SIGNAL("CHECKPASSWORD"), self.password.text())

  def display_error(self, msg):
      self.error_message.setText(msg)
