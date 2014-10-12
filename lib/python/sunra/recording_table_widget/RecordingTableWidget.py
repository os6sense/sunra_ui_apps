"""
# A shared widget that
# - has a table view which will display all bookings
# - can be configured to show a button which emits a configured signal when
# - pressed.
# - paginates the table and responds to nextPage and previousPage methods
"""

from datetime import datetime, timedelta

from PyQt4.QtGui import QTableWidget, QTableWidgetItem, QWidget#, QPushButton
from PyQt4.QtGui import QApplication, QBoxLayout, QAbstractItemView#, QIcon
from PyQt4.QtGui import QSizePolicy
from PyQt4.QtCore import  QObject, Qt, SIGNAL, QSize# Policy

from sunra.config import Global
from sunra.recording_db_proxy import RecordingDBProxy
from sunra.presenters import TimePresenter

def _(val):
    """ Will you please move this to a shared lib? """
    return val

# - RecordingTableWidget
# ---- RecordingTableWidgetView
# ---- RecordingTableWidgetModel
# ---- RecordingTableWidgetController
###############################################################################

class RecordingTableWidget(QWidget):
    """
        A widget which provides a specialised table backed by the list of
        bookings from the rails api.
    """
    def __init__(self, parent=None):
        super(RecordingTableWidget, self).__init__(parent)

        self.rdb_proxy = RecordingDBProxy(Global())

        self.model = RecordingTableWidgetModel(self.rdb_proxy)
        self.view = RecordingTableWidgetView(parent=self)
        self.controller = RecordingTableWidgetController(self.model, self.view)

        self.view.connect(self.view,
                SIGNAL("ROWCLICKED"), self.handle_item_selected)

        self.init_ui()

    def handle_item_selected(self, row):
        self.emit(SIGNAL("ROWCLICKED"), row)

    def init_ui(self):
        """
        UI setup.
        """
        layout = QBoxLayout(0, self)
        self.setLayout(layout)
        layout.addWidget(self.view)
        self.view.move(0, 0)
        #self.view.resize(self.parent().width(), self.parent().height())
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

    def next_page(self):
        """
        get the next page of entries in the list of bookings.
        """
        self.controller.next_page()
        self._page_loaded()

    def previous_page(self):
        """
        get the previous page of entries in the list of bookings.
        """
        self.controller.previous_page()
        self._page_loaded()

    def _page_loaded(self):
        self.emit(SIGNAL("RT_PAGE_LOADED"),
                (self.current_page, self.page_count))

    def _get_selected(self):
        """ Returns the list of selected recording_ids as an array """
        return self.model.selected
    selected = property(_get_selected)

    def project_details(self):
        row = self.model.current_row
        if row == None:
            return ('', '', '', '')

        return (self.view.item(row, 0).text(),
          self.view.item(row, 1).text(),
          self.view.item(row, 2).text(),
          self.view.item(row, 3).text())

    def _get_page_count(self):
        return self.model.pages.page_count
    page_count = property(_get_page_count)

    def _get_current_page(self):
        return self.model.current_page
    current_page = property(_get_current_page)

###############################################################################
# VIEW
###############################################################################
class RecordingTableWidgetView(QTableWidget):
    """ Implements the view """
    def __init__(self, parent=None):
        QTableWidget.__init__(self, 5, 3)

        self.item_widget = None
        self.initUi()

    def set_item_widget(self, iw):
        self.item_widget = iw

    def initUi(self):
        self.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.setSelectionMode(QAbstractItemView.SingleSelection)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setShowGrid(False)
        self.verticalHeader().hide()
        self.setAlternatingRowColors(True)
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.itemClicked.connect(self.handle_item_clicked)

        self.setStyleSheet( """
            QHeaderView:section {
                font-weight: bold;
                color: orange;
                background: black;
            }

            QHeaderView:section:active {
                background: black;
            }

            QTableWidget {
                color: black;
            }

            QTableWidget:item:alternate {
                background: rgb(84, 84, 84);
                color: white;
            }
            QTableWidget:item:selected {
                background: orange;
                color: black;
            }
            """)
        self.setFrameShape(0)


    def add_item(self, row, col, text, centre=False):
        """
        Add a textual item to the table widget.

        Params::
        row -- row
        col -- col
        text -- text
        """
        item = QTableWidgetItem(str(text))

        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        self.setItem(row, col, item)

    def create_headers(self):
        """ Create table headers """
        self.setColumnCount(5)
        self.setHorizontalHeaderLabels(
                [_("D A T E"),
                _("T I M E"),
                _("P R OJ E C T  N A M E"),
                _("C L I E N T  N A M E"),
                _("# R E C O R D I N G S")])

        for ind, width in enumerate([140, 140, 250, 298, 150]):
            self.setColumnWidth(ind, width)

    def populate(self, model):
        """
        populate the session table with page data
        """
        row = -1

        self.clear()

        self.create_headers()
        page = model.pages.get(model.current_page).json()

        for session in page:
            row += 1
            self.setRowCount(row+1)

            self.add_item(row, 0, session['date'])
            self.add_item(row, 1, TimePresenter(session['start_time']))
            self.add_item(row, 2, session['project']['project_name'])
            self.add_item(row, 3, session['project']['client_name'])

            self.add_item(row, 4, len(session['recordings']), True)

            recordings = []
            for recording in session['recordings']:
                recordings.append(recording['id'])

            #if len(recordings) > 0 and self.item_widget != None:
                #iw = self.item_widget()
                #iw.clicked.connect(lambda fa, s=session['id'], r=recordings:
                            #self.emit(SIGNAL("ITEMSELECTED"), (s, r)))

                #self.setCellWidget(row, 6, iw)

    def handle_item_clicked(self, item):
        """ Emits ROWCLICKED signal which provides the index of the row """
        self.emit(SIGNAL("ROWCLICKED"), item.row())

