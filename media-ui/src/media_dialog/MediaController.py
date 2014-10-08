
from time import sleep
from PyQt4.QtCore import pyqtSignature, QObject, Qt, SIGNAL, QTime, QSize
from PyQt4.QtGui import QIcon

from .MediaDialog import MediaDialog

def _(val):
    return val

###############################################################################
###############################################################################
class MediaController(QObject):
    """
    """
    def __init__(self, rdb_proxy, config):
        super(MediaController, self).__init__(None)

        self.config = config
        self.rdb_proxy = rdb_proxy

        self.view = MediaDialog()

        self.view.connect(self.view,
                SIGNAL("MARKFORCOPY"), self.mark_for_copy)

        self.view.connect(self.view,
                SIGNAL("MARKFORUPLOAD"), self.mark_for_upload)

        self.view.connect(self.view,
                SIGNAL("ROWCLICKED"), self.handle_item_selected)

        self.view.connect(self.view,
                SIGNAL("RT_NEXT_PAGE"), self.handle_next_page)

        self.view.connect(self.view,
                SIGNAL("RT_PREVIOUS_PAGE"), self.handle_previous_page)

        self.view.connect(self.view,
                SIGNAL("RT_PAGE_LOADED"), self.handle_page_loaded)

        self.add_formats()

    def handle_page_loaded(self, values):
        if values[0] == values[1]:
            self.view.enable_next(False)
        else:
            self.view.enable_next(True)

        if values[0] == 1:
            self.view.enable_previous(False)
        else:
            self.view.enable_previous(True)

    def handle_item_selected(self, row):
        self.view.toggle_action_buttons(True)
        # enable

    def handle_next_page(self):
        self.view.toggle_action_buttons(False)

    def handle_previous_page(self):
        self.view.toggle_action_buttons(False)

    def add_formats(self):
        self.view.add_formats(
            [format['name'] for format in self.rdb_proxy.format_lookup()]
        )

    def mark_for_copy(self, recording_ids, formats):
        """ Confirm selection and check a format has been selected """
        if len(formats) == 0:
            self.view.show_format_selection_error('copy')
            return

        if self.view.confirm('copy'):
            self.emit(SIGNAL("MARKFORCOPY"), recording_ids, formats)

    def mark_for_upload(self, recording_ids, formats):
        """ confirm selection, check a format """

        if len(formats) == 0:
            self.view.show_format_selection_error('upload')
            return

        upload = self.view.confirm('upload')

        if not upload[0]:
            return

        self.emit(SIGNAL("MARKFORUPLOAD"), recording_ids, formats, upload[1])

    def confirm_upload_marking(self, is_immediate):
        self.view.confirm_upload_marking(is_immediate)

    def show(self):
        """
        """
        self.view.show()
