from MPVWidget import MPVWidget

from PyQt4.QtGui import QWidget, QApplication, QFrame, QBoxLayout, QDialog
from PyQt4.QtGui import QPushButton, QVBoxLayout
from PyQt4.QtCore import SIGNAL, Qt

class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.init()

    def init(self):
        self.setLayout(QBoxLayout(0, self))
        self.setWindowModality(Qt.WindowModal)

        self.frame = QFrame(self)
        self.frame.setStyleSheet("background: black;")
        self.frame.move(0, 0)
        self.frame.resize(self.size().width(), self.size().height())
        self.frame.setAttribute( Qt.WA_OpaquePaintEvent )

        self.button = QPushButton('Test', self)
        self.button.clicked.connect(self.handleButton)
        layout = QVBoxLayout(self)
        layout.addWidget(self.button)

    def handleButton(self):
        self.emit(SIGNAL("clicked"))

def osd():
    mp.osd("OSD Display text")

if __name__ == "__main__":

    import sys
    if len(sys.argv) != 2:
        print "Usage: %s FILENAME" % sys.argv[0]
        sys.exit()

    app = QApplication(sys.argv)
    example = Example()
    example.resize(640, 480)
    example.show()

    mp = MPVWidget(example.frame)

    app.connect(app, SIGNAL("quit"), mp.exit)
    app.connect(example, SIGNAL("clicked"), osd)

    mp.start(sys.argv[1], example.frame.winId())

    app.exec_()


