#!/usr/bin/env python
# Adapted from Henning Schr?ders Qt3 Mplayer Widget
# see http://henning.cco-ev.de/mplayer_py.txt

# Also see:
# http://www.mplayerhq.hu/DOCS/tech/slave.txt
# http://mediacoder.sourceforge.net/wiki/index.php/MPlayer_Slave_Mode_Protocol
# mplayer -input cmdlist

#import os
import atexit

import subprocess
import time

from PyQt4.QtGui import QWidget, QApplication, QFrame, QBoxLayout, QDialog
from PyQt4.QtGui import QGraphicsOpacityEffect, QPen, QPainter, QGridLayout
from PyQt4.QtCore import SIGNAL, Qt, QTimer, QObject

from pa_peak_monitor import PAPeakMonitor, PAPeakMonitorException

class VUWidgetView(QWidget):
    """
    """
    def __init__(self, parent):
        super(VUWidgetView, self).__init__(parent)
        self.vu_len = 0
        self.initUI()
        self.resizeEvent = self.onResize

    def initUI(self):      
        self.black_pen = QPen(Qt.black, 4, Qt.SolidLine)
        self.green_pen = QPen(Qt.green, 4, Qt.SolidLine)

        self.vu_height = self.height() - 20
        self.vu_height = 300
        self.show()

    def update(self, sample):
        self.vu_height = self.height() - 20
        self.vu_len = sample
        self.repaint()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
 
        qp.setPen(self.black_pen)
        qp.drawLine(10, 10, 10, self.vu_height - self.vu_len)

        qp.setPen(self.green_pen)
        qp.drawLine(10, self.vu_height - self.vu_len, 10, self.vu_height)

        qp.end()

    def onResize(self, event):
        self.vu_height = self.height() - 20

class VUMeter(QObject):
    KITCHEN_SINK = 'alsa_output.pci-0000_00_1b.0.analog-stereo'

    def __init__(self, parent, sink_name=None):
        super(VUMeter, self).__init__(parent)

        if sink_name == None:
            self.sink_name = self.KITCHEN_SINK
        else:
            self.sink_name = sink_name

        self.meter_rate = 344
        self.display_scale = 8
        self.monitor = PAPeakMonitor(self.sink_name, self.meter_rate)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(100)

        self.view = VUWidgetView(parent)
        self.view.setGeometry(0, 0, 20, parent.height() )

    def update(self):
        for sample in self.monitor:
            sample = sample * self.display_scale
            self.view.update(sample)


class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.init()
        
    def init(self):      
        self.vumeter = VUMeter(self)

        self.setWindowModality(Qt.WindowModal)
        layout = QGridLayout(self)
        layout.addWidget(self.vumeter.view)
        self.setLayout(layout)

        self.setWindowTitle('VU Meter Example')
        self.show()
        
        
if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    
    example = Example()

    example.resize(640, 480)
    app.exec_()
