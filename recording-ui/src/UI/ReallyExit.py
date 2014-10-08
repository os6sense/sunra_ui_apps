# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ReallyExit.ui'
#
# Created: Wed Jul  2 15:38:43 2014
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

class Ui_ExitDialog(object):
    def setupUi(self, ExitDialog):
        ExitDialog.setObjectName(_fromUtf8("ExitDialog"))
        ExitDialog.resize(537, 145)
        ExitDialog.setMaximumSize(QtCore.QSize(550, 250))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        ExitDialog.setPalette(palette)
        self.groupBox = QtGui.QGroupBox(ExitDialog)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 541, 151))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans Serif"))
        font.setPointSize(9)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet(_fromUtf8("background: rgb(84, 84, 84)"))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.exitButton = QtGui.QPushButton(self.groupBox)
        self.exitButton.setGeometry(QtCore.QRect(330, 80, 171, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans Serif"))
        font.setPointSize(10)
        self.exitButton.setFont(font)
        self.exitButton.setStyleSheet(_fromUtf8("color: white;"))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("images/window-close.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exitButton.setIcon(icon)
        self.exitButton.setIconSize(QtCore.QSize(32, 32))
        self.exitButton.setObjectName(_fromUtf8("exitButton"))
        self.returnButton = QtGui.QPushButton(self.groupBox)
        self.returnButton.setGeometry(QtCore.QRect(60, 80, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.returnButton.setFont(font)
        self.returnButton.setStyleSheet(_fromUtf8("color: white;"))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("images/go-previous.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.returnButton.setIcon(icon1)
        self.returnButton.setIconSize(QtCore.QSize(32, 32))
        self.returnButton.setObjectName(_fromUtf8("returnButton"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 0, 511, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet(_fromUtf8("color: red;"))
        self.label.setWordWrap(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.line = QtGui.QFrame(self.groupBox)
        self.line.setGeometry(QtCore.QRect(270, 80, 20, 61))
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.line_2 = QtGui.QFrame(self.groupBox)
        self.line_2.setGeometry(QtCore.QRect(10, 60, 515, 20))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))

        self.retranslateUi(ExitDialog)
        QtCore.QMetaObject.connectSlotsByName(ExitDialog)

    def retranslateUi(self, ExitDialog):
        ExitDialog.setWindowTitle(_translate("ExitDialog", "Really Exit Recording?", None))
        self.exitButton.setText(_translate("ExitDialog", "REALLY EXIT?", None))
        self.returnButton.setText(_translate("ExitDialog", "BACK TO RECORDING", None))
        self.label.setText(_translate("ExitDialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">YOU HAVE CHOSEN TO QUIT RECORDING.</span></p><p align=\"center\"><span style=\" font-size:9pt; color:#ffffff;\">Please only do this if there are no further groups to record for this booking.</span></p></body></html>", None))

