from PyQt4.QtGui import QMessageBox
#from PyQt4.QtCore import *

import itertools as IT
import collections

class SharedMessageDialog() :
    """
        Prototype for a shared message dialog system
    """
    def showError(self, title, message):
        QMessageBox.critical(self, title, message)

    # Helper, dry up
    def showErrors(self, title, errors):
        errors = self.flatten(errors)
        errors = "\n".join(errors)
        self.showError(title, errors)

    # Helper    
    def flatten(self, l):
        for el in l:
            if isinstance(el, collections.Iterable) and not isinstance(el, basestring):
                for sub in self.flatten(el):
                    yield sub
            else:
                yield el

    def showWarning(self, title, message):
        QMessageBox.warning(self, title, message)

    def showInfo(self, title, message):
        QMessageBox.information(self, title, message)
    
    def showQuestion(self, title, question_text):
        return QMessageBox.question(self, title,
                 question_text, QMessageBox.Yes|QMessageBox.No)
