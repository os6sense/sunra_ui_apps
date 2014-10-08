from PyQt4.QtGui import *
from PyQt4.QtCore import *

class CenterDialog() :
    """
    Simple class to center a dialog, not to be created directly.
    Inherit from it and call self.center() to center a dialog
    """
    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)
