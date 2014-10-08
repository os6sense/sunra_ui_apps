import requests
import json

from presenters import TimePresenter, DatePresenter
"""

"""
#class BookingDetail:
    #"""
        #Simple container class for booking detail.
    #"""
    #def __init__(self, b_date, start_time, end_time, studio_id):
        #"""
        #Params::
            #b_date -- date of the booking
            #start_time -- start_time of the booking
            #end_time -- end time for the booking.
        #"""
        #self.facility_studio = studio_id
        #self.date = b_date
        #self.start_time = start_time
        #self.end_time = end_time

    #def to_json(self):
        #return json.dumps(self, default=lambda o: o.__dict__, 
                #sort_keys=True, indent=4)

    #def to_dict(self):
        #return {'facility_studio': self.facility_studio,
                #'date': self.date,
                #'start_time': self.start_time,
                #'end_time': self.end_time }

# I WAS USING THIS ONE RATHER THAN THE ONE IN THE LIB DIR!!!!
class RecordingDBProxy:
    """
    A minimal proxy interface to the rails REST API.
    """
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

        r = requests.get(self.project_url, params=params)

        return r.json()

    def find_project(self, client_name, project_name):
        params = {
                  'auth_token': self.api_key,
                  'client_name': client_name,
                  'project_name': project_name}

        r = requests.get(self.project_url, params=params)
        
        return r.json()[0]['uuid']

    def find_client(self, client_name):
        pass

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

        r = requests.get(self.project_url, params=params)
        
        return r.json()

    def _get(self, url, params):
        pass

    def _post(self, url, data):
        """
        Helper to perform a post so that we dont have headers/params
        repeated everywhere.
        """
        headers = {'content-type': 'application/json'}
        params = {'auth_token': self.api_key}

        return requests.post(url, params=params, 
                data=json.dumps(data), headers=headers)


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
        data = { 'project': {
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
        requests.delete(url, params=params )


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

    def update_start_time(self, booking_id, minutes):
        """
        # Given a booking id
        # if add x minutes to the booking doesnt result in overlap just do it

        # if it does result in overlap, move the overlapped bookings start time
        # ahead by the overlap + 01 seconds
        """
        pass

    def update_end_time(self, booking_id, minutes):
        """

        """
        pass


    def recordings(self, uuid, booking_id):
        """
        Get all the recordings for a given project and booking.

        Params::
        uuid -- uuid of the project
        booking_id -- id of the booking

        """
        params = { 'auth_token': self.api_key }

        url = "%s/projects/%s/bookings/%s/recordings.json" % (self.resource_url, uuid, booking_id)
        r = requests.get(url, params=params)
        
        return r.json()





class RecordingServiceProxy:
    """
    Calls the recording service via its rest api. The URL for the 
    recording service is set in the config file. 

    Start and Stop are obvious but it important to note that a booking
    MUST be scheduled for the studio at the date and time when the 
    call to start is made.
    """
    def __init__(self, config):
        self.api_key = config.api_key
        self.recording_service_url = config.recording_service_rest_api_url 

    def get(self, action):
        url = "%s/%s/" % (self.recording_service_url, action)

        params = { 'api_key': self.api_key }
        r = requests.get(url, params=params)
        
        return r.json()


    def start(self):
        """
        It takes your dog for a walk. What do you think it does?!

        Returns::
        The status after the recording service rest api has received a
        start command.
        """
        return self.get("start")

    def stop(self):
        """
        Really? 

        Returns::
        The status after the recording service rest api has received a
        stop command.
        """
        return self.get("stop")

    def status(self):
        """
        Returns the current status of the recording service.

        """
        return self.get("status")








