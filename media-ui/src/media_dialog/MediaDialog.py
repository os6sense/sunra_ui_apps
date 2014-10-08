""" """

from PyQt4.QtGui import QDialog, QIcon, QTableWidgetItem, QCheckBox
from PyQt4.QtGui import QHBoxLayout, QMessageBox
from PyQt4.QtCore import pyqtSignature, QTimer, SIGNAL, Qt

from UI.CenterDialog import CenterDialog
from UI.copier_dialog import Ui_Dialog
from UI.upload_select import Ui_UploadSelectDialog

from sunra.recording_table_widget.RecordingTableWidget import RecordingTableWidget

# Generic Dialog for confirmation and selecting immediate or delayed
# upload.
class ConfirmationDialog(QDialog, CenterDialog, Ui_UploadSelectDialog):# Ui_confirmation_dialog):
    def __init__(self, parent=None):
        super(ConfirmationDialog, self).__init__(parent)
        self.setupUi(self)
        self.center()

        self.setStyleSheet( """
            background: rgb(84, 84, 84);
            color: white;
            font-weight: bold;
        """)

        self.setWindowFlags(Qt.WindowStaysOnTopHint)

        self._selection_made = False # Flag to ensure we dont treat a close
                                     # event as a cancel event
        self.immediate_upload = False
        self.cancelled = False
        self.copy_confirmed = False

    def closeEvent(self, event):
        if self._selection_made == False:
            self.cancelled = True

    def showInformation(self, title, text, parent=None):
        QMessageBox.information(parent, title, text)

    def showQuestion(self, title, question_text):
        response =  QMessageBox.question(self, title, question_text,
            QMessageBox.Yes | QMessageBox.No)

        if response == QMessageBox.Yes:
            self._selection_made = True
            self.copy_confirmed = True
        else:
            self._selection_made = True
            self.copy_confirmed = False

    def setText(self, title, question_text):
        self.upload_message.setText(question_text)

    def show(self):
        self._selection_made = False
        self.immediate_upload = False
        self.cancelled = False

        self.center()
        super(ConfirmationDialog, self).show()

    def exec_(self):
        self._selection_made = False
        self.immediate_upload = False
        self.cancelled = False

        self.center()
        super(ConfirmationDialog, self).exec_()

    @pyqtSignature("")
    def on_cancel_button_clicked(self):
        self._selection_made = True
        self.cancelled = True
        self.close()

    @pyqtSignature("")
    def on_upload_overnight_button_clicked(self):
        self._selection_made = True
        self.immediate_upload = False
        self.close()

    @pyqtSignature("")
    def on_upload_immediately_button_clicked(self):
        self._selection_made = True
        self.immediate_upload = True
        self.close()

