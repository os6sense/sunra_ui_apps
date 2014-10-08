
import pytz
from dateutil.parser import parse
from datetime import datetime

from sunra.presenters import TimePresenter
from i18n import *

def _(val):
    return val

###############################################################################
# ProjectPropertiesModel
###############################################################################
class ProjectPropertiesModel(object):
    def __init__(self, project=None, booking=None):
        self._date = None
        self._start_time = None
        self._end_time = None

        if project:
            self.uuid = project['uuid']
            self.project_name = project['project_name']
            self.client_name = project['client_name']

            if booking:
                self.booking_id = booking['id']
                self.date = booking['date']
                self.start_time = booking['start_time']
                self.end_time = booking['end_time']
                self.facility_studio = booking['facility_studio']

    #####################
    # end_time property
    #####################
    def _get_end_time(self):
        """ Return the end time of a booking """
        return self._end_time
    def _set_end_time(self, value):
        """ sets the end_time. If a string is passed, conversion to a datetime
        is attempted via parse """
        if isinstance(value, datetime):
            self._end_time = value
        else:
            self._end_time = parse(value)

        self._end_time = self._end_time.replace(tzinfo=pytz.utc)

    end_time = property(_get_end_time, _set_end_time)

    #####################
    # start_time property
    #####################
    def _get_start_time(self):
        """ Return the star time of a booking """
        return self._start_time
    def _set_start_time(self, value):
        """ sets the start_time. If a string is passed, conversion to a datetime
        is attempted via parse """
        if isinstance(value, datetime):
            self._start_time = value
        else:
            self._start_time = parse(value)

        self._start_time = self._start_time.replace(tzinfo=pytz.utc)

    start_time = property(_get_start_time, _set_start_time)

    #####################
    # date property
    #####################
    def _set_date(self, value):
        if isinstance(value, datetime):
            self._date = value
        else:
            self._date = parse(value)
    def _get_date(self):
        """ return the project date if set, otherwise return todays date """
        if self._date is not None:
            return self._date

        return datetime.now()

    date = property(_get_date, _set_date)

    #####################
    # studio_id property
    #####################
    def _get_studio_id(self):
        """ get studio id """
        return self.facility_studio
    def _set_studio_id(self, value):
        """ set studio id """
        self.facility_studio = value
    studio_id = property(_get_studio_id, _set_studio_id,
            doc="Alias for facility_studio")

    #####################
    # current time as a property
    #####################
    def _get_current_time(self):
        """ Helper - provides the current time with utc tz info """
        return datetime.now().replace(tzinfo=pytz.utc)#(pytz.utc)

    current_time = property(_get_current_time,
            doc="Calculate Current Time with utc info")

    def booking_is_active(self):
        """ Return true if the booking is active i.e. it has started
        and has yet to finish """
        if self.start_time < self.current_time \
                and self.end_time > self.current_time:
            return True

        return False

    def _check_for_overlap(self, projects):
        """
        Ensure that the model dates do not overlap with any other booking.

        Params::
        projects which is the list of projects and bookings as returned from
        the rest api call.
        """
        errors = []
        for project in projects:
            for booking in project['bookings']:
                if self._overlap(self.start_time,
                        self.end_time,
                        booking['start_time'],
                        booking['end_time']) >= 0:

                    errors.append(self._overlap_error(project['project_name'],
                            booking['start_time'],
                            booking['end_time']))

        return errors

    def _overlap(self, a_start, a_end, b_start, b_end):
        """
        Helper, given 2 times with a start and end, check if they overlap

        Params::
        a_start: start of the first time
        a_end: end of the first time
        b_start: start of the datetime period to compare against
        b_start: end of the datetime perdiod to compare against
        """
        return (a_start - parse(b_end).replace(tzinfo=pytz.utc)).total_seconds() * \
                        (parse(b_start).replace(tzinfo=pytz.utc) - a_end).total_seconds()

    def _overlap_error(self, project, start, end):
        """ Helper - format overlap error message """
        err = "Project overlaps with another booking project:" \
            " %s booked between %s and %s" \
            % (project, TimePresenter(start), TimePresenter(end) )
        return _(err)

    def verify(self, projects):
        """
        Verify that the fields are valid values
        """
        errors = []
        min_title_warning = _("Project Title MUST be a minimum of " \
                            "4 characters in length.")
        min_client_warning = _("Client Name MUST be a minimum of " \
                                "4 characters in length.")

        if len(self.project_name) < 4:
            errors.append(min_title_warning)

        if len(self.client_name) < 4:
            errors.append(min_client_warning)

        # check for overlapping booking times
        overlap_errors = self._check_for_overlap(projects)

        if len(overlap_errors) > 0:
            errors.append(overlap_errors)

        if len(errors) > 0:
            return errors

        return []

    def create_project(self, proxy):
        """
        Create a new project using the proxy. Sets uuid to the proxys
        first return value.

        Returns::
        An array containing any errors that were encountered when creating the
        project.
        """
        self.uuid, errors = proxy.create_project(self.client_name,
                self.project_name)

        return errors

    def create_booking(self, proxy):
        """
        Create a new booking using the proxy, passing self to the proxy
        and setting booking_id to the value returned.
        """
        # There will be the odd occassion when the start time of a group
        # overlaps with the end time of another. Usually this will be along
        # the lines of a one booking finishing at 5:00pm and another starting
        # directly after. In order to avoid times overlapping we add 1
        # second to the start time. THIS IS DONE IN THE RAILS BOOKING

        booking = proxy.create_booking(self.uuid, self)

        if not "id" in booking:
            return booking

        self.booking_id = booking["id"]

        # When the booking is created the utc time in the database will
        # differ from the time info provided hence update the start and
        # end time using the returned json values.
        self.date = booking['date']
        self.start_time = booking['start_time']
        self.end_time = booking['end_time']

    def extend_booking(self, proxy, value):
        self.end_time = proxy.extend_booking(self.uuid, self.booking_id, value)
        print self.end_time

    def update(self, proxy):
        """

        Update an existing project/booking via the rails api.
        """
        pass
