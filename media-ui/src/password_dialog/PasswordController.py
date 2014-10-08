from time import sleep
from PyQt4.QtCore import pyqtSignature, QObject, Qt, SIGNAL, QTime, QSize
from PyQt4.QtGui import QIcon

from sunra.config import Global
from sunra.recording_db_proxy import RecordingDBProxy

from .PasswordDialog import PasswordDialog
from .Password import Password

def _(val):
    return val

###############################################################################
###############################################################################
class PasswordController(QObject):
    """
    Controller for the project properties dialog interaction.
    Based on the presence of exisiting projects (projects being returned
    via the RecordingDBProxy), the form controller will chose to display
    either the list view or the form view.

    Once a valid project has either been selected or created the controller
    will emit a ShowRecorder signal.
    """
    def __init__(self):
        super(PasswordController, self).__init__(None)

        self.config = Global()
        self.rdb_proxy = RecordingDBProxy(self.config)

        self.password_view = PasswordDialog()

        self.password_view.connect(self.password_view,
                SIGNAL("CHECKPASSWORD"), self.check_password)

    def show(self):
        """
        """
        self.password_view.show()

    def hide(self):
        self.password_view.hide()

    def check_password(self, password):
        if Password.check_password(str(password), self.config.ui_hash):
            self.emit(SIGNAL("AUTHORISED"))
        else:
            # BUG - cant update  multiple times
            msg = "Bad Password! You may not pass."
            self.password_view.display_error(msg)