###############################################################################
# Controller
###############################################################################
class RecordingTableWidgetController(QObject):
    """ Basic controller """
    def __init__(self, model, view, parent=None):
        super(RecordingTableWidgetController, self).__init__(parent)
        self.model = model
        self.view = view

        self.view.connect(self.view,
                SIGNAL("ROWCLICKED"), self.handle_item_selected)

        self.view.populate(self.model)

    def previous_page(self):
        """ Change pages in the model and update the view """
        self.model.previous_page()
        self.view.populate(self.model)

    def next_page(self):
        """ Change pages in the model and update the view """
        self.model.next_page()
        self.view.populate(self.model)

    def show(self):
        """ Show the view """
        self.view.show()

    def handle_item_selected(self, row):
        """ Handles the ROWCLICKED method, setting the models current
        selected row to that of the table view """
        self.model.selected = row
        # Re emit
        self.emit(SIGNAL("ROWCLICKED"), row)
###############################################################################
# Model
###############################################################################
class RecordingTableWidgetModel(object):
    """
    A model that manages and coordinates access to data from the rails api
    """
    def __init__(self, rdb_proxy):
        self.current_page = 1
        self.rdb_proxy = rdb_proxy
        self.pages = Pages(rdb_proxy)
        self.pages.get(self.current_page) # get the first page
        self._selected = []
        self._current_row = None

    def _set_selected(self, row):
        """
        takes an integer param. Attempts to create a list of the recording_ids
        that correspond the the currently selected item in the tableview
        """
        self._selected = []

        if row != None:
            self._current_row = row
            bookings = self.pages.get(self.current_page).json()
            for recording in bookings[row]['recordings']:
                self._selected.append(recording['id'])

    def _get_current_row(self):
        """ Return a list of the currently select recording_ids """
        return self._current_row
    current_row = property(_get_current_row)





    def _get_selected(self):
        """ Return a list of the currently select recording_ids """
        return self._selected
    selected = property(_get_selected, _set_selected)

    def next_page(self):
        """
        Attempt to get the next set of bookings from the pages backing store.
        """
        self._current_row = None
        if self.current_page < self.pages.page_count:
            # Only pagination data returned
            self.current_page += 1

        self.pages.get(self.current_page)
        self.selected = None

    def previous_page(self):
        """
        Attempt to get the previous set of bookings from the pages backing
        store.
        """
        self._current_row = None
        if self.current_page > 1: # Only pagination data returned
            self.current_page -= 1

        self.pages.get(self.current_page)
        self.selected = None

###############################################################################
# Container for pages returned from the rest api
###############################################################################
class Pages(object):
    def __init__(self, rdb_proxy):
        self.pages = {}
        self.rdb_proxy = rdb_proxy
        self.page_count = 0

    def get(self, page_number):
        if not page_number in self.pages:
            self.pages[page_number] = Page(page_number, self.rdb_proxy)

            # update page count
            self.page_count = 1 + self.pages[page_number].total_entries / self.pages[page_number].per_page

        return self.pages[page_number]

###############################################################################
class Page(object):
    """
        Acts as a cache for the session info from the rails rest api.
        Expires after 60 seconds.
    """
    def __init__(self, page_number, rdb_proxy):
        self.expire = 60 # seconds
        self.page_number = page_number
        self.rdb_proxy = rdb_proxy

        self._cache = self._last_updated = self._per_page \
                = self._total_entries = None

        self.refresh_cache()

    def _get_total_entries(self):
        """ Return the number of entires TOTAL available """
        return self._total_entries
    total_entries = property(_get_total_entries)

    def _get_per_page(self):
        """ Return the number of entries per page """
        return self._per_page
    per_page = property(_get_per_page)

    def _get_last_updated(self):
        """ return the time the cache was last updated """
        return self._last_updated
    last_updated = property(_get_last_updated)

    def expired(self):
        """
        Test if the cache has expired.
        """
        if datetime.now() > self.last_updated + timedelta(0, self.expire):
            return True
        return False

    def refresh_cache(self):
        """
        Refresh the page/json cache from the rails server.
        """
        self._cache = self.rdb_proxy.bookings(self.page_number)
        self._total_entries = \
                int(self._cache[-1]['pagination']['total_entries'])
        self._per_page = int(self._cache[-1]['pagination']['per_page'])
        del self._cache[-1] # Remove the last line which will contain
                            # the pagination information.
        self._last_updated = datetime.now()

    def json(self):
        """
        Return the raw json from the cache, refreshing if it has expired.
        """
        if self.expired():
            self.refresh_cache()

        return self._cache

import sys
def main(args):
    app = QApplication(args)

    table = RecordingTableWidget()
    table.resize(640, 480)
    table.show()

    sys.exit(app.exec_())

if __name__=="__main__":
    main(sys.argv)
