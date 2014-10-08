# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'upload_select.ui'
#
# Created: Thu Jul 31 18:49:23 2014
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

class Ui_UploadSelectDialog(object):
    def setupUi(self, UploadSelectDialog):
        UploadSelectDialog.setObjectName(_fromUtf8("UploadSelectDialog"))
        UploadSelectDialog.setWindowModality(QtCore.Qt.WindowModal)
        UploadSelectDialog.resize(764, 284)
        UploadSelectDialog.setMinimumSize(QtCore.QSize(0, 284))
        UploadSelectDialog.setMaximumSize(QtCore.QSize(788, 284))
        UploadSelectDialog.setStyleSheet(_fromUtf8("background: rgb(85, 85, 85);"))
        UploadSelectDialog.setSizeGripEnabled(False)
        UploadSelectDialog.setModal(True)
        self.verticalLayout = QtGui.QVBoxLayout(UploadSelectDialog)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.frame_2 = QtGui.QFrame(UploadSelectDialog)
        self.frame_2.setMinimumSize(QtCore.QSize(760, 160))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 160))
        self.frame_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.upload_message = QtGui.QLabel(self.frame_2)
        self.upload_message.setGeometry(QtCore.QRect(20, 10, 751, 141))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.upload_message.setFont(font)
        self.upload_message.setText(_fromUtf8(""))
        self.upload_message.setObjectName(_fromUtf8("upload_message"))
        self.verticalLayout.addWidget(self.frame_2)
        self.frame = QtGui.QFrame(UploadSelectDialog)
        self.frame.setMinimumSize(QtCore.QSize(760, 100))
        self.frame.setFrameShape(QtGui.QFrame.VLine)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.cancel_button = QtGui.QPushButton(self.frame)
        self.cancel_button.setGeometry(QtCore.QRect(100, 30, 170, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.cancel_button.setFont(font)
        self.cancel_button.setStyleSheet(_fromUtf8("color: white"))
        self.cancel_button.setObjectName(_fromUtf8("cancel_button"))
        self.upload_overnight_button = QtGui.QPushButton(self.frame)
        self.upload_overnight_button.setGeometry(QtCore.QRect(400, 20, 340, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.upload_overnight_button.setFont(font)
        self.upload_overnight_button.setStyleSheet(_fromUtf8("color: white"))
        self.upload_overnight_button.setObjectName(_fromUtf8("upload_overnight_button"))
        self.upload_immediately_button = QtGui.QPushButton(self.frame)
        self.upload_immediately_button.setGeometry(QtCore.QRect(400, 60, 340, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.upload_immediately_button.setFont(font)
        self.upload_immediately_button.setStyleSheet(_fromUtf8("color: white"))
        self.upload_immediately_button.setObjectName(_fromUtf8("upload_immediately_button"))
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(UploadSelectDialog)
        QtCore.QMetaObject.connectSlotsByName(UploadSelectDialog)

    def retranslateUi(self, UploadSelectDialog):
        UploadSelectDialog.setWindowTitle(_translate("UploadSelectDialog", "C O N F I R M  &  S E L E C T  U P L O A D  O P T I O N", None))
        self.cancel_button.setText(_translate("UploadSelectDialog", "C A N C E L", None))
        self.upload_overnight_button.setText(_translate("UploadSelectDialog", "U P L O A D  O V E R N I G H T", None))
        self.upload_immediately_button.setText(_translate("UploadSelectDialog", "U P L O A D  I M M E D I A T E L Y", None))

