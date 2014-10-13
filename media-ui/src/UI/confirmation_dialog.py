# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'confirmation_dialog.ui'
#
# Created: Mon Oct 13 20:09:16 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_confirmation_dialog(object):
    def setupUi(self, confirmation_dialog):
        confirmation_dialog.setObjectName(_fromUtf8("confirmation_dialog"))
        confirmation_dialog.resize(212, 54)

        self.retranslateUi(confirmation_dialog)
        QtCore.QMetaObject.connectSlotsByName(confirmation_dialog)

    def retranslateUi(self, confirmation_dialog):
        confirmation_dialog.setWindowTitle(_translate("confirmation_dialog", "Dialog", None))