# Main Dialog
class MediaDialog(QDialog, Ui_Dialog, CenterDialog):
    """
    """
    def __init__(self, parent=None):
        super(MediaDialog, self).__init__(parent)
        self.setupUi(self)
        self.center()

        self.setWindowFlags(Qt.WindowStaysOnTopHint)

        self.recordings_table = RecordingTableWidget(parent=self)
        self.table_container.layout().addWidget(self.recordings_table)

        self.file_formats_container.setLayout(QHBoxLayout())

        self.recordings_table.connect(self.recordings_table,
                SIGNAL("ROWCLICKED"), self.reemit_item_selected)

        self.recordings_table.connect(self.recordings_table,
                SIGNAL("RT_PAGE_LOADED"), self.reemit_page_loaded)

        self.confirmation_dialog = ConfirmationDialog(parent)

        self._formats = []

        self.setStyleSheet( """
            background: rgb(84, 84, 84);
            color:white;
        """)

    def enable_previous(self, val):
        self.newerButton.setEnabled(val)

    def enable_next(self, val):
        self.olderButton.setEnabled(val)

    def reemit_item_selected(self, row):
        self.emit(SIGNAL("ROWCLICKED"), row)

    def reemit_page_loaded(self, values):
        self.emit(SIGNAL("RT_PAGE_LOADED"), values)

    def _get_selected_formats(self):
        _selected_formats = []
        for cb in self._formats:
            if cb.isChecked():
                _selected_formats.append(str(cb.text()))
        return _selected_formats

    selected_formats = property(_get_selected_formats)

    @pyqtSignature("")
    def on_cancelButton_clicked(self):
        self.close()

    @pyqtSignature("")
    def on_copyButton_clicked(self):
        self.emit(SIGNAL("MARKFORCOPY"),
                self.recordings_table.selected,
                self._get_selected_formats()
                )

    @pyqtSignature("")
    def on_uploadButton_clicked(self):
        self.emit(SIGNAL("MARKFORUPLOAD"),
                self.recordings_table.selected,
                self._get_selected_formats()
                )

    @pyqtSignature("")
    def on_olderButton_clicked(self):
        """ Essentially our Back behavior """
        self.emit(SIGNAL("RT_NEXT_PAGE"))
        self.recordings_table.next_page()

    @pyqtSignature("")
    def on_newerButton_clicked(self):
        """ Forward to beginging i.e. newer bookings """
        self.emit(SIGNAL("RT_PREVIOUS_PAGE"))
        self.recordings_table.previous_page()

    def toggle_action_buttons(self, val):
        """
        enable/disable nav button depending if there are newer
            or older pages.
        """
        self.copyButton.setEnabled(val)
        self.uploadButton.setEnabled(val)
        self.file_formats_container.setEnabled(val)

    def add_formats(self, formats):
        """
        Add the list of available media formats to the dialog
        as checkbox options
        """
        self._formats = []
        layout = self.file_formats_container.layout()
        for i in range(layout.count()):
            layout.itemAt(i).widget().close()

        self._formats_as_string = ""
        for format in formats:
            self._formats_as_string += " " + format
            cb = QCheckBox(format, self)
            cb.setMinimumWidth(100)
            cb.setStyleSheet("color: white")

            if format == "MP3":
                cb.setChecked(True)

            self._formats.append(cb)
            self.file_formats_container.layout().addWidget(cb)

    def confirm(self, action):
        """
        Confirm the selection and return a tupple where the first parameter
        indicates the cancellation status (true if cancelled) and the second
        whether or not to upload immediately.
        """
        title = "%s : P L E A S E  C O N F I R M" % action
        question_text = "<html><b>%s - PLEASE CONFIRM.</b><br/>"\
                "<br/>Do you want to %s %s recordings for the following project?"\
                "<br/><br/>PROJECT : %s"\
                "<br/>CLIENT : %s"\
                "<br/>DATE   : %s<br/></html>" % (
                action.upper(),
                action,
                " & ".join(self.selected_formats),
                self.recordings_table.project_details()[2],
                self.recordings_table.project_details()[3],
                self.recordings_table.project_details()[0]
                )

        self.hide()
        if action == 'upload':
            self.confirmation_dialog.setText(title, question_text)
            self.confirmation_dialog.exec_()
            self.show()

            if self.confirmation_dialog.cancelled:
                return (False, False)

            return (True, self.confirmation_dialog.immediate_upload)
        else:
            self.confirmation_dialog.showQuestion(title, question_text)
            self.show()
            return self.confirmation_dialog.copy_confirmed

    def confirm_upload_marking(self, is_immediate):
        if is_immediate:
            text = "Recordings are now being uploaded to the archive server "
        else:
            text = "Recordings will be uploaded to the archive server overnight"

        self.confirmation_dialog.showInformation("S U C C E S S", text, self)

    def show_format_selection_error(self, action=None):
        QMessageBox.information(self, "Please select a format",
                    "Please select at least one of the available formats" +
                    "(%s) to %s" % (self._formats_as_string, action))
        return
