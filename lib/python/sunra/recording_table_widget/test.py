

#!/usr/bin/env python
#-*- coding:utf-8 -*-

from PyQt4 import QtCore, QtGui

class myWindow(QtGui.QWidget):

    def __init__(self, parent=None):
        super(myWindow, self).__init__(parent)

        self.setStyleSheet( """ QListWidget:item:selected:active {
                                     background: blue;
                                }
                                QListWidget:item:selected:!active {
                                     background: gray;
                                }
                                QListWidget:item:selected:disabled {
                                     background: gray;
                                }
                                QListWidget:item:selected:!disabled {
                                     background: blue;
                                }
                                """
                                )

        self.listWidget = QtGui.QListWidget(self)
        self.listWidget.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)

        self.button = QtGui.QPushButton(self)
        self.button.setText("Disable the list!")
        self.button.clicked.connect(self.on_button_clicked)

        self.layout = QtGui.QVBoxLayout(self)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.listWidget)

        for itemNumber in range(5):
            item = QtGui.QListWidgetItem(self.listWidget)
            item.setText("Item {0}".format(itemNumber))
            self.listWidget.addItem(item)


    @QtCore.pyqtSlot()
    def on_button_clicked(self):
        enable = False if self.listWidget.isEnabled() else True

        self.listWidget.setEnabled(enable)

if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)
    app.setApplicationName('myWindow')

    main = myWindow()
    main.show()

    sys.exit(app.exec_())
