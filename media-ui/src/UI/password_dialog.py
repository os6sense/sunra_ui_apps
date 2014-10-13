# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'password_dialog.ui'
#
# Created: Mon Oct 13 20:09:15 2014
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(588, 114)
        Dialog.setStyleSheet(_fromUtf8("background: rgb(85, 85, 85);"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 9, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(_fromUtf8("color: white;"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.password = QtGui.QLineEdit(Dialog)
        self.password.setGeometry(QtCore.QRect(190, 5, 391, 27))
        self.password.setStyleSheet(_fromUtf8("background: white"))
        self.password.setEchoMode(QtGui.QLineEdit.Password)
        self.password.setObjectName(_fromUtf8("password"))
        self.line = QtGui.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(10, 60, 571, 20))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.okButton = QtGui.QPushButton(Dialog)
        self.okButton.setGeometry(QtCore.QRect(410, 70, 170, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.okButton.setFont(font)
        self.okButton.setStyleSheet(_fromUtf8("color: white"))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../../lib/images/mail-mark-notjunk.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.okButton.setIcon(icon)
        self.okButton.setIconSize(QtCore.QSize(32, 32))
        self.okButton.setObjectName(_fromUtf8("okButton"))
        self.cancelButton = QtGui.QPushButton(Dialog)
        self.cancelButton.setGeometry(QtCore.QRect(240, 70, 170, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.cancelButton.setFont(font)
        self.cancelButton.setStyleSheet(_fromUtf8("color: white"))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("../../../lib/images/window-close.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cancelButton.setIcon(icon1)
        self.cancelButton.setIconSize(QtCore.QSize(32, 32))
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        self.error_message = QtGui.QLabel(Dialog)
        self.error_message.setGeometry(QtCore.QRect(190, 40, 391, 17))
        self.error_message.setStyleSheet(_fromUtf8("color: red"))
        self.error_message.setText(_fromUtf8(""))
        self.error_message.setObjectName(_fromUtf8("error_message"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "E N T E R  P A S S W O R D  . . .", None))
        self.label_2.setText(_translate("Dialog", "P A S S W O R D  :", None))
        self.okButton.setText(_translate("Dialog", "O K", None))
        self.cancelButton.setText(_translate("Dialog", "C A N C E L", None))

