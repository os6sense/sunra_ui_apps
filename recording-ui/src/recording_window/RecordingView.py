# File:: recording_window.py

import pytz
from datetime import datetime

from PyQt4.QtGui import QDialog, QIcon, QTableWidgetItem, QMessageBox, QPushButton
from PyQt4.QtCore import pyqtSignature, Qt, QObject, QTimer, SIGNAL, QSize

from UI.RecordingWindow import Ui_RecordingWindow
from UI.CenterDialog import CenterDialog

from sunra.presenters import DatePresenter, TimerPresenter, TimePresenter
from studio_light_controller import StudioLightController

from pyqt_vumeter import VUMeter
from pyqt_mpv_widget import MPVWidget

def _(val):
    """
    Used for i18n
    """
    return val

class RecordingView(QDialog, Ui_RecordingWindow, CenterDialog):
    """
    Dialog class for the QT4 created Ui_RecordingWindow.
    This is the MAIN interface for the creation of recordings.
    """
    def __init__(self, preview_url, parent=None):
        super(RecordingView, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)
        self.setWindowFlags(self.windowFlags() | Qt.WindowMaximized)

        self.center()

        self._mplayer = MPVWidget.MPVWidget(parent=self.previewArea)

        self.lights = None
        if StudioLightController.connect():
            self.lights = StudioLightController()

        self.vu_meter = VUMeter.VUMeter(self)
        self.vu_meter_frame.layout().addWidget(self.vu_meter.view)

        self.preview_url = preview_url

        self.formats = {}

    def show(self):
        """ Activate the preview and show the form.  """
        self.__activatePreview(True)
        super(RecordingView, self).show()

    def set_recording_prompt(self, text):
        """ Set the red recording prompts text """
        self.recording_prompt.setText(text)

    def enable_ui(self, val):
        """
        put the recording controls into an enabled or disabled state.
        """
        self.lDuration.setStyleSheet("background:transparent; color: grey;")

        self.start_button_frame.setEnabled(val)
        self.duration_frame.setEnabled(val)
        self.lDuration.setEnabled(val)
        self.groupBox.setEnabled(val)
        self.quitButton.setEnabled(True)

    def update_from_model(self, model):
        """
        Update the UI based on details in the model.

        Params::
        model -- A model with booking details.
        """
        self.lCompanyName.setText(model.client_name.upper())
        self.lProjectName.setText(model.project_name.upper())
        self.lDate.setText(DatePresenter(model.date))

        self.lStartTime.setText(TimePresenter(model.start_time))
        self.lEndTime.setText(TimePresenter(model.end_time))

    def set_ui_stopped(self):
        """
        Put the UI in a state to reflect a stopped recording/No recording in
        progress.
        """
        start_str = _("START RECORDING")
        start_prompt_str = _("Click START RECORDING to begin.")
        start_wt_str = _("Session Recording - Press the START RECORDING " \
                         "button to record")

        if self.lights:
            self.lights.off()

        self.startRecordingButton.setText(start_str)
        self.startRecordingButton.setIcon(QIcon("images/media-record.png"))

        if self.startRecordingButton.isEnabled():
            self.recording_prompt.setText(start_prompt_str)
            self.lDuration.setStyleSheet("background: transparent; color: black");
            self.setWindowTitle(start_wt_str)

        self.quitButton.setEnabled(True)

    def set_ui_started(self):
        """
        Put the UI in a state to reflect a started recording/recording in
        progress.
        """
        stop_str = _("STOP RECORDING")
        stop_prompt_str = _("Click STOP RECORDING to end.")
        stop_wt_str = _("RECORDING IN PROGRESS -- RECORDING IN PROGRESS")

        if self.lights:
            self.lights.off()

        self.startRecordingButton.setText(stop_str)

        if self.startRecordingButton.isEnabled():
            self.recording_prompt.setText(stop_prompt_str)
            self.lDuration.setStyleSheet("background: transparent; color: red")
            self.setWindowTitle(stop_wt_str)

        self.quitButton.setEnabled(False)

        self.startRecordingButton.setIcon(
                QIcon("images/media-playback-stop.png"))

    def update_time(self, t):
        """
        Update the timer display of current date and time.
        """
        self.timeLabel.setText(TimerPresenter(t))

    @pyqtSignature("")
    def on_startRecordingButton_clicked(self):
        """
        Signal received - the start button has been clicked
        """
        self.emit(SIGNAL("RecordingButtonPressed"))

    def __setStampSize(self, bStamp):
        self._mplayer.toggle_stamp_size()

    @pyqtSignature("")
    def on_cbStampSize_clicked(self):
        """ change the size of the preview window """
        self.__setStampSize(self.cbStampSize.isChecked())

    def __activatePreview(self, activate_or_hide=True):
        """ activate the preview, starting mplayer """
        duration = 0.00

        if activate_or_hide == True:
            self._mplayer.start(self.preview_url,
                                self.previewArea.winId(),
                                duration)

            self.cbStampSize.setEnabled(True)
        else:
            self._mplayer.stop()
            self.cbStampSize.setEnabled(False)

    #@pyqtSignature("")
    #def on_checkBox_clicked(self):
        #""" Mute/Unmute the audio """
        #self._mplayer.toggle_mute()

    def update_status(self, status):
        """ Update the duration timer. """
        self.lDuration.setText(status['duration'])
        self.update_recorder_status(status)

    def update_recorder_status(self, status):
        """
        Update the list and color of the individual recording status
        icons.
        """
        for recorder in status['recorders']:
            if not recorder['format'] in self.formats:
                button = QPushButton(recorder['format'].upper(),
                        self.format_status_container)
                button.setIcon(QIcon('images/red_circle.png'))
                button.setIconSize(QSize(12, 12))
                button.setStyleSheet("outline: none; color: white;")
                button.resize(80, 30)
                button.setAutoDefault(False)
                button.setFlat(True)

                self.format_status_container.layout().addWidget(button)
                self.formats[recorder['format']] = button

            if recorder['is_recording']:
                self.formats[recorder['format']].setIcon(
                        QIcon("images/green_circle.png"))
            else:
                self.formats[recorder['format']].setIcon(
                        QIcon("images/red_circle.png"))

    def update_groups(self, groups):
        """ Update the list/table of completed groups.  """
        self.group_list.clear()
        for index, width in enumerate([40, 100, 100]):
            self.group_list.setColumnWidth(index, width)

        self.groupBox.setMinimumSize(0, len(groups)*30+30)
        self.group_list.setMinimumSize(0, len(groups)*30)

        self.group_list.setRowCount(len(groups))

        for row, group in enumerate(groups):
            if group.has_key('pagination'):
                continue

            self.group_list.setItem(row, 0,
                    QTableWidgetItem(str(group['group_number'])))

            self.group_list.setItem(row, 1,
                    QTableWidgetItem(TimePresenter(group['start_time'])))

            self.group_list.setItem(row, 2,
                    QTableWidgetItem(TimePresenter(group['end_time'])))


    # QUIT / EXIT handling
    # --------------------------------------------
    def closeEvent(self, event):
        self.emit(SIGNAL("CloseEvent"), event)

    @pyqtSignature("")
    def on_quitButton_clicked(self):
        self.close()
