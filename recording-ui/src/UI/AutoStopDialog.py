# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AutoStopDialog.ui'
#
# Created: Tue May  5 12:38:32 2015
#      by: PyQt4 UI code generator 4.11.2
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

class Ui_AutoStopDialog(object):
    def setupUi(self, AutoStopDialog):
        AutoStopDialog.setObjectName(_fromUtf8("AutoStopDialog"))
        AutoStopDialog.resize(548, 297)
        AutoStopDialog.setMaximumSize(QtCore.QSize(550, 300))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(84, 84, 84))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(84, 84, 84))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(84, 84, 84))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(84, 84, 84))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(84, 84, 84))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(84, 84, 84))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(84, 84, 84))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(84, 84, 84))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(84, 84, 84))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        AutoStopDialog.setPalette(palette)
        AutoStopDialog.setStyleSheet(_fromUtf8("background: rgb(84, 84, 84)"))
        self.groupBox = QtGui.QGroupBox(AutoStopDialog)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 551, 301))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans Serif"))
        font.setPointSize(9)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet(_fromUtf8("background: rgb(84, 84, 84); color: white;"))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setFlat(True)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.extendButton = QtGui.QPushButton(self.groupBox)
        self.extendButton.setGeometry(QtCore.QRect(350, 240, 191, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.extendButton.setFont(font)
        self.extendButton.setStyleSheet(_fromUtf8("color: white;"))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("images/media-record.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.extendButton.setIcon(icon)
        self.extendButton.setIconSize(QtCore.QSize(32, 32))
        self.extendButton.setObjectName(_fromUtf8("extendButton"))
        self.stopButton = QtGui.QPushButton(self.groupBox)
        self.stopButton.setGeometry(QtCore.QRect(10, 240, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.stopButton.setFont(font)
        self.stopButton.setStyleSheet(_fromUtf8("color: white;"))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("images/media-playback-stop.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stopButton.setIcon(icon1)
        self.stopButton.setIconSize(QtCore.QSize(32, 32))
        self.stopButton.setObjectName(_fromUtf8("stopButton"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(-10, -10, 571, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet(_fromUtf8("color: red;"))
        self.label.setWordWrap(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.line = QtGui.QFrame(self.groupBox)
        self.line.setGeometry(QtCore.QRect(280, 230, 20, 61))
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.line_2 = QtGui.QFrame(self.groupBox)
        self.line_2.setGeometry(QtCore.QRect(10, 220, 531, 20))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(320, 100, 121, 31))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.radioButton_3 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_3.setGeometry(QtCore.QRect(420, 188, 51, 22))
        self.radioButton_3.setStyleSheet(_fromUtf8("color: white;"))
        self.radioButton_3.setObjectName(_fromUtf8("radioButton_3"))
        self.radioButton_2 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(360, 188, 51, 22))
        self.radioButton_2.setStyleSheet(_fromUtf8("color: white;"))
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(20, 180, 261, 41))
        self.label_3.setStyleSheet(_fromUtf8("color: white;"))
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.radioButton_1 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_1.setGeometry(QtCore.QRect(300, 188, 51, 22))
        self.radioButton_1.setStyleSheet(_fromUtf8("color: white;"))
        self.radioButton_1.setChecked(True)
        self.radioButton_1.setObjectName(_fromUtf8("radioButton_1"))
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(470, 190, 66, 17))
        self.label_4.setStyleSheet(_fromUtf8("color: white"))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.countdown_label = QtGui.QLabel(self.groupBox)
        self.countdown_label.setGeometry(QtCore.QRect(150, 90, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.countdown_label.setFont(font)
        self.countdown_label.setStyleSheet(_fromUtf8("color: red;"))
        self.countdown_label.setObjectName(_fromUtf8("countdown_label"))
        self.schedule_label = QtGui.QLabel(self.groupBox)
        self.schedule_label.setGeometry(QtCore.QRect(70, 150, 261, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.schedule_label.setFont(font)
        self.schedule_label.setWordWrap(True)
        self.schedule_label.setObjectName(_fromUtf8("schedule_label"))
        self.end_time_label = QtGui.QLabel(self.groupBox)
        self.end_time_label.setGeometry(QtCore.QRect(350, 150, 91, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.end_time_label.setFont(font)
        self.end_time_label.setStyleSheet(_fromUtf8("color: white"))
        self.end_time_label.setWordWrap(True)
        self.end_time_label.setObjectName(_fromUtf8("end_time_label"))
        self.label_9 = QtGui.QLabel(self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(150, 60, 261, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setWordWrap(True)
        self.label_9.setObjectName(_fromUtf8("label_9"))

        self.retranslateUi(AutoStopDialog)
        QtCore.QMetaObject.connectSlotsByName(AutoStopDialog)

    def retranslateUi(self, AutoStopDialog):
        AutoStopDialog.setWindowTitle(_translate("AutoStopDialog", "Automatic Stop In Progress...", None))
        self.extendButton.setText(_translate("AutoStopDialog", "EXTEND BOOKING", None))
        self.stopButton.setText(_translate("AutoStopDialog", "STOP RECORDING", None))
        self.label.setText(_translate("AutoStopDialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:48pt;\">WARNING!!</span></p></body></html>", None))
        self.label_2.setText(_translate("AutoStopDialog", "<html><head/><body><p><span style=\" font-size:20pt; font-weight:600; color:#fd0000;\">MINUTES</span></p></body></html>", None))
        self.radioButton_3.setText(_translate("AutoStopDialog", "20", None))
        self.radioButton_2.setText(_translate("AutoStopDialog", "10", None))
        self.label_3.setText(_translate("AutoStopDialog", "<html><head/><body><p><span style=\" font-weight:600;\">Select a duration and press &quot;Extend Booking&quot; to add time.</span></p></body></html>", None))
        self.radioButton_1.setText(_translate("AutoStopDialog", "5", None))
        self.label_4.setText(_translate("AutoStopDialog", "MINUTES", None))
        self.countdown_label.setText(_translate("AutoStopDialog", "00:00", None))
        self.schedule_label.setText(_translate("AutoStopDialog", "<html><head/><body><p><span style=\" color:#ffffff;\">This booking is scheduled to end at</span></p></body></html>", None))
        self.end_time_label.setText(_translate("AutoStopDialog", "<html><head/><body><p><span style=\" font-size:14pt;\">17:00</span></p></body></html>", None))
        self.label_9.setText(_translate("AutoStopDialog", "<html><head/><body><p><span style=\" color:#ffffff;\">Recording will automatically stop in:</span></p></body></html>", None))

