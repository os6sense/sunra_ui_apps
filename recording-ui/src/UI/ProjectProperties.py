# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ProjectProperties.ui'
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

class Ui_ProjectProperties(object):
    def setupUi(self, ProjectProperties):
        ProjectProperties.setObjectName(_fromUtf8("ProjectProperties"))
        ProjectProperties.setWindowModality(QtCore.Qt.WindowModal)
        ProjectProperties.resize(800, 397)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 85, 85))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 85, 85))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 85, 85))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 85, 85))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 85, 85))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 85, 85))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 85, 85))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 85, 85))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 85, 85))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        ProjectProperties.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans Serif"))
        font.setPointSize(10)
        ProjectProperties.setFont(font)
        ProjectProperties.setStyleSheet(_fromUtf8("background: rgb(85, 85, 85);\n"
"color: white;"))
        ProjectProperties.setModal(True)
        self.groupBox_2 = QtGui.QGroupBox(ProjectProperties)
        self.groupBox_2.setGeometry(QtCore.QRect(75, 20, 650, 331))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setTitle(_fromUtf8(""))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.label_2 = QtGui.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(5, 40, 131, 18))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label = QtGui.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(5, 80, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_4 = QtGui.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(0, 180, 641, 131))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(_fromUtf8("color: white;"))
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_3 = QtGui.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(5, 0, 81, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.studio_name_label = QtGui.QLabel(self.groupBox_2)
        self.studio_name_label.setGeometry(QtCore.QRect(190, 0, 141, 17))
        self.studio_name_label.setObjectName(_fromUtf8("studio_name_label"))
        self.start_time = QtGui.QTimeEdit(self.groupBox_2)
        self.start_time.setGeometry(QtCore.QRect(190, 130, 81, 27))
        self.start_time.setStyleSheet(_fromUtf8("background: white;\n"
"color: black;"))
        self.start_time.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.start_time.setSpecialValueText(_fromUtf8(""))
        self.start_time.setObjectName(_fromUtf8("start_time"))
        self.end_time = QtGui.QTimeEdit(self.groupBox_2)
        self.end_time.setGeometry(QtCore.QRect(470, 130, 81, 27))
        self.end_time.setStyleSheet(_fromUtf8("background: white;\n"
"color: black;"))
        self.end_time.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.end_time.setObjectName(_fromUtf8("end_time"))
        self.label_6 = QtGui.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(5, 135, 141, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(self.groupBox_2)
        self.label_7.setGeometry(QtCore.QRect(340, 0, 151, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.date_label = QtGui.QLabel(self.groupBox_2)
        self.date_label.setGeometry(QtCore.QRect(500, 0, 141, 17))
        self.date_label.setObjectName(_fromUtf8("date_label"))
        self.label_9 = QtGui.QLabel(self.groupBox_2)
        self.label_9.setGeometry(QtCore.QRect(380, 135, 91, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.line = QtGui.QFrame(self.groupBox_2)
        self.line.setGeometry(QtCore.QRect(0, 20, 651, 20))
        self.line.setStyleSheet(_fromUtf8("color: white;"))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.line_2 = QtGui.QFrame(self.groupBox_2)
        self.line_2.setGeometry(QtCore.QRect(0, 110, 651, 20))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.line_3 = QtGui.QFrame(self.groupBox_2)
        self.line_3.setGeometry(QtCore.QRect(0, 160, 651, 20))
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.line_4 = QtGui.QFrame(self.groupBox_2)
        self.line_4.setGeometry(QtCore.QRect(0, 320, 651, 20))
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.leClientName = QtGui.QLineEdit(self.groupBox_2)
        self.leClientName.setGeometry(QtCore.QRect(190, 40, 451, 27))
        self.leClientName.setStyleSheet(_fromUtf8("background: white;\n"
"color: black;"))
        self.leClientName.setObjectName(_fromUtf8("leClientName"))
        self.leProjectTitle = QtGui.QLineEdit(self.groupBox_2)
        self.leProjectTitle.setGeometry(QtCore.QRect(190, 80, 451, 27))
        self.leProjectTitle.setStyleSheet(_fromUtf8("background: white;\n"
"color: black;"))
        self.leProjectTitle.setObjectName(_fromUtf8("leProjectTitle"))
        self.set_start_time = QtGui.QPushButton(self.groupBox_2)
        self.set_start_time.setGeometry(QtCore.QRect(280, 130, 81, 31))
        self.set_start_time.setObjectName(_fromUtf8("set_start_time"))
        self.set_end_time = QtGui.QPushButton(self.groupBox_2)
        self.set_end_time.setGeometry(QtCore.QRect(560, 130, 81, 31))
        self.set_end_time.setObjectName(_fromUtf8("set_end_time"))
        self.create_project_button = QtGui.QPushButton(ProjectProperties)
        self.create_project_button.setEnabled(True)
        self.create_project_button.setGeometry(QtCore.QRect(540, 360, 191, 32))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("images/applications-multimedia.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.create_project_button.setIcon(icon)
        self.create_project_button.setIconSize(QtCore.QSize(24, 24))
        self.create_project_button.setObjectName(_fromUtf8("create_project_button"))
        self.cancelButton = QtGui.QPushButton(ProjectProperties)
        self.cancelButton.setGeometry(QtCore.QRect(390, 360, 131, 32))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("images/window-close.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cancelButton.setIcon(icon1)
        self.cancelButton.setIconSize(QtCore.QSize(24, 24))
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))

        self.retranslateUi(ProjectProperties)
        QtCore.QMetaObject.connectSlotsByName(ProjectProperties)

    def retranslateUi(self, ProjectProperties):
        ProjectProperties.setWindowTitle(_translate("ProjectProperties", "Enter Booking/Project Details Please.", None))
        self.label_2.setText(_translate("ProjectProperties", "CLIENT:", None))
        self.label.setText(_translate("ProjectProperties", "PROJECT:", None))
        self.label_4.setText(_translate("ProjectProperties", "<html><head/><body><p align=\"justify\">CLIENT and PROJECT information should be available from the paper copy of the booking form.</p><p align=\"justify\">Press the SET buttons to provide a START and END TIME for the booking. This can be approximate but should cover the entire booking. Please ensure the end time is the <span style=\" font-weight:600;\">latest</span> time at which a project might end.</p><p align=\"justify\">Please click the &quot;OK&quot; button below when you have entered this information</p></body></html>", None))
        self.label_3.setText(_translate("ProjectProperties", "STUDIO:", None))
        self.studio_name_label.setText(_translate("ProjectProperties", "MONK", None))
        self.label_6.setText(_translate("ProjectProperties", "START TIME:", None))
        self.label_7.setText(_translate("ProjectProperties", "PROJECT DATE:", None))
        self.date_label.setText(_translate("ProjectProperties", "TODAY 04/02/14", None))
        self.label_9.setText(_translate("ProjectProperties", "END TIME:", None))
        self.set_start_time.setText(_translate("ProjectProperties", "SET", None))
        self.set_end_time.setText(_translate("ProjectProperties", "SET", None))
        self.create_project_button.setText(_translate("ProjectProperties", "CREATE PROJECT", None))
        self.cancelButton.setText(_translate("ProjectProperties", "CANCEL", None))

