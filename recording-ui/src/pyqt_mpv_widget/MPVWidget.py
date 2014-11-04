#!/usr/bin/env python
# Adapted from Henning Schr?ders Qt3 Mplayer Widget
# see http://henning.cco-ev.de/mplayer_py.txt

# Also see:
# http://www.mplayerhq.hu/DOCS/tech/slave.txt
# http://mediacoder.sourceforge.net/wiki/index.php/MPlayer_Slave_Mode_Protocol
# mplayer -input cmdlist

import os, atexit, subprocess

from PyQt4.QtGui import QWidget
from PyQt4.QtCore import SIGNAL, Qt

from MPVRunner import MPVRunner
from FIFOController import FifoController

class MPVWidget(QWidget):
    """
    Wrapper around MPV in slave mode to allow us to play video on any
    QT Component.
    """
    CFG = dict(AO="alsa", VO="xv")

    def __init__(self, parent=None):
        super(MPVWidget, self).__init__(parent)

        self.process = None
        self.muted = True
        self.fullscreen_flag = False
        self.pause_flag = False
        self.stamp_size = True

        self.playback_controller = FifoController()

        self.CFG["FIFO"] = self.playback_controller.fifo_filename()
        self.CFG["FILENAME"] = "http://localhost:8090/livehq.flv"

    def stop(self):
        """ Stop Play Back"""
        self.exit()

    def toggle_stamp_size(self):
        """ toggle between an extremely small and full size """
        # unless we resize the parent, we just end up with a black screen
        if self.stamp_size:
            self.parent().resize(320, 200)
        else:
            self.parent().resize(self.parent().parent().size())

        self.stamp_size = not self.stamp_size

    def start(self, filename, winid=None, position=0):
        """
        Start Playback. If winid is suplied output will be in THAT QT
        window/container.
        if position is supplied playback will start at that number of
        seconds into the video
        """
        if winid is not None:
            self.CFG["WID"] = winid
        else:
            self.CFG["WID"] = self.winId()

        self.pause_flag = False
        self.fullscreen_flag = False

        self.CFG["TIME"] = position
        self.CFG["FILENAME"] = filename

        # There was a bug with video not displaying sometimes, and this delay
        # was added to solve that problem; however it is unclear if the issue
        # will remain with MPV rather than mplayer hence the delay is disabled
        # for testing.
        # time.sleep(1)
        self.process = MPVRunner.execute(self.CFG)

        atexit.register(self.exit)

    def play(self, filename):
        """
        Pass the name of a file and immediately start playback.
        """
        if self.process: # if already playing stop
            self.process.kill()

        self.start(filename)

    def osd(self, msg, duration=5):
        """
        msg can be any string but AVOID single quotes.
        Duration is measured in seconds and defaults to 5.
        """
        self("osd_show_text '%s' %s" % (msg, duration * 1000))

    def exit(self):
        """
        Close any playing files.
        """
        if self.process:
            self.process.kill()

        self.playback_controller.close_fifo()

        # Nuclear option since the above does not work it seems
        # subprocess.call("killall -9 mpv", shell=True)
        MPVRunner.STOP = True
        MPVRunner.nuke()

        self.close()

    def __call__(self, cmd):
        """
        When called will try and pass cmd to the running process.
        Used to control slave functions.
        """
        if self.process:
            self.process.stdin.write("\n%s\n" % cmd)

    def load(self, url):
        """
        load and play a new file.
        """
        self.CFG["FILENAME"] = url
        self("loadfile %s" % url)


    def toggle_mute(self):
        """
        Switch between mute and unmute.
        """
        self.muted = not self.muted
        self("mute")

    def fullscreen(self):
        """
        Switch to fullscreen mode.
        """
        if not self.fullscreen_flag:
            self("vo_fullscreen")
            self.fullscreen_flag = True

    def windowed(self):
        """
        Switch to windowed mode.
        """
        if self.fullscreen_flag:
            self("vo_fullscreen")
            self.fullscreen_flag = False

    def search_to(self, s_time):
        """
        Seek to a given position in the video.
        """
        self("ss " + s_time)

