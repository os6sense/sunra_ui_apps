import requests
import json

from sunra.presenters import TimePresenter, DatePresenter

class RecordingDBProxy(object):
    """
    A minimal proxy interface to the rails REST API.
    """
    JSON_HEADER = {'content-type': 'application/json'}

    def __init__(self, config):
        self.api_key = config.api_key
        self.studio_id = config.studio_id
        self.resource_url = config.project_rest_api_url

        self.project_url = "%s/projects.json" % self.resource_url

    def get_current_booking(self, studio_id=-1):
        """
        Obtain booking information on any bookings which is currently
        running for a given studio.

        Params::
        +studio_id+ -- optional, if a studio id is not suppled the
        studio id from the config will be used.

        Returns::
        """
        if studio_id == -1:
            studio_id = self.studio_id

        params = {'studio_id': studio_id,
                  'auth_token': self.api_key,
                  'ppf': 'present'}

        return requests.get(self.project_url, params=params).json()

    # NB: I'd swear I merged this - theres a conflict here between
    # find project and find projects
    def find_project(self, client_name, project_name):
        params = {
                  'auth_token': self.api_key,
                  'client_name': client_name,
                  'project_name': project_name}

        r = requests.get(self.project_url, params=params)

        return r.json()[0]['uuid']

    def find_projects(self, client_name, project_name):
        """
        find projects which match both client and project name
        """
        params = {
                  'auth_token': self.api_key,
                  'client_name': client_name,
                  'project_name': project_name}

        return requests.get(self.project_url, params=params).json()

    def get_todays_bookings(self, studio_id=-1):
        """
        Find ALL bookings that are scheduled for *today*. This also
        includes any bookings that may have finished.

        See get_current_booking for bookings that are scheluled for *now*.

        Returns::
        """
        if studio_id == -1:
            studio_id = self.studio_id

        params = {'studio_id': studio_id,
                  'auth_token': self.api_key,
                  'ppf': 'today'}

        return requests.get(self.project_url, params=params).json()

    def _get(self, url, params):
        """
        untested, but provides a get method with basic headers and
        params for json gets.
        """
        headers = {'content-type': 'application/json'}
        params['auth_token'] = self.api_key

        return requests.get(url, params=params, headers=headers).json()

    def _post(self, url, data):
        """
        Helper to perform a post so that we dont have headers/params
        repeated everywhere.
        """
        headers = {'content-type': 'application/json'}
        params = {'auth_token': self.api_key}

        return requests.post(url, params=params,
                data=json.dumps(data), headers=headers)

    def _put(self, url, data):
        """
        COPY AND PASTE JOB - just changes post to put
        Helper to perform a post so that we dont have headers/params
        repeated everywhere.
        """
        params = {'auth_token': self.api_key}

        return requests.put(url, params=params,
                data=json.dumps(data), headers=self.JSON_HEADER)

    def create_project(self, client_name, project_name):
        """
        Create a new project.

        Params::
        client_name -- the name of the client
        project_name -- the name of the project

        Notes:

        The name of the client AND project when combined, must be unique,
        hence client "some client" cannot have more than one project called
        "some project"

        """
        data = {'project': {
                      'client_name': client_name,
                      'project_name': project_name
                   }
                }
        r = self._post(self.project_url, data)

        if r.status_code == 422:
            return 0, r.json()['errors']
        else:
            r.raise_for_status()

        return r.json()['uuid'], None


    def delete_project(self, uuid):
        """
        Delete a project given its uuid

        Params::
        +uuid+

        """
        params = {'auth_token': self.api_key}
        url = "%s/projects/%s" % (self.resource_url, uuid)
        requests.delete(url, params=params)

    def create_booking(self, uuid, booking_detail, studio_id=-1):
        """
        booking_detail -- a hash of the form
        """
        if studio_id == -1:
            studio_id = self.studio_id

        data = {
            'booking': {
                'facility_studio': studio_id,
                'date': DatePresenter(booking_detail.date),
                'start_time': TimePresenter(booking_detail.start_time, False),
                'end_time': TimePresenter(booking_detail.end_time, False)
             }
        }
        url = "%s/projects/%s/bookings.json" % (self.resource_url, uuid)

        r = self._post(url, data)

        if len(r.json()) == 1:
            # some sort of error occurred
            return r.json()

        return r.json()[1]

        # WE MIGHT HAVE A CONFLICT HERE SINCE THE METHODS HAVE DIVERGED
        # THIS IS THE RETURN USED BY ANYTHING THAT WAS USING THE **LIBRARY**
        # return self._post(url, data).json()[1]["id"]

    def extend_booking(self, uuid, booking_id, value):

        url = "%s/projects/%s/bookings/%s.json" % (self.resource_url,
                                                uuid,
                                                booking_id)
        params = {'f': 'nudge',
                   'time': value}

        response = self._get(url, params)
        return response['end_time']

    def recordings(self, uuid, booking_id):
        """
        Get all the recordings for a given project and booking.

        Params::
        uuid -- uuid of the project
        booking_id -- id of the booking

        """
        params = {'auth_token': self.api_key}

        url = "%s/projects/%s/bookings/%s/recordings.json" % (
                self.resource_url, uuid, booking_id)
        return requests.get(url, params=params).json()

    """
    These methods are those which are needed by the uploade UI in order to:
    1) List all bookings/session
    2) Obtain detail to display information about that session
        e.g number of recordings/groups, available format types
    3) Mark the recordings for a session for upload
    """

    def format_lookup(self):
        """
        Return the list of recording formats in use, along with the integer key
        for that format
        """
        params = {'auth_token': self.api_key}

        url = "%s/format_lookups.json" % (self.resource_url)
        return requests.get(url, params=params).json()

    def bookings(self, page=1):
        """
        return the details (json) for a session/booking
        """
        params = {'auth_token': self.api_key, 'page': page}

        url = "%s/bookings.json" % (self.resource_url)
        return requests.get(url, params=params).json()

    def formats(self, recording_id, scoping=None):
        """
        Obtain the list of available formats for a recording.
        """
        params = {'auth_token': self.api_key}

        if scoping:
            params[scoping] = 1

        if recording_id == None:
            url = "%s/recording_formats.json" % (self.resource_url)
        else:
            url = "%s/recordings/%s/recording_formats.json" % (
                self.resource_url, recording_id)

        print url

        return requests.get(url, params=params).json()

    def mark_for_upload(self, recording_format_id, value):
        """
        Mark a recording for upload
        """
        self._mark_format(recording_format_id, value, 'upload')

        url = "%s/projects/%s/bookings.json" % (self.resource_url,
                                                recording_format_id)

    def mark_for_copy(self, recording_format_id, value):
        """
        Mark a recording for upload
        """
        self._mark_format(recording_format_id, value, 'copy')

    def mark_for_encryption(self, recording_format_id, value):
        """
        Mark a recording for upload
        """
        self._mark_format(recording_format_id, value, 'encrypt')

    def mark_encrypted(self, recording_format_id, value):
        """
        Mark a recording for upload
        """
        self._mark_format(recording_format_id, value, 'encrypted')

    def mark_fixed(self, recording_format_id, value):
        """
        Mark a recording for upload
        """
        self._mark_format(recording_format_id, value, 'fixed_moov_atom')

    def _mark_format(self, rf_id, value, operation):
        """
        Helper to dry up the mark routines:

        rf_id : RecordingFormat ID
        op: 'upload', 'copy', 'encrypt', 'fixed_moov_atom'
        value: True or False
        """
        data = {'recording_format': {operation: value}}

        url = "%s/recording_formats/%s.json" % (self.resource_url, rf_id)
        result = self._put(url, data)
        result.raise_for_status()
